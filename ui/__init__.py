'''\
This module provides the necessary function
to display the output. Either if is Windows
or Linux, or even if it's supposed to show
on the terminal, this module is what decides
what interface will be used.'''

__author__ = "Fawers"

import settings, strings

def send(data, terminal):
    SYSTEM = settings.get('system_name')

    if terminal:
        import terminal
        terminal.run(data)
        return 
        # terminal interface treats the data
        # in a different way.
    elif 'linux' in SYSTEM:
        import linux as interface
    elif 'windows' in SYSTEM:
        import windows as interface
    else:
        return # nothing to do here


    if not data:
        data = [strings.get('no_anime')]
    else:
        data = ['{title} => {episode} {at} {airtime}'.format(
                title=chunk[0].title,episode=chunk[1],airtime=chunk[2],
                at=strings.get('at')) for chunk in data]

    interface.run(data)
