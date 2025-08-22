# bonus.py - A program that asks for a word and prints each letter on its own line in reverse order

word = input("Input: ")
print("Output: ")

for i in range(len(word)-1, -1, -1):
    print(word[i])