# exercise2.py - A while loop that keeps asking the user for input until they type "exit"

while True:
    word = input("Enter some input: ")
    if word.lower() == "exit":
        print("Goodbye!")
        break
    print(word)