'''\
Being the central module, this will hold
the main constants.
'''
__author__ = "Fawers"

import os, platform


# Main directory
BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
# System name -> linux, windows, etc...
SYSTEM_NAME = platform.system().lower()
