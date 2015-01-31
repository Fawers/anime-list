__author__ = "Fawers"

import argparse
import strings

# Parse args
_parser = argparse.ArgumentParser()
_parser.add_argument("-t", "--terminal", action="store_true",
    help=strings.get('arg_parser__terminal'))

ARGS = _parser.parse_args()

def get(arg, default=None):
    if arg in ARGS:
        return getattr(ARGS, arg)
    else:
        return default
