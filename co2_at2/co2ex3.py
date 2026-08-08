from tabulate import tabulate

words = ["govern", "government", "governance"]

def analyze_word(word):

    if word == "govern":
        return [
            word,
            "govern",
            "None",
            "Root/Base",
            "Level 0",
            "govern",
            "govern"
        ]

    elif word == "government":
        return [
            word,
            "govern",
            "-ment",
            "govern → government",
            "Level 1",
            "govern",
            "govern"
        ]

    elif word == "governance":
        return [
            word,
            "govern",
            "-ance",
            "govern → governance",
            "Level 1",
            "govern",
            "govern"
        ]

results = [analyze_word(word) for word in words]

headers = [
    "Original Word",
    "Root",
    "Affix",
    "Derivational Hierarchy",
    "Derivational Level",
    "Normalized Representation",
    "Final Output"
]

print("\nMORPHOLOGY-BASED NORMALIZATION REPORT\n")
print(tabulate(results, headers=headers, tablefmt="grid"))