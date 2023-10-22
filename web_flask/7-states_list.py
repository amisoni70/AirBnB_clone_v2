#!/usr/bin/python3
"""
A script that starts a web flask app
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def appteardown_handle(self):
    """
    A method to handle the app teardown
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    A method to render a list of states
    present
    """
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
