# Finite-State Machine for Morphological Parsing
# Generates plural forms of English nouns

def pluralize(noun):
    # State 1: Words ending with s, x, z, ch, sh
    if noun.endswith(("s", "x", "z", "ch", "sh")):
        return noun + "es"

    # State 2: Words ending with consonant + y
    elif noun.endswith("y") and len(noun) > 1 and noun[-2].lower() not in "aeiou":
        return noun[:-1] + "ies"

    # State 3: Default rule
    else:
        return noun + "s"


print("Finite-State Machine for Morphological Parsing")
print("-----------------------------------------------")

while True:
    word = input("\nEnter a singular noun (or type 'exit' to quit): ")

    if word.lower() == "exit":
        print("Program Ended.")
        break

    plural = pluralize(word)

    print("Singular Noun :", word)
    print("Plural Noun   :", plural)