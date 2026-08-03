import random
from collections import defaultdict

text = "I love natural language processing and I love python programming"

words = text.lower().split()

# Create bigram model
bigrams = defaultdict(list)

for i in range(len(words)-1):
    bigrams[words[i]].append(words[i+1])

print("Bigram Model:")
for key, value in bigrams.items():
    print(key, "->", value)


# Text Generation
current_word = "i"
generated_text = [current_word]

for i in range(10):
    next_words = bigrams[current_word]

    if next_words:
        current_word = random.choice(next_words)
        generated_text.append(current_word)
    else:
        break

print("\nGenerated Text:")
print(" ".join(generated_text))