# sum.py - Take an integer input and output the sum of its digits

number = input("Enter a number: ")

sum = 0
for digit in number:
    int_digit = int(digit)
    sum += int_digit

print(f"Sum: {sum}")