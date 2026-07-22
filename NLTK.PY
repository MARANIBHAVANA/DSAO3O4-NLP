import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download required resources
nltk.download('punkt')
nltk.download('punkt_tab')   # <-- Add this line
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')   # <-- Add this line

text = input("Enter a sentence: ")

words = word_tokenize(text)
tags = pos_tag(words)

print("\nMorphological Analysis")
print("----------------------------")

for word, tag in tags:
    print(f"{word:<15} {tag}")