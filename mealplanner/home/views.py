import datetime

from django.shortcuts import render_to_response
from django.conf import settings
from django.http import *



def homepage(request):
    """Render the home view for the mealplanner."""

    media_url = settings.MEDIA_URL

    return render_to_response('home/homepage.htm', {'media_url':media_url,})
