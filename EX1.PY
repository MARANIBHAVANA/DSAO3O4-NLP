import re

text = input("Enter a sentence: ")

# Pattern to search for the word "Python"
pattern = r"Python"

# Search the pattern
result = re.search(pattern, text)

if result:
    print("\nPattern Found!")
    print("Matched Word :", result.group())
    print("Start Position :", result.start())
    print("End Position :", result.end())
else:
    print("\nPattern Not Found!")