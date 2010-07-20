import smtplib
from email.mime.text import MIMEText

from local_settings import BROADCAST_EMAILS

from mealplanner.lates.models import LateRecord
from mealplanner.lates.utils import getDietStr, getTodaysLates, getDisplayTime

def sendLateCreatedEmail(lateid):
    ''' Send a confirmation email to the user after they submit the Sign Up form '''
    try:
        late = LateRecord.objects.get(id=lateid)
    except LateRecord.DoesNotExist:
        print "sendLateCreatedEmail: error: " +lateid+" not found in the database"
        return

    msg = MIMEText("Hello, "+late.name+".  You have signed up for a late using mealplanner.  To edit or cancel your late request, please visit http://mealplanner.cdawzrd.com/lates/edit/"+str(lateid)+"\n\nLove, mealplanner")
    msg['Subject'] = "Late confirmation from mealplanner"
    msg['From'] = "pika-lates@mit.edu"
    msg['To'] = late.email

    s = smtplib.SMTP()
    try:
        s.connect("localhost")
    except:
        print "Could not connect to SMTP server."
        return
    try:
        s.sendmail(msg['From'], [msg['To']], msg.as_string())
    except:
        print "low-level SMTP error."
    s.quit()

def sendBroadcastReminder():
    ''' Sends an email broadcast about today's lates '''
    todays_lates = getTodaysLates()
    today = getDisplayTime()
    msgStr = """
This is an automated message from mealplanner.

The following people have requested a late today:
"""

    if len(todays_lates) == 0:
        print "No lates to broadcast"
        return

    for late in todays_lates:
        msgStr += "\n" + late.name + " (" + late.diet
        if late.glutenfree:
            msgStr = ", gluten free"
        if late.nonuts:
            msgStr += ", no nuts"
        if late.nopeanuts:
            msgStr += ", no peanuts"
        msgStr += ")"
        if late.type=="early":
            msgStr += " -- Only if dinner will be served early"

    print "msgStr = " + msgStr

    msg = MIMEText(msgStr)
    msg['Subject'] = "mealplanner: lates requested for " +today.strftime("%a, %b %d")
    msg['From'] = "Mealplanner <pika-lates@mit.edu>"
    msg['To'] = "cdawzrd@gmail.com"

    s = smtplib.SMTP()
    try:
        s.connect('127.0.0.1')
        try:
            s.sendmail(msg['From'], [msg['To']], msg.as_string())
            s.quit()
        except:
            print "SMTP problem"
    except:
        print "Could not connect to SMTP server."
        return



    print "done"
