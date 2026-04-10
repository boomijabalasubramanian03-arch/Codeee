class Fan:
   def __init__(self,speed="Medium"):
      self.speed = speed
   def status(self):
      print("THE STATUS OF THE FAN IS :",self.speed)
f1 = Fan()
f1.status()
f2 = Fan("Slow")
f2.status()
