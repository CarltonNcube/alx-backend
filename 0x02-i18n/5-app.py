#!/usr/bin/env python3
"""
5-app module - A Flask app with user login emulation
"""

from flask import Flask, render_template, g
from flask_babel import Babel

app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

@app.before_request
def before_request():
    """
    Executed before all other functions
    """
    g.user = get_user()

def get_user():
    """
    Retrieve user based on login_as URL parameter
    """
    user_id = int(request.args.get('login_as', 0))
    return users.get(user_id)

@app.route('/')
def index():
    """
    Renders index.html template
    """
    return render_template('5-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

