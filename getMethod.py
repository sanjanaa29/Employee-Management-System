import random
import datetime
import calendar
import attendance

def getAddress():
    return ["H/217 Noida", "8006045155", "05619-283135" ]

def getDoJ():
    year = random.randrange(2000,2018)
    month= random.randrange(1,13)
    day= random.randrange(1,29)
    return datetime.date(year, month, day)

def getJobDetails(jDate):
    return attendance.getAttendance(jDate)