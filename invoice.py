from datetime import datetime

class Invoice:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []
        self.tax = 0.1  # 10%
        self.total = 0

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        subtotal = sum(item.total_price for item in self.items)
        tax_amount = subtotal * self.tax
        self.total = subtotal + tax_amount
        return subtotal, tax_amount, self.total

    def print_invoice(self):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        lines = [
            f"INVOICE - {now}",
            f"Customer: {self.customer_name}",
            "-" * 40,
            "ID  Name       Qty   Price   Total"
        ]
        for item in self.items:
            p = item.product
            lines.append(f"{p.id:<4}{p.name:<10}{item.quantity:<6}{p.price:<8}{item.total_price:<8}")
        subtotal, tax, total = self.calculate_total()
        lines.append("-" * 40)
        lines.append(f"Subtotal: {subtotal:.2f}")
        lines.append(f"Tax (10%): {tax:.2f}")
        lines.append(f"Total: {total:.2f}")
        return "\n".join(lines)
