score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("A - Excellent work!")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")