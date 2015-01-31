#!/usr/bin/env python

__author__ = "Fawers"

import os
from sys     import stderr
from urllib  import urlopen
import strings, ui
from parsers import arg_parser as args, url_parser


if __name__ == '__main__':
    # Check for internet connection
    try:
        urlopen('http://www.google.com/')
    except IOError:
        print >>stderr, strings.get('no_connection')
        exit(8)

    terminal = args.get('terminal')
    data     = url_parser.run()

    ui.send(data, terminal)
