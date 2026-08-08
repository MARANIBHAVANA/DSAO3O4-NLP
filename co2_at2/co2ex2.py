from tabulate import tabulate

words = ["disagree", "agreement", "agreeable"]

def analyze_word(word):

    if word == "disagree":
        return [
            word,
            "dis-",
            "agree",
            "None",
            "Derivational",
            "dis- expresses opposition or negation",
            "agree"
        ]

    elif word == "agreement":
        return [
            word,
            "None",
            "agree",
            "-ment",
            "Derivational",
            "-ment changes the verb into a noun denoting a result or state",
            "agree"
        ]

    elif word == "agreeable":
        return [
            word,
            "None",
            "agree",
            "-able",
            "Derivational",
            "-able forms an adjective meaning pleasing or acceptable",
            "agree"
        ]

results = [analyze_word(word) for word in words]

headers = [
    "Original Word",
    "Prefix",
    "Root",
    "Suffix",
    "Transformation Type",
    "Semantic Interpretation",
    "Normalized Base"
]

print("\nMORPHOLOGICAL PARSER REPORT\n")
print(tabulate(results, headers=headers, tablefmt="grid"))