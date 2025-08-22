password = input("Enter a password: ")

if password.lower() == "ai123":
    print("Access granted")
elif password.startswith("ai".lower()):
    print("Almost correct, try again!")
else:
    print("Access denied")