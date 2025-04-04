class CardItem:
    
    discountRate = 0.2
    itemCount = 0

    @classmethod
    def displayİtemCount(cls):
        return f"{cls.itemCount} tane ürün oluşturuldu."
    
    @classmethod
    def createItem(cls, data_str):
        name, price, quantity = data_str.split(",")
        return cls(name, price, quantity)
   
    def __init__(self, name, price, quantity):
  
        self.name = name
        self.price = price
        self.quantity = quantity
        CardItem.itemCount += 1

    def calculateTotal(self):
        total = self.price * self.quantity
        return total
    
    def applyDiscount(self):
        self.price = self.price * (1-CardItem.discountRate)

print(CardItem.displayİtemCount())
item1 = CardItem("Telefon", 50000, 2)
item2 = CardItem("Bilgisayar", 70000, 1)
item3 = CardItem("kitap", 500, 2)
CardItem.createItem("Mouse,13000,5")
print(CardItem.displayİtemCount())



