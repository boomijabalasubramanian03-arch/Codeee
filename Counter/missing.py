from collections import Counter
list1 = eval(input("ENTER THE NOS OF LIST 1:"))
list2 = eval(input("ENTER THE NOS OF LIST 2:"))
c1 = Counter(list1)
c2 = Counter(list2)
no = []
for i in c2.values():
   if i not in list(c1.values()):
      temp = c2.items()
print("THE NOS OCCURING MORE TIMES THAN IN LIST 1 ARE :",no)
