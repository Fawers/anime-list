# -*- encoding: utf-8 -*-

import os
import settings, strings

def run(data):
    summary = '"Anime - {}, {}"'.format(
        strings.get('weekdays')[settings.get('weekday')],
        settings.get('date').strftime(settings.get('date_format'))
    )
    text = '\\n'.join(data).replace('"', r'\"')

    critical = '' if text == strings.get('no_anime') else '-u critical'

    os.system('notify-send -i "%s" %s %s "%s"' % (
              settings.get('icon'), critical, summary, text))
