from tests.test_configs.config_helper import (
    load_and_validate,
    load_and_validate_fails,
    load_config,
)
from pencil_pusher.configs import config_manager


def test_valid():
    """
    Tests that a valid config file contains the required
    parameter title_prefix
    """
    load_config()
    load_and_validate()


def test_invalid_type():
    """
    """
    load_config(title_prefix=3)
    load_and_validate_fails()


def test_not_defined():
    """
    """
    load_config(exclude=["title_prefix"])
    load_and_validate()


def test_get_title_prefix():
    """
    """
    expected = "myprefix"

    load_config(title_prefix=expected)
    load_and_validate()

    response = config_manager.get("title_prefix")
    assert response == expected


def test_get_title_prefix_default():
    """
    """
    load_config(exclude=["title_prefix"])
    load_and_validate()

    response = config_manager.get("title_prefix")
    assert response == ""
