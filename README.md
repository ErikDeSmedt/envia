# Envia

Did you ever lose track of all environment variables you can use to configure a project? Envia is a simple utility that allows you to group them together.

## Installation

```
pip install envia
```

## Usage

You can use Envia as follows

```python
# app/config.py

from envia import EnvVar

APP_DB_VENDOR = EnvVar("APP_DB_VENDOR", default="postgres")
APP_DB_PORT = EnvVar("APP_DB_PORT", default="5432")
APP_DB_HOST = EnvVar("APP_DB_HOST")

# require() can be used to ensure early failure. 
# This fails if APP_REQUIRED_VAR is not set
APP_REQUIRED_VAR = EnvVar("APP_REQUIRED_VAR").require()

```
To use the environment values you can do

```python
# app/db.py
import app.config as cfg

def connect():
	vendor = cfg.APP_DB_VENDOR.get_required()
	port = cfg.APP_DB_PORT.get_required()
	
	# This fails APP_DB_HOST is not set
	host = cfg.APP_DB_HOST.get_required()
	
	# This returns None if APP_DB_HOST is not set
	host = cfg.APP_DB_HOST.require()
```

