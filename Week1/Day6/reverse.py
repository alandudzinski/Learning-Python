# reverse.py - Returns the reversed version of the input

s = input("Enter a word: ")

def reverse_string(s):
    reverse = ""
    for i in range(len(s)-1, -1, -1):
        reverse += s[i]
    return reverse

reversed_s = reverse_string(s)
print(reversed_s)