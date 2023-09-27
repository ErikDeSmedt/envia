""" Utilities to define enviornment variables
"""
import os
import typing as t

from envia.errors import MissingEnvironmentVariable


class EnvVar:
    def __init__(self, name: str, default: t.Optional[str] = None):
        self._name = name
        self._default = default

    def get(self, default: t.Optional[str] = None) -> t.Optional[str]:
        if default is None:
            default = self._default

        return os.environ.get(self._name, default)

    def get_required(self) -> t.Optional[str]:
        value = self.get()
        if value is None:
            raise MissingEnvironmentVariable(self._name)
        return value

    def require(self):
        return self.get_required()
