from django.shortcuts import render_to_response
from django.conf import settings
from mealplanner.lates.models import LateRecord
from django.db.models import Q
from forms import LateSubmitForm
import datetime
from django.http import *
from utils import getWeekdayStr, getWeekday


def dashboard(request):
    todays_lates = LateRecord.objects.filter(Q(schedule="today") | Q(schedule__contains=datetime.datetime.today().weekday()))
    now = datetime.datetime.now()
    todays_weekday = getWeekday()
    todays_weekdaystr = getWeekdayStr()
    media_url = settings.MEDIA_URL
    for late in todays_lates:
        if late.type=="early":
            late.early = 1;

        if late.diet=="m":
            late.dietstring = "Meat"
        if late.diet=="v":
            late.dietstring = "Vegetarian"
        if late.diet=="v*":
            late.dietstring = "Vegan"

        late.restrictionstring = ""

        if late.glutenfree:
            late.restrictionstring = ", gluten free"
        if late.nonuts:
            late.restrictionstring += ", no nuts"
        if late.nopeanuts:
            late.restrictionstring += ", no peanuts"

        if late.restrictionstring:
            late.restrictionstring += "."

    return render_to_response('lates/dashboard.htm', {'current_date': now, 'media_url':media_url, 'todays_lates':todays_lates, 'todays_weekday':todays_weekday, 'todays_weekdaystr':todays_weekdaystr})


def signup(request):
    now = datetime.datetime.now()
    todays_weekday = getWeekday()
    todays_weekdaystr = getWeekdayStr()
    media_url = settings.MEDIA_URL
    globalError = ""

    if request.method == 'POST':    #handle submission
        form = LateSubmitForm(request.POST)
        if form.is_valid():
            #process data in form.cleaned_data
            cd = form.cleaned_data

            existing = LateRecord.objects.filter(email__startswith=cd['email'])
            if existing.count() > 0:
                globalError = "Your email is already in the database for today!"
            else:

                if cd['schedule']=='weekday':
                    sched = todays_weekday
                else:
                    sched = 'today'

                lr = LateRecord(name=cd['name'],date=now,email=cd['email'],type=cd['type'],schedule=sched,diet=cd['diet'],glutenfree=cd['glutenfree'],nonuts=cd['nonuts'],nopeanuts=cd['nopeanuts'])
                lr.save()
                return HttpResponseRedirect('/lates/signup-complete/'+str(lr.id))

    else:

        form = LateSubmitForm()

    return render_to_response('lates/signup.htm', {'current_date': now, 'media_url':media_url, 'todays_weekday':todays_weekday, 'todays_weekdaystr':todays_weekdaystr,'form': form, 'globalError':globalError})

def signupcomplete(request,id):
    now = datetime.datetime.now()
    todays_weekday = getWeekday()
    media_url = settings.MEDIA_URL
    form = LateSubmitForm()

    return render_to_response('lates/signup-complete.htm', {'current_date': now, 'media_url':media_url, 'todays_weekday':todays_weekday, 'form': form, 'late_id':id})
