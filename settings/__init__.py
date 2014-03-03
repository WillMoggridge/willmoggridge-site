from settings.live import *

# TODO: Add logic for loading dev settings if environment variable is set

# Local environment settings.
try:
    from settings.local_settings import *
except ImportError:
    raise Exception("Error importing local_settings.py")
