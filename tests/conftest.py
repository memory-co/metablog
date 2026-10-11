import pytest
from fastapi.testclient import TestClient

from metablog.backend.config import Config
from metablog.backend.main import create_app


@pytest.fixture
def home(tmp_path, monkeypatch):
    monkeypatch.setenv("METABLOG_HOME", str(tmp_path))
    return tmp_path


@pytest.fixture
def client(home):
    return TestClient(create_app(Config.from_env()))


@pytest.fixture
def svc(client):
    return client.app.state
