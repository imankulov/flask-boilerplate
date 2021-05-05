import pytest

from myproject.app import app
from myproject.services import db


@pytest.fixture(autouse=True, scope="session")
def flask_app():
    """Initialize Flask application."""
    extra_config = {"SQLALCHEMY_DATABASE_URI": "sqlite://", "TESTING": True}
    app_instance = app(extra_config)
    with app_instance.app_context():
        yield app


@pytest.fixture
def database(flask_app):
    """A fixture for any database-related operations."""
    db.create_all()
    yield
    db.session.remove()
    db.drop_all()


@pytest.fixture
def client(flask_app):
    """Flask test client."""
    with flask_app.test_client() as client:
        yield client
