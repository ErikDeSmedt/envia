import pytest
import os
from unittest import mock

from envia.env import EnvVar
from envia.errors import MissingEnvironmentVariable


def test_can_read_environment_variable():
    os_vars = {
        "OS_VAR_1": "some_value",
        "OS_VAR_2": "2",
    }

    v1 = EnvVar("OS_VAR_1")
    v2 = EnvVar("OS_VAR_2")

    # The mock defines the variables
    with mock.patch.dict(os.environ, os_vars):
        v1.get()
        assert v1.get() == "some_value"
        assert v2.get() == "2"

        # Check that the required variables pass
        v1.require()
        v2.require()


def test_missing_environment_variable():
    os_vars = {
        "THIS_IS_EMPTY_STRING": "",
    }

    v1 = EnvVar("THIS_IS_EMPTY_STRING")
    v2 = EnvVar("THIS_IS_NOT_SET")

    with mock.patch.dict(os.environ, os_vars):
        assert v1.get() is ""
        assert v2.get() is None

        with pytest.raises(MissingEnvironmentVariable):
            v2.require()


def test_require_returns_self():
    os_vars = {"APP_VAR_01": "value"}

    with mock.patch.dict(os.environ, os_vars):
        app_var_01 = EnvVar("APP_VAR_01").require()

        assert isinstance(app_var_01, EnvVar)
