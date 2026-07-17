import re

products = [
    "Laptop",
    "Laptop Bag",
    "Gaming Laptop",
    "Wireless Mouse",
    "Mouse",
    "Keyboard",
    "Phone Cover",
    "Smart Phone",
    "Bluetooth Speaker",
    "Smart Watch"
]

keyword = input("Enter product keyword: ")

# Exact Search
exact = [p for p in products if re.fullmatch(keyword, p, re.IGNORECASE)]

# Prefix Search
prefix = [p for p in products if re.match(keyword, p, re.IGNORECASE)]

# Suffix Search
suffix = [p for p in products if re.search(keyword + r"$", p, re.IGNORECASE)]

# Partial Search
partial = [p for p in products if re.search(keyword, p, re.IGNORECASE)]

print("\n========== SEARCH RESULTS ==========")

print("\nExact Search")
print(exact if exact else "No Match Found")

print("\nPrefix Search")
print(prefix if prefix else "No Match Found")

print("\nSuffix Search")
print(suffix if suffix else "No Match Found")

print("\nPartial Search")
print(partial if partial else "No Match Found")

print("\nCase-Insensitive Search")
print(partial if partial else "No Match Found")

print("\n========== REPORT ==========")
print("Exact Matches   :", len(exact))
print("Prefix Matches  :", len(prefix))
print("Suffix Matches  :", len(suffix))
print("Partial Matches :", len(partial))