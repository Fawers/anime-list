# -*- encoding: utf-8 -*-

import settings, strings
from ansi import get_code, reset, BOLD
from ansi.colors import get_fg, get_bg, reset_fg, reset_bg
from ansi.colors import RED, GREEN, YELLOW, CYAN, BLACK

def run(data):
    print '{}Anime -'.format(get_code(BOLD, get_bg(BLACK))),

    if not data:
        print '{}{}, {}{}'.format(get_code(get_fg(RED),get_bg(BLACK)),
            strings.get('weekdays')[settings.get('weekday')],
            settings.get('date').strftime(settings.get('date_format')),
            reset())
        print '{}{}{}'.format(get_code(BOLD,get_fg(RED),get_bg(BLACK)),
            strings.get('no_anime'), reset())
    else:
        # get length of the biggest title
        tmaxlen = max(len(d[0].title) for d in data)
        # and the length of the biggest episode string
        emaxlen = max(len(d[1]) for d in data)

        print '{}{}, {}{}'.format(get_code(get_fg(GREEN),get_bg(BLACK)),
            strings.get('weekdays')[settings.get('weekday')],
            settings.get('date').strftime(settings.get('date_format')),
            reset())
        for chunk in data:
            print ('{}{:%is}{} =>' %tmaxlen).format(get_code(BOLD,get_fg(GREEN),
                get_bg(BLACK)), chunk[0].title, get_code(reset_fg())),
            print ('{}{:%is}{} {}' %emaxlen).format(get_code(get_fg(YELLOW)), chunk[1],
                get_code(reset_fg()), strings.get('at')),
            print '{}{}{}'.format(get_code(get_fg(CYAN)), chunk[2],
                reset())

