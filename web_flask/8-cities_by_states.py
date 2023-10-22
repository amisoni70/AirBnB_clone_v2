#!/usr/bin/python3
"""
A script that starts a web flask app
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.teardown_appcontext
def appteardown_handle(self):
    """
    A method to handle the app teardown
    """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_states():
    """
    A method to render a list of cities
    that are present within each state
    """
    all_states = sorted(storage.all(State).values(),
                        key=lambda x: x.name)

    state_cities = {}
    for state in all_states:
        state_cities[state.id] = sorted(
            [city for city in state.cities],
            key=lambda city: city.name
        )

    return render_template('8-cities_by_states.html',
                           all_states=all_states, state_cities=state_cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
