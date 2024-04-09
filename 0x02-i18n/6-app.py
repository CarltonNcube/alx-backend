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
    # Check if the locale is provided in URL parameters
    locale_from_url = request.args.get('locale')
    if locale_from_url:
        return locale_from_url

    # Check if the user's locale is set
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']

    # Check the request header for accepted languages
    request_languages = [lang for lang, _ in request.accept_languages]
    for lang in request_languages:
        if lang in app.config['LANGUAGES']:
            return lang

    # Return the default locale if none of the above conditions are met
    return app.config['BABEL_DEFAULT_LOCALE']

@app.route('/')
def index():
    """
    Renders index.html template
    """
    return render_template('6-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
