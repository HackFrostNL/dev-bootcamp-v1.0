from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def about(name=None):
    return render_template('about.html')

@app.route('/projects/')
def projects(name=None):
    return render_template('projects.html')

@app.route('/contact/')
def contact(name=None):
    return render_template('contact.html')

if __name__ == '__main__':
	app.run(debug=True)
