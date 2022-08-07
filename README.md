# FinLit

![Build Status](https://img.shields.io/badge/build-passing-green)
![Python Verion](https://img.shields.io/badge/python-3.10-blue)

## Getting Started

### Installing Dependencies

#### Python 3.10

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the project directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

#### ENV File

Rename the `.env_example` file to `.env`.

#### DB Setup

In PHPMyAdmin/XAMPP, create a new database and name it `fin_lit`.
Copy the SQL from `fin_lit_prod.sql` and run it as a query in the new database on your local machine.

## Running the server

From within the `project` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

### Running the App

To run the sample, make sure you have `python` and `pip` installed.

Run `pip install -r requirements.txt` to install the dependencies and run `python server.py`. 
The app will be served at [http://localhost:3000/](http://localhost:3000/).