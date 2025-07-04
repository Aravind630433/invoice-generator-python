InvoicePro – Console Invoice Generator 🧾

InvoicePro is a simple command-line invoice generator designed for small stores.  
It allows store owners to manage inventory, create invoices for customers, calculate taxes, and generate printable receipts — all from the terminal.

---

## 🚀 Features

- 📦 Product Inventory Management (Add, List)
- 🧾 Create Invoices with multiple items
- 💰 Automatic subtotal, tax (10%), and total calculation
- 🧃 Saves invoice to text file (under `invoices/`)
- 💾 Persistent inventory using JSON (`data/products.json`)

---

## 📂 Folder Structure

invoicepro/
├── main.py # Entry point
├── product.py # Product model
├── invoice_item.py # Each item in invoice
├── invoice.py # Invoice logic
├── inventory_manager.py # Load, save, update inventory
├── data/
│ └── products.json # Stores product info
└── invoices/
└── ... # Saved invoices


---

## 🛠 How to Run

1. Open terminal in the project directory.
2. Make sure you have Python installed.
3. Run:
```bash
python main.py

📋 Usage Example

    Add products like:

        ID: P001

        Name: Pen

        Price: 10

        Stock: 100

    Create invoice:

        Customer name: Aravind

        Select products

        Enter quantity

    Invoice will be printed and saved as:

invoices/Aravind.txt

📦 Requirements

No third-party packages are required. Works with standard Python 3.x.
👨‍💻 Author

    Developed by: Sunkenapally Aravind

    GitHub: Aravind630433
