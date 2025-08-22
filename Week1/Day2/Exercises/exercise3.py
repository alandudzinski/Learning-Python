num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Invalid operator.")