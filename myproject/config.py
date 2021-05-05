"""
Flask configuration.

The module doesn't depend on the project. The configuration file is initialized
with python-dotenv, and we don't read environment variables in the rest of the
project.


What config.py can import?
--------------------------

The module doesn't import anything from the project.


Who can import config.py?
---------------------------

The module is imported by the app.py but nowhere else!
"""
import os
import pathlib

import dotenv

dotenv.load_dotenv()


def adjust_database_uri(variable: str) -> str:
    # Heroku defines the database URL prefix as "postgres", but SQLAlchemy expects
    # "postgresql"
    if variable.startswith("postgres://"):
        variable = variable.replace("postgres://", "postgresql://")
    # In development, we may use {PROJECT_ROOT} in the URL to replace it with the
    # actual project root, for SQLAlchemy database path
    return variable.replace("{PROJECT_ROOT}", PROJECT_ROOT.as_posix())


# Common application and Flask settings. PROJECT_ROOT points to the root of the
# repository.
PROJECT_ROOT = pathlib.Path(__file__).parents[1]
SECRET_KEY = os.environ["SECRET_KEY"]

# SQLAlchemy settings
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = adjust_database_uri(os.environ["DATABASE_URL"])

# Other settings...
