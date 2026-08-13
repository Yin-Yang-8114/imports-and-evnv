from datetime import date
from rich.console import Console
from rich.table import Table

console = Console()

expenses = [{"date": "2026-08-10", "title": "Notebook", "category": "school", "amount": 24.90},{"date": "2026-08-11", "title": "Coffee", "category": "food", "amount": 12.00},]


def calculate_total(expenses):
    total = 0.0
    for item in expenses:
        total += item["amount"]
    return total


def show_expenses(expenses):
    table = Table(title="Expense Tracker")
    table.add_column("Date")
    table.add_column("Title")
    table.add_column("Category")
    table.add_column("Amount", justify="right")

    for item in expenses:
        table.add_row(item["date"],item["title"],item["category"],f"{item['amount']:.2f}")

    console.print(table)

    total = calculate_total(expenses)
    console.print(f"Total: {total:.2f} ILS\n")


def add_expense(expenses, title, amount, category):
    new_item = {
        "date": date.today().isoformat(),
        "title": title,
        "amount": amount,
        "category": category
    }
    expenses.append(new_item)


def ask_for_expense(expenses):
    title = input("Expense title: ")
    amount = float(input("Amount: "))
    category = input("Category: ")
    add_expense(expenses, title, amount, category)


def main():
    show_expenses(expenses)

    choice = input("Would you like to add an expense? (y/n): ")
    if choice.lower() == 'y':
        ask_for_expense(expenses)
        show_expenses(expenses)


main()