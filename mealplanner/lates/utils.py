import datetime
from datetime import timedelta

def getWeekdayStr(t):
    delta = timedelta(days=1)
    if t.hour >= 19:
        t = t + delta
    tw = t.weekday()
    d = {7: "Sunday", 0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday",}
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
