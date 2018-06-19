import printing
import getMethod
import datetime    
# employee= [ "EmpCode", "Name", "DoJ", "ADDRESS", "Working Hours", "Permonth Salary",  ]

emp001= [ "Emp001", "Sanjana Sarbahi"]
emp002= [ "Emp002", "Candy Sarbahi"]
emp003= [ "Emp003", "Ambuj Ahuja"]
emp004= [ "Emp004", "Sanjeev Sarbahi"]
emp005= [ "Emp005", "Raji Sarbahi"]

employees= [ emp001, emp002, emp003, emp004, emp005]
totalEmp= len(employees)

for em in range(0,totalEmp):
    employees[em].append(getMethod.getDoJ())
    employees[em].append(getMethod.getAddress())
    employees[em].append(getMethod.getJobDetails(employees[em][2]))
    employees[em].append(employees[em][4])

def findingEmp(empl):
    for i in range(0,5):
        if(empl == employees[i][0]):
            empl=employees[i]
            return empl
    return "ErrorCode-1"

while 1:
    emp= findingEmp(input("\nEnter EmpID to access the details: "))
    if(emp != "ErrorCode-1"):
        printing.printBasicDetails(emp)
        while 1:
            print("\n--- select one from the given option ---")
            key= int(input(" 1. Contact Details \n 2. Working Hours Details \n 3. Salary Details \n 4. Exit: "))
            if key==1:
                printing.printContactDetails(emp)
            if key==3 or key==2:
                while 1:
                    year= int(input("   Please Enter the year: "))
                    if year >= emp[2].year and year <= datetime.datetime.now().year:
                        break
                    else:
                        print("Invalid Year try with another input.")
                        continue
                if key==2:
                    month= int(input("   Enter the month: "))
                    printing.printWorkingHours(emp[4],year,month)
                else:
                    printing.printSalary(emp[4],year)
            if key==4:
                break
            if(input("\nTo Display Other Details press 'y' and for exit press any other key: ")!= 'y'):
                break
    else:
        print("Can not find this EmpID, Try again with other EmpID....")
        if(input("\n\nFor continue press press 'y' and for exit press any other key--- ")!= 'y'):
            break
    if(input("\n\n For other Employees, press 'y', for exit press other key: ")!= 'y'):
        break