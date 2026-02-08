res = False
e = input("ENTER THE MAIL TO CHECK:")
if "@" in e and "." in e :
  res = True
if e.index("@")==0 or e.index("@")==-1 or e.index(".")==-1  :
  res = False
if res==True:
    print("THE MAIL IS VALID!")
else:
    print("THE MAIL IS NOT VALID!")
