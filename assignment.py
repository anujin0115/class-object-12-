# Exercise 1

class Rectangle:
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def area(self):
        return self.width*self.length
    def perimeter(self):
        return 2*(self.width+self.length)

# Exercise 2

class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: ${self.price}")


# Exercise 3
class ShoppingCart:
    pass
