from flask import Flask


def test_app_class(app):
    assert isinstance(app, Flask)


def test_root_success(client):
    response = client.get('/')
    assert response.status_code == 200


def test_app_for_non_existing_endpoint(client):
    response = client.get('/foo')
    assert response.status_code == 404
