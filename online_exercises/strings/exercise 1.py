'''
“Given a string s consisting of one or more words separated by spaces,
write a Python program to check whether every word in the string starts with a capital (uppercase) letter.
Return True if all words begin with a capital letter, otherwise return False.”

Example:
Input: "Hello World From Python" → Output: True
Input: "Hello world" → Output: False
'''
s = "Hello World From Python"

all_capital = True   # assume true unless proven otherwise

for word in s.split():
    if not word[0].isupper():
        all_capital = False
        break

print(all_capital)
