class BookClass:
    def __init__(self, price):
        self.price=price
    
    def __add__(self, other):
        if isinstance(other, BookClass):
            return BookClass(self.price + other.price)
        return NotImplemented
    def __str__(self):
        return f"Book price: Rs{self.price}"
    
book1=BookClass(400)
book2=BookClass(300)
total=book1+book2
print(total)
