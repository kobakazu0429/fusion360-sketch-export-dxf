from .src.commands import start, stop
from .src.lib import fusion360utils as futil


def run(context):
    try:
        start()

    except:
        futil.handle_error("run")


def stop():
    try:
        # Remove all of the event handlers your app has created
        futil.clear_handlers()
        stop()

    except:
        futil.handle_error("stop")
