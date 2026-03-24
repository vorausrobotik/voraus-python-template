"""Contains all application utility functions."""

import pytest

from {{cookiecutter.import_name}} import get_app_name, get_app_version


def test_get_app_name() -> None:
    assert get_app_name() == "{{ cookiecutter.package_name }}"


def test_get_app_version(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("{{ cookiecutter.import_name }}.__version__", "42.0.0")
    assert get_app_version() == "42.0.0"
