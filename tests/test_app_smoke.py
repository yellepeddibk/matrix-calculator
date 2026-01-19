"""Smoke test to verify the Flask app can be imported and started."""

from flask import Flask


def test_app_imports(app):
    """Test that the Flask app module can be imported successfully."""
    assert app is not None


def test_app_is_flask_instance(app):
    """Test that app is a Flask instance."""
    assert isinstance(app, Flask)


def test_app_has_routes(app):
    """Test that the app has the expected routes defined."""
    rules = [rule.rule for rule in app.url_map.iter_rules()]
    assert "/" in rules
    assert "/api/determinant" in rules
    assert "/api/rref" in rules
