# -*- encoding: cp1252 -*-

import os
import settings, strings

def run(data):
    homedir  = os.getenv('USERPROFILE')
    vbscript = {
        "code":'MsgBox {text}, vbInformation, "Anime - {weekday}, {date}"\r\n',
        "name": "anime-notify.vbs"
    }
    filename = os.path.join(homedir,vbscript['name'])

    weekday  = strings.get('weekdays')[settings.get('weekday')]

    # Escape quotes
    data = [d.replace('"', '""') for d in data]

    text = '"' + '" & vbCrLf & "'.join(data) + '"'

    with open(filename, 'w') as script:
        script.write(vbscript['code'].format(
            text=text,
            weekday=weekday,
            date=settings.get('date').strftime(settings.get('date_format'))
        ))

    os.system('start /wait wscript "%s"' %filename)
    os.remove(filename)
