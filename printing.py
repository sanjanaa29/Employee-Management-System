#EMPLOYEE: EmpCode, Name, DOJ, Add(add, Pph, Oph), Attendance, WorkingHours, Salary
import random
import datetime
import calendar
import getMethod

def printWorkingHours(data,year,month):
    print("\n-------Printing Working Hours Details of Month ",month," , year ",year," ------\n")
    years=data[0]
    months=data[1]
    day=data[2]
    hours=data[3]
    i = years.index(year)
    j= months[i].index(month)
    for k in range(0,len(day[i][j])):
        print("Date:    ", datetime.date(years[i],months[i][j],day[i][j][k]),"        Working Hourse: ", hours[i][j][k])

def printSalary(data,year):
    print("\n-------Printing Salary Details of year ",year," ------\n")
    years= data[0]
    months= data[1]
    salary= data[4]
    i= years.index(year)
    for j in range(0 , len(months[i])):
        print("Year:  ",year," and  Month: ",months[i][j],"        Salary: ", salary[i][j])

def printBasicDetails(data):
    print("\n-------Printing Basic Details--------\n") 
    print("Employee Code: ", data[0])
    print("Employee Name: ", data[1])
    print("Date of Joining: ", data[2])
    now= datetime.datetime.now()
    print("Current Date is: ",now.date())
    print("\nWorking hours Details of Current Month-------> ")
    printWorkingHours(data[4],now.year,now.month)
    print("\nSalary Details of Current Year----------> ")
    printSalary(data[5],now.year)
    
def printContactDetails(data):
    print("\n-------Printing Contact Details ------\n")
    print("    Add: ", data[3][0])
    print("    Personal Ph. ", data[3][1])
    print("    Office Ph. ", data[3][2])

