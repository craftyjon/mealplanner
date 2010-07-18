import datetime
from datetime import timedelta
from local_settings import ROLLOVER_TIME

def getWeekdayStr(t):
    delta = timedelta(days=1)

    if t.hour >= 19:
        t = t + delta

    tw = t.weekday()
    d = {6: "Sunday", 0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday",}

    return d[tw]

def getWeekday(t):
    delta = timedelta(days=1)

    if t.hour >= 19:
        t = t + delta

    tw = t.weekday()
    return tw

def getDietStr(d):
    if d=="m":
        return "Meat"
    if d=="v":
        return "Vegetarian"
    if d=="v*":
        return "Vegan"

    return "DIET_NULL"

def getDisplayTime():
    ''' Returns the current date and time in the context of displaying a late '''
    return getSignupTime()

def getSignupTime():
    ''' Returns the current date and time in the context of submitting a late '''
    now = datetime.datetime.now()
    cutoff = datetime.datetime.combine(datetime.date.today(),datetime.datetime.strptime(ROLLOVER_TIME, "%H:%M").time())
    if now.hour >= cutoff.hour:
        now = now + datetime.timedelta(days=1)
    return now
