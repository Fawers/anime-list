#!/usr/bin/env python

__author__ = "Fawers"

import os
from sys        import stderr
from urllib     import urlopen
from datetime   import datetime, timedelta
import settings, strings, ui
from parsers    import arg_parser as args, url_parser


if __name__ == '__main__':
    # Check for internet connection
    try:
        urlopen('http://www.google.com/').close()
    except IOError:
        print >>stderr, strings.get('no_connection')
        exit(8)

    # Check for specific date argument
    date     = args.get('date')
    if date: # Add to settings
        n = datetime.now()
        if date in ('yesterday','ontem'):
            settings.SETTINGS['date']    = n - timedelta(1)
            settings.SETTINGS['weekday'] = (n.isoweekday() - 1) % 7
        elif date in ('tomorrow','amanha'):
            settings.SETTINGS['date']    = n + timedelta(1)
            settings.SETTINGS['weekday'] = (n.isoweekday() + 1) % 7
        else: # YYYY-MM-DD format
            d = datetime(*map(int, date.split('-')))
            settings.SETTINGS['date']    = d
            settings.SETTINGS['weekday'] = d.isoweekday() % 7


    terminal = args.get('terminal')
    data     = url_parser.run()

    ui.send(data, terminal)
