__author__ = "Fawers"

from re import match
from datetime import datetime, timedelta
import argparse

import settings
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


    if ARGS.date is not None:
        date = ARGS.date

        n = datetime.now()

        if date == strings.get('yesterday'):
            n -= timedelta(days=1)

        elif date == strings.get('tomorrow'):
            n += timedelta(days=1)

        elif match(r'^-?\d+$', date): # integer check
            n += timedelta(days=int(date))

        elif any(date.lower() in wd.lower() + '-'
                 for wd in strings.get('weekdays')): # weekday check

            wd = settings.get('weekday')
            if date.endswith('-'):
                d = strings.get('weekdays').index(date[:-1].title())
                days = -((wd - d) % 7)
            else:
                d = strings.get('weekdays').index(date.title())
                if d < wd:
                    d += 7
                days = (d - wd)

            n += timedelta(days=days)

        else: # settings.get('date_format') format
            n = datetime.strptime(date, settings.get('date_format'))

        settings.SETTINGS['date'] = n
        settings.SETTINGS['weekday'] = n.weekday()

def get(arg, default=None):
    if arg in ARGS:
        return getattr(ARGS, arg)
    else:
        return default

_setup()

del _setup
