import datetime
from datetime import timedelta

def getWeekdayStr():
    t = datetime.datetime.today();
    delta = timedelta(days=1)
    if t.hour >= 19:
        t = t + delta
    tw = t.weekday()
    print tw
    d = {7: "Sunday", 0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday",}
    return d[tw]

def getWeekday():
    t = datetime.datetime.today();
    delta = timedelta(days=1)
    if t.hour >= 19:
        t = t + delta
    tw = t.weekday()
    return tw
