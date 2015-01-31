'''\
Module designated to access the website in search of
the titles provided by list_parser. Also, this module
is responsible of finding both episode number and airtime
of each show.'''

__author__ = "Fawers"

import re
from urllib2   import urlopen
from datetime  import datetime, timedelta
import settings
import ansi
from AnimeList import AirTime
from parsers   import list_parser

URL = "http://animecalendar.net/{}/{}/{}"

def run():
    '''\
The main function of the url_parser module. This
function is responsible for querying the website
and fetching the desired data. Return value is a
list containing show title, episode number and
airtime. Such list will be ordered by airtime.'''
    now       = datetime.now()
    yesterday = now - timedelta(1)
    tomorrow  = now + timedelta(1)
    titles    = list_parser.parse()
    found     = [] # list of found titles and their airtimes

    episode_pattern = re.compile(r'ep: \d+', re.I)
    airtime_pattern = re.compile(r'(?<=at )\d\d:\d\d', re.I)

    for date in (yesterday, now, tomorrow):
        req  = urlopen(URL.format(date.year,date.month,date.day))
        data = req.read()
        req.close()

        for title in titles:
            match = re.search(title.query_pattern(), data)
            if match:
                match = match.group()
                ep    = episode_pattern.search(data, data.find(match)).group()
                airtm = airtime_pattern.search(data, data.find(match)).group()
                at    = AirTime(airtm, date) + settings.get('timezone_offset')

                if at.day == now.day:
                    found.append((title,ep,at))

        if found:
            titles = filter(lambda title: title not in zip(*found)[0],
                titles) # Remove found titles from main list

    return sorted(found, key=lambda t: t[2]) # sort by airtime
