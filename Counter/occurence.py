from collections import Counter
s = input("ENTER THE STRING:")
counts = Counter(s)
num = list(counts.values())
temp = num[0]
for i in num:
   if i==temp:
      flag = True
   else:
      flag = False
if flag==True:
   print("ALL CHARACTERS OCCUR SAME NO OF TIMES:")
else:
   print("ALL CHARACTERS DOES NOT OCCUR SAME NO OF TIMES:")  
