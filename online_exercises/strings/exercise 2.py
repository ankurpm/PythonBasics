'''
“Given a string s and a list of substrings, check if s contains any of those substrings.”

Example:
s = "python is awesome"
substrings = ["java", "thon", "code"] → should return True (because "thon" is present)
'''

s = "python is awesome"
substrings = ["java", "thon", "code", "some"]

found = False

for sub in substrings:
    if sub in s:
        found = True
        break

print(found)
