from fastapi.testclient import TestClient
from pytest import fixture
from ..app.models import database
from ..main import app
from motor.motor_asyncio import AsyncIOMotorClient
from ..app.models import client, MONGODB_URL


TEST_MONGO_URL = 'mongodb://mongo_test_db:27017'
test_client = AsyncIOMotorClient(TEST_MONGO_URL)

override_database = test_client.test_db

app.dependency_overrides[database] = override_database


@fixture(scope='module')
def client():

    with TestClient(app) as client:
        yield client
