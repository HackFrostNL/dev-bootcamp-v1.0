# Example 3 - Rainbow Flask

Follow the same steps as [the first example](./example-1.md), but instead use this code:

```py
import random
from flask import Flask

app = Flask(__name__)

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

@app.route("/")
def rainbow():
    return f"""
<head>
    <style>
        body {{
            background-color: {random_color()}
        }}
    </style>
</head>
<body>
    <p>Rainbow Flask</p>
</body>
    """
```

Here, we import the random module, and we define a function that returns a random [hex color](https://en.wikipedia.org/wiki/Web_colors#Hex_triplet).

This route also contains a bit of [HTML](https://en.wikipedia.org/wiki/HTML), something the previous examples have very little of, because we want to style the background an arbitrary color, this will be covered in more detail later, but for now, if you run this, you will get a page that each time you refresh, will display a piece of text like before, but with a random colorful background!
