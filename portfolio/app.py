from flask import Flask
from flask import render_template
from decouple import config

app = Flask(__name__)
CONTACT_FORM_ACTION = config('FORMSPREE_API')

@app.route('/')
def about(name=None):
    return render_template('about.html')

@app.route('/projects/')
def projects(name=None):
    return render_template('projects.html')

@app.route('/contact/')
def contact(name=None):
    return render_template('contact.html', api=CONTACT_FORM_ACTION)

if __name__ == '__main__':
	app.run(debug=True)
