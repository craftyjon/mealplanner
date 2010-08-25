import datetime

from django.shortcuts import render_to_response
from django.conf import settings
from django.db.models import Q
from django.http import *

from models import MenuItem
from forms import MenuEditForm

def DisplayMenu(request):

    return render_to_response('menu/displaymenu.htm')

def EditMenu(request):

    return render_to_response('menu/editmenu.htm')
