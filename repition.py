l1=[];l2=[]
f = open("para.txt","r")
p = f.read().lower().split()
for i in p:
   i = i.lower()
   if i not in l1:
      l1.append(i)
   else:
      l2.append(i)
print("REPEATED WORDS ARE : ")
for k in l2:
   c = 1
   if k in p:
      c+=1
   print(k,":",c,end = " ")
print()
