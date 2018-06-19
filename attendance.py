import random
import datetime
import calendar

def yearsFromJoin(emp):
    years= []
    now = datetime.datetime.now()
    for i in range(emp.year, now.year+1):
        years.append(i)
    return years

def monthsFromJoin(emp, year):
    months= []
    now = datetime.datetime.now()
    for i in range(0, len(year)):
        temp= []
        if year[i]== emp.year and year[i]== now.year:
            for j in range(emp.month, now.month+1):
                temp.append(j)
        else:
            if year[i] == now.year:
                for j in range(1, now.month+1):
                    temp.append(j)
            else:
                if year[i] == emp.year:
                    for j in range(emp.month, 13):
                        temp.append(j)
                else:
                    for j in range(1, 13):
                        temp.append(j)            
        months.append(temp)
    return months

def daysFromJoin(emp, year, month):
    days=[]
    now = datetime.datetime.now()
    for i in range(0, len(year)):
        temp1= []
        for j in range(0, len(month[i])):
            temp= []
            if(month[i][j] == now.month and emp.month==now.month and emp.year== year[i] and year[i] == now.year):
                for k in range(emp.day,now.day):
                    temp.append(k)
            else:
                if( month[i][j] == now.month and year[i]== now.year):
                    for k in range(1, now.day):
                        temp.append(k)
                else:
                    if( emp.month == month[i][j] and emp.year== year[i]):
                        for k in range(emp.day, int(max( calendar.monthrange(year[i],month[i][j]))+1)):
                            temp.append(k)
                    else:
                        for k in range(1, int(max( calendar.monthrange(year[i],month[i][j]))+1)):
                            temp.append(k)
            temp1.append(temp)
        days.append(temp1)
    return days

def workingHour(year,month,day):
    hours= []
    now = datetime.datetime.now()
    for i in range(0, len(year)):
        temp1= []
        for j in range(0, len(month[i])):
            temp2= []
            for k in range(0, len(day[i][j])):
                current= datetime.date(year[i],month[i][j],day[i][j][k])
                if current.weekday() == 6 or current.weekday() == 5:
                    temp2.append(0)
                else:
                    temp2.append(random.randrange(0,9))
            temp1.append(temp2)
        hours.append(temp1)                
    return hours

def salary(year,month,hours):
    salary= []
    for i in range(0, len(year)):
        temp1= []
        for j in range(0, len(month[i])):
            temp1.append(sum(hours[i][j])*1500)
        salary.append(temp1)  
    return salary

def getAttendance(joiningDate):
    year=  yearsFromJoin(joiningDate)
    month= monthsFromJoin(joiningDate,year)
    day= daysFromJoin(joiningDate,year,month)
    hours= workingHour(year, month, day)
    sal= salary(year, month, hours)
    return [year, month, day, hours, sal]
