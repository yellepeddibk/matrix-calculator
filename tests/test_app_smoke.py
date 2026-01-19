"""Smoke test to verify the Flask app can be imported and started."""


def test_app_imports():
    """Test that the Flask app module can be imported successfully."""
    from webapp.app import app
    assert app is not None


def test_app_is_flask_instance():
    """Test that app is a Flask instance."""
    from flask import Flask
    from webapp.app import app
    assert isinstance(app, Flask)


def test_app_has_routes():
    """Test that the app has the expected routes defined."""
    from webapp.app import app
    rules = [rule.rule for rule in app.url_map.iter_rules()]
    assert "/" in rules
    assert "/api/determinant" in rules
    assert "/api/rref" in rules
