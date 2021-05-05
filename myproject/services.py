"""
Flask services

The module provides a "registry" or "service locator" for other modules of the
application. It initializes stub objects for Flask extensions, that are configured
inside the app.py later on.

What services.py can import?
----------------------------

The module doesn't import anything from the project.



Who can import config.py?
--------------------------

The module is imported by different modules across the project, as necessary.
"""
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate(db=db)
