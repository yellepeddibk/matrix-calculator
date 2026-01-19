"""Pytest configuration to ensure project root is in Python path."""

import sys
from pathlib import Path

import pytest

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


@pytest.fixture(scope="session")
def app():
    """Provide Flask app instance for tests."""
    from webapp.app import app as flask_app
    return flask_app
