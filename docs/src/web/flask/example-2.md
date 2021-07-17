# Example 2 - Flask Math

Follow the same steps as [the first example](./example-1.md), but instead use this code:

```py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Flask Math</p>"

@app.route('/<int:number>')
def display_number(number):
    """ Displays a number back to the user as-is """
    return str(number)

@app.route('/<int:x>/add/<int:y>')
def add(x, y):
    """ Adds x and y, returns result """
    return str(x + y)

@app.route('/<int:x>/subtract/<int:y>')
def subtract(x, y):
    """ Subtracts y from x, returns result """
    return str(x - y)
```

Here, we're using routing within flask, and [variable rules](https://flask.palletsprojects.com/en/2.0.x/quickstart/#variable-rules) to take in input from the user, ensure we get it as a number, do some math, and return it back as a string.

Uses of this app include:

> http://localhost:5000/10 , displays `10` in the browser
>
> http://localhost:5000/10/add/20, returns `30`
>
> http://localhost:5000/10/subtract/20, returns `-10`

Try and take this code, and add some more math functions, such as multiplication and division, or go nuts and make it solve arbitrary equations, its up to you!
