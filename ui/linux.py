# -*- encoding: utf-8 -*-

import os
import settings, strings

def run(data):
    summary = '"Anime - {}"'.format(strings.get(
        'weekdays')[settings.get('weekday')])
    text    = '\\n'.join(data).replace('"', r'\"')

    os.system('notify-send -u critical %s "%s"' %(summary,text))
