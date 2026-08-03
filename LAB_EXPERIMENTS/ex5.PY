import nltk
from nltk.stem import PorterStemmer

# Create Porter Stemmer object
ps = PorterStemmer()

# Input words
words = input("Enter words separated by spaces: ").split()

print("\nPorter Stemmer Output")
print("------------------------------")
print("Original Word\tStemmed Word")

for word in words:
    print(f"{word}\t\t{ps.stem(word)}")