'''\
Designated to read and parse the list file,
this module is what takes care of ignoring
comments (lines starting with semi-colons)
and separating titles from queries.'''

__author__ = "Fawers"

import os
import settings
from AnimeList import Title

def parse(filename=None):
    '''\
Returns a tuple with all the titles
and their respective queries.'''
    if not filename:
        filename = settings.get('filename')
    file_       = open(filename, 'r')
    title_list  = []

    for line in file_:
        # Remove any leading and trailing spaces, newlines, etc
        line = line.strip()
        # If the line starts with a ';', skip it; it's a comment
        if line and line[0] != ';':
            # Split data by '->' to separate title from query
            data    = map(str.strip, line.split('->'))
            title   = data[0]

            if len(data) == 2: # If the query exists...
                query = data[1]
                title_list.append(Title(title, query))
            else:
                title_list.append(Title(title))
    
    # Convert to a tuple so it becomes immutable
    return tuple(title_list)
