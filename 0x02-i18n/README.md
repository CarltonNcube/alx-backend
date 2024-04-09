# Project 0x02: Internationalization (i18n)


This project focuses on implementing internationalization features in Flask web applications. 
The project covers parametrizing templates to display content in multiple languages, inferring 
the correct locale based on various factors, and localizing timestamps.

## Key Concepts:

### Internationalization (i18n):

Internationalization involves designing and developing software applications to support multiple languages and 
regions without modifying the source code. It enables users to interact with the application in their preferred language.

### Flask-Babel:

Flask-Babel is a Flask extension that facilitates internationalization and localization tasks in Flask applications.
It provides utilities for translating messages, formatting dates and times according to different locales, and managing language preferences.

### pytz:

pytz is a Python library that offers timezone definitions and utilities for working with timezones. 
It allows developers to handle timezone conversions and localize timestamps effectively.

## Learning Objectives:


- Gain a deeper understanding of internationalization concepts and their implementation in Flask applications.
- Learn how to parametrize Flask templates to display content in multiple languages based on user preferences.
- Understand how to infer the correct locale for a user based on various factors such as URL parameters, user settings, or request headers.
- Acquire proficiency in localizing timestamps and formatting dates and times according to different locales.


## Tasks:

### 0. Basic Flask app

- Set up a basic Flask app with a single route and an HTML template.
- The route should render the HTML template that displays "Welcome to Holberton" as the page title and "Hello world" as the header.

### 1. Basic Babel setup

- Install the Babel Flask extension and configure available languages.
- Set Babel’s default locale and timezone using a Config class.
- Utilize the configured settings for your Flask app.

### 2. Get locale from request

- Develop a function to retrieve the locale from the request using `request.accept_languages`.
- Determine the best-matched locale from supported languages and return it.

### 3. Parametrize templates

- Parametrize templates using the `_` or `gettext` function.
- Create a babel.cfg file for extracting translations from Python and Jinja templates.
- Initialize translations and edit translation files to provide translations for message IDs.
- Compile translation files and verify correct translations in templates.

### 4. Force locale with URL parameter

- Implement a method to force a specific locale by passing the `locale=fr` parameter to your app’s URLs.
- Detect and return the forced locale if it's supported; otherwise, use the default behavior.

### 5. Mock logging in

- Create a mock user login system with a user table.
- Define a function to get the user and set it as a global using `app.before_request`.
- Display a welcome message or default message based on user login status in the HTML template.

### 6. Use user locale

- Modify the function to get the locale to use the user’s preferred locale if supported.
- Test different user logins and verify the displayed locale in the application.

### 7. Infer appropriate time zone

- Define a function to infer the appropriate time zone based on URL parameters, user settings, or request headers.
- Validate and return the inferred time zone, defaulting to UTC if no valid time zone is found.


