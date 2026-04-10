 class Rectangle:
   def __init__(self,length,width):
      self.length = l
      self.width = w
   def area(self):
      return self.length*self.width
l = float(input("ENTER THE LENGTH OF THE RECTANGLE:"))
w = float(input("ENTER THE WIDTH OF THE RECTANGLE:"))
r = Rectangle(l,w)
print("AREA OF THE RECTANGLE IS :",r.area())
