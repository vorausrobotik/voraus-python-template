#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A cookiecutter for Python packages."""

from importlib_metadata import PackageNotFoundError, version

__module_name__ = "cookiecutter_pypackage"

try:  # pragma: no cover
    __version__ = version(__module_name__)
except PackageNotFoundError as error:  # pragma: no cover
    raise ModuleNotFoundError(
        f"Unable to determine version of package '{__module_name__}'. "
        "If you are on a local development system, use 'pip install -e .[dev]' in order to install the package. "
        "If you are on a productive system, this shouldn't happen. Please report a bug."
    ) from error
