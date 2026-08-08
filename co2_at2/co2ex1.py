from tabulate import tabulate

words = ["analyzing", "analysis", "analytical"]

def analyze_word(word):
    if word == "analyzing":
        return [
            word,
            "analyz",
            "None",
            "-ing",
            "Inflectional",
            "Present participle / progressive form",
            "analyze"
        ]

    elif word == "analysis":
        return [
            word,
            "analy",
            "None",
            "-sis",
            "Derivational",
            "Noun formation related to analysis",
            "analyze"
        ]

    elif word == "analytical":
        return [
            word,
            "analy",
            "None",
            "-tical",
            "Derivational",
            "Adjective formation expressing relation to analysis",
            "analyze"
        ]

results = [analyze_word(word) for word in words]

headers = [
    "Original Word",
    "Root",
    "Prefix",
    "Suffix",
    "Type",
    "Morphological Interpretation",
    "Normalized Output"
]

print("\nMORPHOLOGICAL ANALYSIS REPORT\n")
print(tabulate(results, headers=headers, tablefmt="grid"))