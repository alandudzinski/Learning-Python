# valid_palindrome.py - Given a string, determine if it reads the same backward as forward, ignoring cases and non-alphanumeric characters

# Example
s = "Pizzip"

def is_palindrome(word: str) -> bool:

    # cleaned_word = ""
    # for c in word:
    #     if str.isalnum(c):
    #         cleaned_word += c
    word = "".join(c.lower() for c in word if c.isalnum())

    half_len = int(len(word) / 2)
    for i in range(0, half_len):
        if word[i] != word[-i-1]:
            return False
    return True


result = is_palindrome(s)

if result:
    print("palindrome ✅")
else:
    print("palindrome ❌")