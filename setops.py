s1 = set();s2 = set()
n1 = int(input("ENTER NO OF STUDENTS IN FIRST DAY:"))
for i in range(0,n1):
    name = input("ENTER STUDENT NAME:")
    rollno = input("ENTER ROLL NUMBER:")
    s1.add((name,rollno))
n2 = int(input("ENTER NO OF STUDENTS IN SECOND DAY:"))
for i in range(0,n2):
    name = input("ENTER STUDENT NAME:")
    rollno = input("ENTER ROLL NUMBER:")
    s2.add((name,rollno))
print("STUDENTS IN BOTH DAYS :",s1&s2)
print("STUDENTS IN EITHER DAYS :",s1|s2)
print("STUDENTS ABSENT ON SECOND DAY :",s1-s2)
