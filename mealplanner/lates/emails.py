import smtplib
from email.mime.text import MIMEText

from mealplanner.lates.models import LateRecord

def sendLateCreatedEmail(lateid):

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

