import os.path

# Settings for this mealplanner instance

# Path to database, relative to local_settings.py
DATABASE_PATH = "mealplanner.db"

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '../static/').replace('\\','/'),

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).

MEDIA_URL = 'http://18.214.1.236:81/'

# Time that the system switches over to the next day.  Set to "dinnertime" usually.
ROLLOVER_TIME = "19:00"
#ROLLOVER_TIME = "18:30"

# End of meal period dates


# Time to send email broadcast
BROADCAST_TIME = "18:00"

# Emails to receive broadcast
BROADCAST_EMAILS = "you@yourhost.com"
ENABLE_BROADCAST = False

# Email stuff
SMTP_SERVER = "127.0.0.1"
SMTP_PORT = 25
