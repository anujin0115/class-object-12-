# Exercise 1

class Rectangle:
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def area(self):
        return self.width*self.length
    def perimeter(self):
        return 2*(self.width+self.length)

class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: ${self.price}")

class ShoppingCart:
    def __init__(self):
        self.cart=[]
        self.prices=[]
        self.total=0
    def add_item(self,name,price):
        self.cart.append(name)
        self.prices.append(price)
        self.total += 1
    def total_price(self):

        self.amount=0
        for i in self.prices:
            self.amount+=i
        return self.amount
    def show_items(self):
        for p in range(self.total):
            print(f"{self.cart[p]}: ${self.prices[p]}")
