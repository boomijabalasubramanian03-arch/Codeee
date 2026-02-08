f = open("para.txt","r")
para = f.read()
p=para.split()
l1 = []
for i in p:
   c = 0
   for j in i:
      c+=1
   l1.append((i,c))
t = 1;lw=""
for j in l1:
   if j[1]>t:
      lw = j
      t = j[1]
print("THE PARA :",para)
print("LONGEST WORD IN THE PARAGRAPH:",lw)
print("THE REVERSED WORD IS : ",lw[0][::-1])
