from datetime import date
class Invoice:
    def __init__(self, customer_name, amount, invoice_date):
        self.customer_name = customer_name
        self.amount_due = amount
        self.invoice_date = invoice_date

def amount_due(invoices, grace_period_days=30):
    past_due_amount = 0
    for invoice in invoices:
        days_past_due = (date.today() - invoice.invoice_date).days
        if days_past_due > grace_period_days:
            past_due_amount += invoice.amount_due
    return past_due_amount

invoices = [
    Invoice("Anne", 10.00, date(2025, 6, 17)),
    Invoice("Don", 75.00, date(2020, 7, 21)),
    Invoice("Poli", 13.00, date(2029, 11, 5)),
    Invoice("Raul", 60.00, date(2021, 4, 15)),
]

result = amount_due(invoices)
print(result)
