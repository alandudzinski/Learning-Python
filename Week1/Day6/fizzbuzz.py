# fizzbuzz.py - A program that prints numbers 1–50, with extras when divisible by 3, 5, or both

for i in range(1, 51):
    print(i)

    # Divisible by both
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Divisible by three
    elif i % 3 == 0:
        print("Fizz")
    # Divisble by five
    elif i % 5 == 0:
        print("Buzz")