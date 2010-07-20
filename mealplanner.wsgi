import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'mealplanner.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

sys.path.append('/var/www/servers/mealplanner')
sys.path.append('/var/www/servers/mealplanner/mealplanner')


