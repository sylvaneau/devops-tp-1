import app
import pytest

@pytest.fixture()
def client():
    return app.app.test_client()


@pytest.fixture()
def runner():
    return app.app.test_cli_runner()