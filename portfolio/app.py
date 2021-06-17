from flask import Flask
from flask import render_template
import decouple
import requests

GITHUB_REPOS_URL = "https://api.github.com/users/jackharrhy/repos?per_page=100"
CONTACT_FORM_ACTION = decouple.config('FORMSPREE_API', default="/contact")

app = Flask(__name__)

projects = []

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
        projects.append({
            "name": repo["name"],
            "description": repo["description"],
            "language": repo["language"],
            "url": repo["html_url"],
        })

@app.route('/')
def about_route(name=None):
    return render_template('about.html')

@app.route('/projects/')
def projects_route(name=None):
    return render_template('projects.html', projects=projects)

@app.route('/contact/')
def contact_route(name=None):
    return render_template('contact.html', api=CONTACT_FORM_ACTION)

if __name__ == '__main__':
	app.run(debug=True)
