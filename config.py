import os

SECRET_KEY = os.environ.get(
    "SAFEROUTE_SECRET_KEY",
    "development-secret-key"
)

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": os.environ.get("SHRUTIRANDHE22", ""),
    "database": "saferoute",
    "port": 3306,
}

DEFAULT_CENTER = (20.5937, 78.9629)
DEFAULT_ZOOM = 5