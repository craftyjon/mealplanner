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

def overview(request):
    """Render the home view for the lates app."""
    # Make sure old lates are deleted
    expireLates()

    curdate = getDisplayDatetime()
    todays_weekday = getWeekday(curdate)
    todays_weekdaystr = getWeekdayStr(curdate)

    todays_lates = LateRecord.objects.filter(Q(schedule="today") | Q(schedule__contains=todays_weekday))



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

    return render_to_response('lates/overview.htm', {'current_date': curdate, 'media_url':media_url, 'todays_lates':todays_lates, 'todays_weekday':todays_weekday, 'todays_weekdaystr':todays_weekdaystr})

def dashboard(request):
    """Render the fullscreen dashboard view of the lates app."""
    # Make sure old lates are deleted
    expireLates()

    media_url = settings.MEDIA_URL
    curdate = getDisplayDatetime()
    todays_weekday = getWeekday(curdate)
    todays_weekdaystr = getWeekdayStr(curdate)

    todays_lates = LateRecord.objects.filter(Q(schedule="today") | Q(schedule__contains=todays_weekday))

    logged_in = False

    meta_user = ""

    meta_clock = getClock()

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

    return render_to_response('lates/dashboard.htm', {'current_date': curdate, 'media_url':media_url, 'todays_lates':todays_lates, 'todays_weekday':todays_weekday, 'todays_weekdaystr':todays_weekdaystr, 'logged_in':logged_in, 'meta_clock':meta_clock, 'meta_user':meta_user})

def signup(request):
    """Render the signup form for the lates app"""
    now = datetime.datetime.today()

    media_url = settings.MEDIA_URL
    globalError = ""
    curdate = getSignupTime()

    todays_weekday = getWeekday(curdate)
    todays_weekdaystr = getWeekdayStr(curdate)

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
                    exp = datetime.datetime.combine((curdate + delta), getExpiresTime())
                else:
                    sched = 'today'
                    exp = datetime.datetime.combine(curdate.date(), getExpiresTime())

                lr = LateRecord(name=cd['name'],date=now,email=cd['email'],type=cd['type'],expires=exp,schedule=sched,diet=cd['diet'],glutenfree=cd['glutenfree'],nonuts=cd['nonuts'],nopeanuts=cd['nopeanuts'])
                lr.save()
                return HttpResponseRedirect('/lates/signup-complete/'+str(lr.id))
    else:
        form = LateSubmitForm()

    return render_to_response('lates/signup.htm', {'current_date': curdate, 'media_url':media_url, 'todays_weekday':todays_weekday, 'todays_weekdaystr':todays_weekdaystr,'form': form, 'globalError':globalError})

def signupcomplete(request,id):
    """Render the signup complete page for the lates app"""
    curdate = getSignupTime()

    todays_weekday = getWeekday(curdate)
    todays_weekdaystr = getWeekdayStr(curdate)
    media_url = settings.MEDIA_URL
    form = LateSubmitForm()

    try:
        late = LateRecord.objects.get(id=id)
    except LateRecord.DoesNotExist:
        print "mealplanner.lates.views.signupcomplete: late not found (line 131)"
        late.schedule = "today"
    weekly = True

    if late.schedule=="today":
        weekly = False

    #sendLateCreatedEmail(id)

    return render_to_response('lates/signup-complete.htm', {'current_date': curdate, 'media_url':media_url, 'todays_weekday':todays_weekday, 'todays_weekdaystr':todays_weekdaystr, 'form': form, 'late_id':id, 'weekly':weekly})
