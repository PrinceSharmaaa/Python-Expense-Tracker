
def expense_tracker():
    total = 0.0

    print("=" * 35)
    print("        EXPENSE TRACKER")
    print("=" * 35)

    while True:
        try:
            expense = float(input("\nEnter expense amount: ₹"))

            if expense < 0:
                print("Expense cannot be negative.")
                continue

            total += expense

            print("Expenses added Successfully.")
            print(f"Current total: ₹{total:.2f}")

        except ValueError:
            print("Please enter a valid number.")
            continue

        choice = input("\nAdd another expense? (yes/no): ").lower()

        while choice not in ("yes", "no"):
            print("Please enter 'yes' or 'no'.")
            choice = input("Add another expense? (yes/no): ").lower()

        if choice == "no":
            break

    print("\n" + "*" * 35)
    print("            SUMMARY")
    print("*" * 35)
    print(f"    Total Spent: ₹{total:.2f}")
    print("*" * 35)


if __name__ == "__main__":
    expense_tracker()
