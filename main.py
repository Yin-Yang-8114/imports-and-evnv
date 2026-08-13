from datetime import date

expenses = [{"date": "2026-08-10", "title": "Notebook", "category": "school", "amount": 24.90},{"date": "2026-08-11", "title": "Coffee", "category": "food", "amount": 12.00},]




def calculate_total(expenses):
    total = 0.0
    for item in expenses:
        total += item["amount"]
    return total


def show_expenses(expenses):
    print("\n--- Expense List ---")
    for item in expenses:
        print(f"{item['date']} | {item['title']} | {item['category']} | {item['amount']:.2f}")

    total = calculate_total(expenses)
    print(f"Total: {total:.2f} ILS\n")


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