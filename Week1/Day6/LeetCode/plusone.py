# plusone.py - Given a list of digits representing a number. Increment the number by one and return the result as a list of digits

# Example
digits = [9, 9, 9]

for i in range(len(digits)-1, -1, -1):
    if digits[i] != 9:
        digits[i] += 1
        break
    else:
        digits[i] = 0
    
    # On the left-most index
    if i == 0:
        digits.insert(0, 1)


print(digits)