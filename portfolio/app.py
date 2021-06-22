from flask import Flask
from flask import render_template
import decouple
import requests

GITHUB_USERNAME = decouple.config("GITHUB_USERNAME", default="jackharrhy")
GITHUB_REPOS_URL = f"https://api.github.com/users/{GITHUB_USERNAME}/repos?per_page=100"

CONTACT_FORM_ACTION = decouple.config("CONTACT_FORM_ACTION", default=None)

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
        projects.append(
            {
                "name": repo["name"],
                "description": repo["description"],
                "language": repo["language"],
                "url": repo["html_url"],
                "image": f"https://picsum.photos/seed/{repo['name']}/800/500",
            }
        )


@app.route("/")
def about_route(name=None):
    return render_template("about.html")


@app.route("/projects/")
def projects_route(name=None):
    return render_template("projects.html", projects=projects)


@app.route("/contact/")
def contact_route(name=None):
    return render_template("contact.html", api=CONTACT_FORM_ACTION)


if __name__ == "__main__":
    app.run(debug=True)
