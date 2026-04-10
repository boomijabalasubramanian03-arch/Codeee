class Book:
   def __init__(self,title,author):
      self.title = title
      self.author = author
   def display(self):
      print("TITLE OF THE BOOK:",self.title)
      print("AUTHOR OF THE BOOK:",self.author)
title = input("ENTER THE BOOK TITLE:")
author = input("ENTER THE AUTHOR:")
b = Book(title,author)
b.display()
