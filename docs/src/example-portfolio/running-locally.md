# Running the application locally

Instructions taken from [here](https://flask.palletsprojects.com/en/2.0.x/installation/), if you run into any issues might be good to reference this as well.

The application itself can be found [here](https://github.com/HackFrostNL/dev-bootcamp-v1.0/tree/main/example-portfolio) on our GitHub if you just wish to browse the source code without downloading it to your machine.

1. Clone the project from GitHub, and enter it; ensuring you're in the right directory (that contains files such as `app.py` and `requirements.txt` is very important, pretty much every step expects you to be in the one directory).

```sh
git clone https://github.com/HackFrostNL/dev-bootcamp-v1.0.git
cd ./dev-bootcamp-v1.0/example-portfolio
```

2. Ensure you're running Python 3, this is covered in more detail within the [setup](../setup/overview.md), but a good sanity check before continuing.

```sh
python3 --version
```

3. Create a virtual environment, so you can install packages locally to the project without populating the global python package namespace, and also without needing root to install packages either. More info on virtual environments [here](https://realpython.com/python-virtual-environments-a-primer/).

```sh
cd path/to/dev-bootcamp-v1.0/example-portfolio
python3 -m venv venv
```

4. Activate the virtual environment, depending on your shell this might be different.

```sh
cd path/to/dev-bootcamp-v1.0/example-portfolio
. venv/bin/activate
```

5. Install all of the required application dependencies.

```sh
cd path/to/dev-bootcamp-v1.0/example-portfolio
pip install -r requirements.txt
```

6. Finally, run the application, and then open your browser to [http://localhost:3000](http://localhost:3000); if everything went correctly you should now see the example application!

```sh
cd path/to/dev-bootcamp-v1.0/example-portfolio
flask run
```

Don't fret to ask for help in the Discord if you run into any issues with the above commands.
