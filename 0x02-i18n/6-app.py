#!/usr/bin/env python3
"""
6-app module - A Flask app with user login emulation and locale handling
"""

from flask import Flask, render_template, g, request
from flask_babel import Babel, _
import os

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

def get_user():
    """
    Retrieve user based on login_as URL parameter
    """
    user_id = int(request.args.get('login_as', 0))
    return users.get(user_id)

def get_locale():
    """
    Determine user's preferred locale
    """
    # Check URL parameters
    locale_from_url = request.args.get('locale')
    if locale_from_url:
        return locale_from_url

    # Check user settings
    if g.user:
        user_locale = g.user.get('locale')
        if user_locale:
            return user_locale

    # Check request header
    locale_from_header = request.accept_languages.best_match(['en', 'fr', 'kg'])
    if locale_from_header:
        return locale_from_header

    # Default locale
    return 'en'

@app.before_request
def before_request():
    """
    Executed before all other functions
    """
    g.user = get_user()
    g.locale = get_locale()

@app.route('/')
def index():
    """
    Renders index.html template
    """
    return render_template('6-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

