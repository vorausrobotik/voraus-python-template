"""Contains all application utility functions."""

from {{cookiecutter.import_name}} import get_app_name, get_app_version
from pytest import MonkeyPatch


def test_get_app_name() -> None:
    assert "{{ cookiecutter.package_name }}" == get_app_name()


def test_get_app_version(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("{{ cookiecutter.import_name }}.__version__", "42.0.0")
    assert "42.0.0" == get_app_version()
