# Finite State Automaton to recognize strings ending with 'ab'

def check_string(s):
    if s.endswith("ab"):
        return True
    else:
        return False

print("Finite State Automaton")
print("----------------------")

while True:
    string = input("\nEnter a string (or type 'exit' to quit): ")

    if string.lower() == "exit":
        print("Program Ended.")
        break

    if check_string(string):
        print("Accepted: The string ends with 'ab'.")
    else:
        print("Rejected: The string does not end with 'ab'.")