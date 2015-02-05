__author__ = "Fawers"

import time, json
from os.path    import join, exists, abspath, dirname
from sys        import stderr
from datetime   import datetime, timedelta
from __init__   import BASE_DIR, SYSTEM_NAME

def _setup():
    # Load settings
    # If the file is missing, terminate.
    # File: 'settings'
    global SETTINGS

    filename = join(BASE_DIR, 'settings')

    if not exists(filename):
        print >>stderr, "'settings' file not found!"
        exit(1)

    # Load settings
    with open(filename) as settings_file:
        SETTINGS = json.load(settings_file)

    # Update SETTINGS to join BASE_DIR with filename
    SETTINGS['filename'] = join(BASE_DIR, SETTINGS['filename'])


    # Change the settings file if you don't want the software to
    # calculate the offset each time. In such case, you must
    # provide the offset yourself in the else block.
    # Using automatic calculation is preferred unless undesired.
    if SETTINGS['calculate_offset']:
        # Create timezone info and add it to settings.
        _local, _utc = time.localtime(), time.gmtime() # local and UTC times
        
        # Convert struct_time objects to datetime objects
        local, utc  = datetime(*_local[:6]), datetime(*_utc[:6])
        
        local_tz    = local - utc
        tz_offset   = local_tz - timedelta(seconds=9*3600)
        # 9 because the standard timezone on AnimeCalendar.net
        # is UTC + 9 (Japan's timezone). And 3600s = 1h
    else:
        tz_offset   = timedelta() # Change this to the actual offset.
        # Hint: http://www.worldtimezone.com/


    SETTINGS['timezone_offset'] = tz_offset

    SETTINGS['system_name'] = SYSTEM_NAME

    SETTINGS['weekday'] = datetime.now().weekday()

def get(key, default=None):
    return SETTINGS.get(key, default)

# Run setup function
_setup()
