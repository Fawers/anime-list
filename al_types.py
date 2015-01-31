'''\
Module containing types originally written in
__init__.py. Transfer reason: to avoid path hacks.'''

__author__ = "Fawers"

from datetime import timedelta, datetime

class Title(object):
    '''\
Class used to represent Anime titles and,
if applicable, their respective queries.'''
    def __init__(self, title, query=None):
        self._title = title
        self._query = query

    def __repr__(self):
        if self._query:
            return "<Title: %s -> %s" %(self._title, self._query)
        else:
            return "<Title: %s>" %self._title

    @property
    def title(self):
        return self._title

    @property
    def query(self):
        if self._query:
            return self._query
        else:
            return self._title

    def query_pattern(self):
        '''\
Returns the regex pattern that will be used
to search the website.'''
        return r'(?i)' + self.query.replace('?', r'.*')



class AirTime(object):
    '''\
Class used to represent Anime airtime,
and to convert to local machine timezone.'''
    def __init__(self, time_string, datetime_obj):
        '''time_string should be "HH:MM"'''
        self._hour, self._minute = map(int,time_string.split(':'))
        if datetime_obj.strftime("%H:%M") != time_string:
            datetime_obj = datetime(*(datetime_obj.timetuple()[:3] +
                (self._hour, self._minute)))
        self._dt = datetime_obj

    @property
    def day(self):
        return self._dt.day

    def __repr__(self):
        return "%02d:%02d" \
            %(self._hour, self._minute)

    def __add__(self, offset):
        if isinstance(offset, int):
            hour = self._hour + offset
            if hour < 0:
                return AirTime("%02d:%02d" %(hour%24, self._minute),
                    self._dt+timedelta(days=-1))
            elif hour > 24:
                return AirTime("%02d:%02d" %(hour%24, self._minute),
                    self._dt+timedelta(days=1))
            else:
                return AirTime("%02d:%02d" %(hour, self._minute), self._dt)
        
        elif isinstance(offset, timedelta):
            dt = self._dt + offset
            return AirTime(dt.strftime("%H:%M"), dt)

    def __eq__(self, other):
        return self._dt == other._dt

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self._dt < other._dt

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)

    def __cmp__(self, other):
        if self < other:
            return -1
        elif self == other:
            return 0
        else:
            return 1
