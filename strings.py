__author__ = "Fawers"

import settings, json
from os.path    import join, exists
from __init__   import BASE_DIR
from sys        import stderr

def _setup():
    # Load strings file
    # Again, terminate if the file is missing
    # or if the language is not a valid one
    # File: 'strings' + language sufix
    # Check and load strings file
    global STRINGS

    if settings.get('language') in settings.get('language_options'):
        filename = join(BASE_DIR, 'strings.'+settings.get('language'))

        if not exists(filename):
            print >>stderr, "Missing a strings file for %s!" %settings.get('language')
            exit(2)

        with open(filename) as _strings:
            STRINGS = json.load(_strings)

    else:
        print >>stderr, "Language '%s' not available!" %settings.get('language')
        print >>stderr, "Select one from %s!" %settings.get('language_options')
        exit(4)

def get(key, default=None):
    string   = STRINGS.get(key, default)
    encoding = 'cp1252' if 'windows' in settings.get('system_name') else 'utf-8'
    
    if string.__class__ in (str, unicode):
        return string.encode(encoding)
    else: # list
        return [s.encode(encoding) for s in string]

# Run setup function
_setup()

# Cleanup namespace
del _setup
