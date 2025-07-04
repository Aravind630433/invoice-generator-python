from product import Product
from invoice_item import InvoiceItem
from invoice import Invoice
from inventory_manager import InventoryManager
import os

def save_invoice_to_file(invoice_text, customer_name):
    if not os.path.exists('invoices'):
        os.makedirs('invoices')
    filename = f"invoices/{customer_name.replace(' ', '_')}.txt"
    with open(filename, 'w') as f:
        f.write(invoice_text)
    print(f"Invoice saved to {filename}")

def main():
    inventory = InventoryManager()

    while True:
        print("\n1. Add Product\n2. View Products\n3. Create Invoice\n4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            pid = input("Product ID: ")
            name = input("Product Name: ")
            price = float(input("Price: "))
            stock = int(input("Stock: "))
            product = Product(pid, name, price, stock)
            inventory.add_product(product)

        elif choice == '2':
            inventory.list_products()

        elif choice == '3':
            customer_name = input("Customer Name: ")
            invoice = Invoice(customer_name)

            while True:
                inventory.list_products()
                pid = input("Enter Product ID to add (or 'done'): ")
                if pid.lower() == 'done':
                    break
                product = inventory.get_product(pid)
                if not product:
                    print("Invalid ID.")
                    continue
                qty = int(input("Quantity: "))
                if qty > product.stock:
                    print("Not enough stock!")
                    continue
                item = InvoiceItem(product, qty)
                invoice.add_item(item)
                product.update_stock(qty)

            inventory.save_products()
            invoice_text = invoice.print_invoice()
            print(invoice_text)
            save_invoice_to_file(invoice_text, customer_name)

        elif choice == '4':
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
