operation = input("Choose an operation (add, subtract, multiply, divide): ")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

match operation:
    case "add":
        print(f"Result: {x + y}")
    case "subtract":
        print(f"Result: {x - y}")
    case "multiply":
        print(f"Result: {x * y}")
    case "divide":
        if y != 0:
            print(f"Result: {x / y}")
        else:
            print("Error: Cannot divide by zero.")
    case _:
        print("Unknown operation.")

