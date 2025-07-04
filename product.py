import json

class Product:
    def __init__(self, pid, name, price, stock):
        self.id = pid
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock -= quantity

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }

    @staticmethod
    def from_dict(data):
        return Product(data["id"], data["name"], data["price"], data["stock"])
