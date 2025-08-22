def print_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

num_str = input("Enter a number: ").strip()
if num_str.isdigit():
    num = int(num_str)
    print_table(num)
else:
    print("Please enter an integer.")
