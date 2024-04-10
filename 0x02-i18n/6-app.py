#!/usr/bin/env python3
"""
6-app module - A Flask app with user login emulation and locale handling
"""

from flask import Flask, render_template, g, request
from flask_babel import Babel, _

app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)

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


@app.before_request
def before_request():
    """
    Executed before all other functions
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Determine user's preferred locale
    """
    locale_from_url = request.args.get('locale')
    if locale_from_url:
        return locale_from_url
    if g.user and g.user.get('locale'):
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Renders index.html template
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
