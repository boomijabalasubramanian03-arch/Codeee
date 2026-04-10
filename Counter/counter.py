from collections import Counter
nums = eval(input("ENTER THE LIST OF NUMBERS:"))
d = Counter(nums)
nos = []
for i,j in d.items():
   if d[i]==1:
      nos.append(i)
print("THE NUMBERS THAT OCCURED ONLY ONCE ARE :",nos)
