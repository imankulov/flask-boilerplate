"""
Flask application.

The module is used to initialize the main project: load configuration, attach
blueprints and initialize services.

What app.py can import?
-----------------------

Services, configuration, and everything that is needed to initialize blueprints,
including controllers and models inside apps. In other words, app.py depends on
a lot of things in the project.


Who can import app.py?
----------------------

The module is not imported from anywhere except from a WSGI server in
production, and conftests.py for pytest.
"""
from typing import Any, Optional

from flask import Flask
from roman_discovery.flask import discover_flask


def app(extra_config: Optional[dict[str, Any]] = None) -> Flask:
    """
    Initialize and return a Flask application.

    extra_config: a dict with extra configuration options, that need to be applied
    to the application before initializing.
    """
    flask_app = Flask(__name__, instance_relative_config=True)
    flask_app.config.from_object("{{ cookiecutter.project_slug }}.config")
    if extra_config:
        flask_app.config.from_mapping(extra_config)

    # Configure services and extensions
    discover_flask("{{ cookiecutter.project_slug }}", flask_app)
    return flask_app
