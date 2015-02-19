__author__ = "Fawers"

import argparse
import strings

def _setup():
    global ARGS
    # Parse args
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--terminal", action="store_true",
        help=strings.get('arg_parser__terminal'))
    parser.add_argument("-d", "--date",
        help=strings.get('arg_parser__date'))

    ARGS = parser.parse_args()

def get(arg, default=None):
    if arg in ARGS:
        return getattr(ARGS, arg)
    else:
        return default

_setup()

del _setup
