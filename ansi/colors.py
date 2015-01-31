'''\
This module provides ANSI color codes for
terminal coloring. Use the get* functions
combined with ansi.get_code to get the
proper terminal coloring codes.

**To be used on Linux only**'''

__author__ = "Fawers"

import settings

FOREGROUND  = 30
BACKGROUND  = 40

BLACK       = 0b000
WHITE       = 0b111

RED         = 0b001
GREEN       = 0b010
BLUE        = 0b100

YELLOW      = RED   | GREEN
MAGENTA     = RED   | BLUE 
CYAN        = GREEN | BLUE


# In both functions, 'color' should be
# one of the constants listed above.
# Different values may cause unexpected
# behavior.

# Regarding OS: the same applies here.
# Below functions should be defined if,
# and only if, the system is Linux.

if 'linux' in settings.get('system_name',''):
    def get_fg(color):
        return FOREGROUND + color

    def get_bg(color):
        return BACKGROUND + color

    def reset_fg():
        return FOREGROUND + 9

    def reset_bg():
        return BACKGROUND + 9
else:
    def get_fg(color):
        return 0
    def get_bg(color):
        return 0
    def reset_fg():
        return 0
    def reset_bg():
        return 0
