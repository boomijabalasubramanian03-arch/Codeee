d1 = {}
res = {}
desgn_pay = {
    "Scientist SC": 56100,
    "Scientist SD": 67700,
    "Engineer SE": 78800,
    "Engineer SF": 123100,
    "Technical Assistant": 44900,
    "Technician-B": 21700
}

def cal_sal(desgn,empid):
    basic = desgn_pay[desgn]
    da = 0.50 * basic
    hra = 0.24 * basic
    ta = 7200
    da_on_ta = 0.50 * ta
    gross = basic + da + hra + ta + da_on_ta

    pf = 0.10 * (basic + da)
    tax = 0.05 * gross

    deductions = pf + tax
    net = gross - deductions
    temp = d1.get(empid)
    print(temp)
    empnm = temp[0]
    res[empid] = [empnm,desgn,net]

def add_employee():
   empid = int(input("ENTER EMP ID:"))
   empnm = input("ENTER THE NAME:")
   desgn = input("ENTER DESIGNATION:")
   d1[empid] = [empnm,desgn,desgn_pay[desgn]]
   print("EMPLOYEE DETAILS ADDED SUCCESSFULLY!")

def view_employees():
   print("-------------------EMPLOYEE DETAILS------------------------")
   print("EMPID\tEMPNAME\t\tDESIGNATION\t\tSALARY")
   for i in res:
      print(i,"\t",res[i][0],"\t\t",res[i][1],"\t\t",res[i][2])
while True:
   print("----------------------EMPLOYEE PAYROLL SYSTEM--------------------------")
   print("-------------------------------MENU------------------------------------")
   print("1.ADD EMPLOYEES\n2.CALCULATE SALARY\n3.DISPLAY\n4.EXIT")
   ch = int(input("ENTER YOUR CHOICE:"))
   if ch==1:
      add_employee()
   elif ch==2:
      empid = int(input("ENTER THE EMPLOYEE ID:"))
      desgn = input("ENTER THE DESIGNATION:")
      cal_sal(desgn,empid)
   elif ch==3:
      view_employees()
   elif ch==4:
      print("THE END!")
      break
   else:
      print("INVALID CHOICE!")
   choice = input("DO YOU WANT TO CONTINUE:")
   if choice in "Nn":
      break
