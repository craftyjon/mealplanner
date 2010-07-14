
import datetime

def getWeekday():
    t = datetime.datetime.today().weekday();
    d = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday",}
    return d[t]
