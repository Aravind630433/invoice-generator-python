import json
import os
from product import Product

class InventoryManager:
    def __init__(self, filepath='data/products.json'):
        self.filepath = filepath
        self.products = self.load_products()

    def load_products(self):
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath, 'r') as f:
            data = json.load(f)
            return [Product.from_dict(p) for p in data]

    def save_products(self):
        with open(self.filepath, 'w') as f:
            json.dump([p.to_dict() for p in self.products], f, indent=4)

    def add_product(self, product):
        self.products.append(product)
        self.save_products()

    def update_product(self, product_id, new_stock):
        for p in self.products:
            if p.id == product_id:
                p.stock = new_stock
                self.save_products()
                return True
        return False

    def get_product(self, product_id):
        for p in self.products:
            if p.id == product_id:
                return p
        return None

    def list_products(self):
        print("ID  Name       Price   Stock")
        for p in self.products:
            print(f"{p.id:<4}{p.name:<10}{p.price:<8}{p.stock}")
