import conftest
import pytest

def test_request_example(client):
    response = client.get("/countries")
    assert b"Thailand" in response.data