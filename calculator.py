import os
def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        try:
            return num1 / num2
        except ZeroDivisionError:
            print("Cannot divide by zero!")
            return None

    else:
        print("INVALID OPERATOR SELECTED!")
        return None


while True:
    print("\n===== CALCULATOR =====")
    print("1. Calculate")
    print("2. Clear")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Calculate selected")
        print("\n--- Calculator ---")

        num1 = input("Enter your first number: ")
        operator = input("Enter your operator (+, -, *, /): ")
        num2 = input("Enter your second number: ")

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("INVALID INPUT! Please enter valid numbers.")
            continue

        answer = calculate(num1, operator, num2)

        if answer is not None:
            print(num1, operator, num2, "=", answer)

    elif choice == "2":
          os.syst1em("cls" if os.name == "nt" else "clear")

    elif choice == "3":
        print("Calculator is closing...")
        break

    else:
        print("Invalid choice!")