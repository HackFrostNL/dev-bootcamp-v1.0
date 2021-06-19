import os
import urllib
from datetime import datetime
from pathlib import Path

from flask import Flask, abort
from flask import render_template
import decouple
import requests
import markdown

GITHUB_REPOS_URL = "https://api.github.com/users/jackharrhy/repos?per_page=100"
CONTACT_FORM_ACTION = decouple.config("CONTACT_FORM_ACTION", default=None)

app = Flask(__name__)

projects = []

projects.append(
    {
        "name": "Non GitHub Project",
        "description": "a project i did not post on github that i am instead posting here",
        "language": None,
        "url": None,
        "image": "https://picsum.photos/seed/nongithub/800/500",
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
        projects.append(
            {
                "name": repo["name"],
                "description": repo["description"],
                "language": repo["language"],
                "url": repo["html_url"],
                "image": f"https://picsum.photos/seed/{repo['name']}/800/500",
            }
        )


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

            print(slug)

            post = {
                "date": date,
                "title": title,
                "html": html,
                "slug": slug,
            }

            blog_posts.append(post)
            blog_slug_to_post[slug] = post


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

    return render_template("blog_post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
