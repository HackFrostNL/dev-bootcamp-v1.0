import os
import urllib
from datetime import datetime
from pathlib import Path

from flask import Flask, abort
from flask import render_template
import decouple
import requests
import markdown
import sqlite3

GITHUB_USERNAME = decouple.config("GITHUB_USERNAME", default="jackharrhy")
GITHUB_REPOS_URL = f"https://api.github.com/users/{GITHUB_USERNAME}/repos?per_page=100"

DATABASE_PATH = "example-portfolio.db"
CONTACT_FORM_ACTION = decouple.config("CONTACT_FORM_ACTION", default=None)
REACTIONS = ["👍", "🔥", "💖️", "✨", "❄️"]

db_connection = sqlite3.connect(DATABASE_PATH)

db_cursor = db_connection.cursor()
db_cursor.execute(
    """
CREATE TABLE IF NOT EXISTS post_reaction (
    post_slug TEXT,
    value TEXT NOT NULL,
    amount INTEGER NOT NULL,
    PRIMARY KEY (post_slug, value)
)
"""
)
db_cursor.close()
db_connection.commit()

app = Flask(__name__)

projects = []

projects.append(
    {
        "name": "Non GitHub Project",
        "description": "a project i did not post on github that i am instead posting here, also a picture that isn't on the internet but instead is contained in the /static directory",
        "language": None,
        "url": None,
        "image": "/static/project.jpg",
    }
)

repos = requests.get(GITHUB_REPOS_URL).json()

github_projects_i_want_to_display = [
    "Storefront",
    "amogus",
    "DUaaS",
    "jackharrhy.com",
    "yaMUN",
]

for repo in repos:
    if repo["name"] in github_projects_i_want_to_display:
        print("adding github project", repo["name"])
        projects.append(
            {
                "name": repo["name"],
                "description": repo["description"],
                "language": repo["language"],
                "url": repo["html_url"],
                "image": f"https://picsum.photos/seed/{repo['name']}/800/500",
            }
        )

print(f"total of {len(projects)} projects added")


blog_posts = []
blog_slug_to_post = {}


with os.scandir("blog") as it:
    for entry in it:
        if entry.name.endswith(".md") and entry.is_file():
            raw_date, title = entry.name.split("_")
            title = title.rstrip(".md")

            date = datetime.strptime(raw_date, "%Y-%m-%d")

            post_markdown = Path(entry.path).read_text()
            html = markdown.markdown(post_markdown)

            slug = "".join(filter(str.isalnum, title))
            slug = urllib.parse.quote_plus(slug).lower()

            for reaction in REACTIONS:
                db_cursor = db_connection.cursor()
                db_cursor.execute(
                    "SELECT * FROM post_reaction WHERE post_slug = :slug AND value = :value",
                    {"slug": slug, "value": reaction},
                )
                results = db_cursor.fetchall()

                if len(results) == 0:
                    print(
                        f"creating post_reaction row for blog post '{title}' for reaction '{reaction}'"
                    )
                    db_cursor.execute(
                        """
                        INSERT INTO post_reaction (
                            post_slug,
                            value,
                            amount
                        ) VALUES (
                            :post_slug,
                            :value,
                            :amount
                        )
                        """,
                        {"post_slug": slug, "value": reaction, "amount": 0},
                    )

                db_cursor.close()

            db_connection.commit()

            post = {
                "date": date,
                "title": title,
                "html": html,
                "slug": slug,
            }

            blog_posts.append(post)
            blog_slug_to_post[slug] = post


print(f"total of {len(blog_posts)} blog posts added")


@app.route("/")
def about_route():
    return render_template("about.html")


@app.route("/projects/")
def projects_route():
    return render_template("projects.html", projects=projects)


@app.route("/contact/")
def contact_route():
    return render_template("contact.html", api=CONTACT_FORM_ACTION)


@app.route("/blog/")
def blog_route():
    return render_template("blog.html", blog_posts=blog_posts)


@app.route("/blog/<slug>")
def blog_post_route(slug):
    post = blog_slug_to_post.get(slug)

    if post is None:
        abort(404, description="Post not found")

    db_cursor = sqlite3.connect(DATABASE_PATH).cursor()
    db_cursor.execute(
        "SELECT value, amount FROM post_reaction WHERE post_slug = :slug",
        {"slug": slug},
    )
    results = db_cursor.fetchall()

    return render_template("blog_post.html", post=post, reactions=results)


@app.route("/api/react/<slug>/<value>")
def api_react(slug, value):
    if value not in REACTIONS:
        abort(400, description="Invalid value")

    post_exists = slug in blog_slug_to_post.keys()

    if not post_exists:
        abort(404, description="Post not found")

    db_connection = sqlite3.connect(DATABASE_PATH)
    db_cursor = db_connection.cursor()
    db_cursor.execute(
        "UPDATE post_reaction SET amount = amount + 1 WHERE post_slug = :slug AND value = :value",
        {"slug": slug, "value": value},
    )
    db_connection.commit()

    return '', 204


if __name__ == "__main__":
    app.run(debug=True)
