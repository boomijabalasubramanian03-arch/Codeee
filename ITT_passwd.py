upper=lower=symbol=digit=False
p = input("ENTER A VALID PASSWORD:")
i = 0
while len(p)>=8 and i<len(p):
     if ord(p[i])>=65 and ord(p[i])<=90:
      upper=True
     if ord(p[i])>=97 and ord(p[i])<=122:
      lower=True
     if p[i] in "!@-_$%^&*()<>?":
      symbol=True
     if p[i] in "0123456789":
      digit=True
     i+=1
if upper==True and lower==True and symbol==True and digit==True:
    print("VALID PASSWORD!")
else:
    print("NOT A VALID PASSWORD!")
