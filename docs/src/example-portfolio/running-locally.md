# Running the application locally

Instructions taken from [here](https://flask.palletsprojects.com/en/2.0.x/installation/), if you run into any issues might be good to reference this as well.

1. Make sure your terminal is in the right directory, otherwise none of commands will function correctly!

```sh
cd path/to/example-portfolio
```

2. Ensure you're running Python 3, this is covered in more detail within the [setup](/setup/overview.md), but a good sanity check before continuing.

```sh
python3 --version
```

3. Create a virtual environment, so you can install packages locally to the project without populating the global python package namespace, and also without needing root to install packages either.

```sh
python3 -m venv venv
```

4. Activate the virtual environment, depending on your shell this might be different.

```sh
. venv/bin/activate
```

5. Install all of the required application dependencies.

```sh
pip install -r requirements.txt
```

6. Finally, run the application, and then open your browser to [http://localhost:3000](http://localhost:3000); if everything went correctly you should now see the example application!

```sh
flask run
```

Don't fret to ask for help in the Discord if you run into any issues with the above commands.
