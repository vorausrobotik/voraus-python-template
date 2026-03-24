"""Contains all application utility functions."""

import pytest

from cookiecutter_pypackage import get_app_name, get_app_version


def test_get_app_name() -> None:
    assert get_app_name() == "cookiecutter-pypackage"


def test_get_app_version(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("cookiecutter_pypackage.__version__", "42.0.0")
    assert get_app_version() == "42.0.0"
