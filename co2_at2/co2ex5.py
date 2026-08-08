from tabulate import tabulate

words = ["create", "creates", "creating"]

def analyze_word(word):

    if word == "create":
        return [
            word,
            "None",
            "create",
            "Base form",
            "Inflectional",
            "Base verb",
            "create",
            "create"
        ]

    elif word == "creates":
        return [
            word,
            "create",
            "-s",
            "Third-person singular present",
            "Inflectional",
            "Present tense, third-person singular",
            "create",
            "create"
        ]

    elif word == "creating":
        return [
            word,
            "creat",
            "-ing",
            "Present participle",
            "Inflectional",
            "Progressive/present participle form",
            "create",
            "create"
        ]

results = [analyze_word(word) for word in words]

headers = [
    "Original Word",
    "Root",
    "Suffix",
    "Grammatical Category",
    "Morphological Type",
    "Grammatical Feature",
    "Normalized Base",
    "Final Representation"
]

print("\nINFLECTIONAL MORPHOLOGY NORMALIZATION REPORT\n")
print(tabulate(results, headers=headers, tablefmt="grid"))