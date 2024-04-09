#!/usr/bin/env python3
"""
4-app module - A Flask app with forced locale parameter
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration class for the Flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@babel.localeselector
def get_locale():
    """
    Determine the best-matching language from the request
    """
    # Check if the request contains the 'locale' argument
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale
    else:
        return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    """
    Renders index.html template
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
