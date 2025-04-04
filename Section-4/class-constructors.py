class CardItem:
    #constructor
    def __init__(self, name, price, quantity):
        #instance attributes
        self.name = name
        self.price = price
        self.quantity = quantity

    #intance method
    def calculateTotal(self):
        total = self.price * self.quantity
        return total
    
    def applyDiscount(self,rate):
        self.price = self.price * (1-rate)

item1 = CardItem("Telefon", 50000, 2)
item2 = CardItem("Bilgisayar", 70000, 1)
item3 = CardItem("kitap", 500, 2)

item1.applyDiscount(0.1)
print(item1.calculateTotal())
item2.applyDiscount(0.2)
print(item2.calculateTotal())
print(item3.calculateTotal())



