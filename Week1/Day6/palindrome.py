# palindrome.py - Ask the user for a word and check if it’s a palindrome (reads the same backward)

word = input("Enter a word: ")

def is_palindrome(word: str) -> bool:
    half_len = int(len(word) / 2)
    for i in range(0, half_len):
        if word[i] != word[-i-1]:
            return False
    return True


result = is_palindrome(word)

if result:
    print("palindrome ✅")
else:
    print("palindrome ❌")