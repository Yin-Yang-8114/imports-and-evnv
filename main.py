from datetime import date
import questionary
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
    table.add_column("Date", style="cyan")
    table.add_column("Title", style="magenta")
    table.add_column("Category", style="green")
    table.add_column("Amount", justify="right", style="bold yellow")
    for item in expenses:table.add_row(item["date"],item["title"],item["category"],f"{item['amount']:.2f}")
    console.print(table)
    total = calculate_total(expenses)
    console.print(f"[bold green]Total: {total:.2f} ILS[/bold green]\n")

def add_expense(expenses, title, amount, category):
    new_item = {"date": date.today().isoformat(),"title": title,"amount": amount,"category": category}
    expenses.append(new_item)


def is_valid_number(text):
    try:
        val = float(text)
        if val <= 0:
            return "Please enter a number greater than 0"
        return True
    except ValueError:
        return "Please enter a valid number"


def ask_for_expense(expenses):
    title = questionary.text("Expense title:").ask()
    amount_str = questionary.text("Amount:", validate=is_valid_number).ask()
    amount = float(amount_str)
    category = questionary.select("Choose category:",choices=["food", "travel", "school", "entertainment", "other"]).ask()
    add_expense(expenses, title, amount, category)

def main():
    show_expenses(expenses)
    while True:
        add_more = questionary.confirm("Would you like to add an expense?").ask()
        if add_more:
            ask_for_expense(expenses)
            show_expenses(expenses)
        else:
            break


main()