class Animal:
   def speak(self):
      print("Animal Speaks")
class Bird(Animal):
   def speak(self):
      print("Tweet")
a = Animal()
a.speak()
b = Bird()
b.speak()
