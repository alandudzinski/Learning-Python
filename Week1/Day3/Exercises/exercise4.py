# exercise3.py - A function that uses a loop to add numbers from 1 through n

def sum_to_n(n):
    sum = 0
    if n > 0:
        for i in range(1, n + 1):
            sum += i
    elif n < 0:
        for i in range(n, -1):
            sum += i
    return sum


result = sum_to_n(-3)
print(result)