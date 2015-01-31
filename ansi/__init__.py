'''\
This module provides the necessary functions
to stylize terminal output, including color
codes. Use the given constants as arguments
to the given functions in order to get the
proper codes.
**To be used on Linux only**'''

__author__ = "Fawers"

# Importing colors here will avoid the need
# to import it separetaly. As soon as ansi
# is imported, colors can be referenced by
# ansi.colors.
import colors
import settings

RESET       = 0
BOLD        = 1
FAINT       = 2
ITALIC      = 3
UNDERLINE   = 4
INVERTED    = 7
STRIKED     = 9

CANCEL = {
    BOLD:       22,
    FAINT:      22,
    ITALIC:     23,
    UNDERLINE:  24,
    INVERTED:   27,
    STRIKED:    29
}

# Both functions should be defined only if the
# current system is Linux. ANSI color codes
# have no effect in Command Prompt.
if 'linux' in settings.get('system_name',''):
    def get_code(*codes):
        '''\
Use as many codes as you want. In the end,
they will be represented by a single ANSI
string.
Example:
        get_code(BOLD, UNDERLINE, color.get_fg(color.RED))
    ->  get_code(1, 4, 31)
    ->  \\033[1;4;31m'''
        return '\033[' + ';'.join(map(str,codes)) + 'm'

    def reset():
        '''\
Utility function to return a RESET code.'''
        return get_code(RESET)
else:
    # Otherwise, make them return an empty string.
    def get_code(*codes):
        return ''
    def reset():
        return ''
