import pytest
from app.models import User
from app import create_app
 
 
@pytest.fixture(scope='module')
def new_user():
    user = User(email='patkennedy79@gmail.com')
    user.set_password('unittest')
    return user

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('.env_test')
    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()

    yield db  # this is where the testing happens!

    db.drop_all()
