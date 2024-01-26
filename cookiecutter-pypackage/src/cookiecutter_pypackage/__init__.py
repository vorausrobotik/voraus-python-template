"""A cookiecutter for Python packages."""

from importlib_metadata import PackageNotFoundError as _PackageNotFoundError
from importlib_metadata import version as _version

__module_name__ = "cookiecutter_pypackage"


def get_app_name() -> str:
    """Returns the human-readable and prettified name of the application.

    Returns:
        The name of the application.
    """
    return __module_name__.replace("_", "-")


try:  # pragma: no cover
    __version__ = _version(__module_name__)
except _PackageNotFoundError as error:  # pragma: no cover
    raise ModuleNotFoundError(
        f"Unable to determine version of package '{__module_name__}'. "
        "If you are on a local development system, use 'pip install -e .[dev]' in order to install the package. "
        "If you are on a productive system, this shouldn't happen. Please report a bug."
    ) from error
