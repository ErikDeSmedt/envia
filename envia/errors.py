class MissingEnvironmentVariable(Exception):
    def __init__(self, name: str):
        self._name = name

    def __str__(self):
        return f"EnvVar '{self._name}' is not set or empty"
