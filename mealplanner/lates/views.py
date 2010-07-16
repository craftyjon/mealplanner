import datetime

from django.shortcuts import render_to_response
from django.conf import settings
from django.db.models import Q
from django.http import *

from mealplanner.lates.models import LateRecord
from forms import LateSubmitForm
from utils import getWeekdayStr, getWeekday, getDietStr


def overview(request):
    """Render the home view for the lates app."""
    todays_lates = LateRecord.objects.filter(Q(schedule="today") | Q(schedule__contains=datetime.datetime.today().weekday()))
    now = datetime.datetime.now()
    todays_weekday = getWeekday(now)
    todays_weekdaystr = getWeekdayStr(now)
    media_url = settings.MEDIA_URL
    for late in todays_lates:
        if late.type=="early":
            late.early = 1;

        late.dietstring = getDietStr(late.diet)
        late.restrictionstring = ""

        if late.glutenfree:
            late.restrictionstring = ", gluten free"
        if late.nonuts:
            late.restrictionstring += ", no nuts"
        if late.nopeanuts:
            late.restrictionstring += ", no peanuts"

        if late.restrictionstring:
            late.restrictionstring += "."

    return render_to_response('lates/overview.htm', {'current_date': now, 'media_url':media_url, 'todays_lates':todays_lates, 'todays_weekday':todays_weekday, 'todays_weekdaystr':todays_weekdaystr})

def dashboard(request):
    """Render the fullscreen dashboard view of the lates app."""
    todays_lates = LateRecord.objects.filter(Q(schedule="today") | Q(schedule__contains=datetime.datetime.today().weekday()))
    now = datetime.datetime.now()
    todays_weekday = getWeekday(now)
    todays_weekdaystr = getWeekdayStr(now)
    media_url = settings.MEDIA_URL

    for late in todays_lates:
        if late.type=="early":
            late.early = 1;

        late.dietstring = getDietStr(late.diet)
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
    """Render the signup form for the lates app"""
    now = datetime.datetime.today()

    media_url = settings.MEDIA_URL
    globalError = ""

    if now.hour < 19:
        print "Before 7pm, no changes necessary"
        curdate = now;
    else:
        print "After 7pm, advancing a day"
        curdate = now + datetime.timedelta(days=1)

    todays_weekday = getWeekday(now)
    todays_weekdaystr = getWeekdayStr(now)

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
                    delta = datetime.timedelta(days=120)
                    exp = curdate + delta
                else:
                    sched = 'today'
                    exp = curdate

                lr = LateRecord(name=cd['name'],date=now,email=cd['email'],type=cd['type'],expires=exp,schedule=sched,diet=cd['diet'],glutenfree=cd['glutenfree'],nonuts=cd['nonuts'],nopeanuts=cd['nopeanuts'])
                lr.save()
                return HttpResponseRedirect('/lates/signup-complete/'+str(lr.id))
    else:
        form = LateSubmitForm()

    return render_to_response('lates/signup.htm', {'current_date': cd, 'media_url':media_url, 'todays_weekday':todays_weekday, 'todays_weekdaystr':todays_weekdaystr,'form': form, 'globalError':globalError})

def signupcomplete(request,id):
    """Render the signup complete page for the lates app"""
    now = datetime.datetime.now()

    if now.hour < 19:
        curdate = now;
    else:
        curdate = now + timedelta(days=1)

    todays_weekday = getWeekday(now)
    media_url = settings.MEDIA_URL
    form = LateSubmitForm()

    late = LateRecord.objects.filter(id=id)
    weekly = True

    if late[0].schedule=="today":
        weekly = False

    return render_to_response('lates/signup-complete.htm', {'current_date': curdate, 'media_url':media_url, 'todays_weekday':todays_weekday, 'form': form, 'late_id':id, 'weekly':weekly})
