# Example 1 - Hello, Flask!

Any good 'first program' requires a hello world, so we're going to be building a website, in which its only goal is to return the string 'Hello World!'.

This tutorial is taken from [Flasks own website](https://flask.palletsprojects.com/en/2.0.x/quickstart/).

## Setting up our Environment

This assumes you have completed the [initial setup](../setup/overview.md), such as having the latest version of Python, and a capable editor.

### Enter where you want to be, and create the directory

```sh
cd /somewhere/on/my/computer/i/want/to/put/this
mkdir hello-flask
cd hello-flask
pwd # ensure you are where you expect to be on your system!
```

### Create a virtual environment, activate it, install Flask

Covered in more detail [here](https://flask.palletsprojects.com/en/2.0.x/installation/#virtual-environments).

```sh
cd /somewhere/on/my/computer/i/want/to/put/this/hello-flask
python3 -m venv venv
. venv/bin/activate
pip install Flask
```

### Create the main file, fill it with the hello world code

```
cd /somewhere/on/my/computer/i/want/to/put/this/hello-flask
touch app.py
```

Open up the newly created `app.py` in your editor of choice, and fill it with this code:

```py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

An overview of this code from the Flask Quickstart guide:

> First we imported the Flask class. An instance of this class will be our WSGI application.
>
> Next we create an instance of this class. The first argument is the name of the application’s module or package. `__name__` is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.
>
> We then use the route() decorator to tell Flask what URL should trigger our function.
>
> The function returns the message we want to display in the user’s browser. The default content type is HTML, so HTML in the string will be rendered by the browser.

### Run the website

```
cd /somewhere/on/my/computer/i/want/to/put/this/hello-flask
flask run
```

Open up your browser to [http://localhost:5000/](http://localhost:5000/), and you should see this:

![](https://i.imgur.com/K3psQRs.png)

A nice empty white page with the text 'Hello, World!'
