from tabulate import tabulate

words = ["activate", "activation", "reactivation"]

def analyze_word(word):

    if word == "activate":
        return [
            word,
            "None",
            "activ",
            "-ate",
            "Root → activate",
            "Root/derivational verb formation",
            "activate"
        ]

    elif word == "activation":
        return [
            word,
            "None",
            "activ",
            "-ation",
            "activate → activation",
            "Verb → noun; -ation denotes an action or process",
            "activate"
        ]

    elif word == "reactivation":
        return [
            word,
            "re-",
            "activ",
            "-ation",
            "activate → reactivate → reactivation",
            "re- means again; -ation converts the verb into a noun",
            "activate"
        ]

results = [analyze_word(word) for word in words]

headers = [
    "Original Word",
    "Prefix",
    "Root",
    "Suffix",
    "Derivational Sequence",
    "Meaning / Word-Class Effect",
    "Normalized Base"
]

print("\nMORPHOLOGICAL PARSING AND NORMALIZATION REPORT\n")
print(tabulate(results, headers=headers, tablefmt="grid"))