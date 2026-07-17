import re

print("===== UNIVERSITY REGISTRATION SYSTEM =====")

register = input("Enter Register Number: ")
email = input("Enter Institutional Email: ")
course = input("Enter Course Code: ")
semester = input("Enter Semester (Example: Semester 5): ")
mobile = input("Enter Mobile Number: ")

valid = True

# Register Number
if re.fullmatch(r"\d{2}[A-Z]{2}\d{3}", register):
    print("Register Number : Valid")
else:
    print("Register Number : Invalid")
    valid = False

# Email
if re.fullmatch(r"[A-Za-z0-9._%+-]+@college\.edu", email):
    print("Email           : Valid")
else:
    print("Email           : Invalid")
    valid = False

# Course Code
if re.fullmatch(r"[A-Z]{2}\d{3}", course):
    print("Course Code     : Valid")
else:
    print("Course Code     : Invalid")
    valid = False

# Semester
if re.fullmatch(r"Semester\s[1-8]", semester):
    print("Semester        : Valid")
else:
    print("Semester        : Invalid")
    valid = False

# Mobile Number
if re.fullmatch(r"[6-9]\d{9}", mobile):
    print("Mobile Number   : Valid")
else:
    print("Mobile Number   : Invalid")
    valid = False

print("\n========== FINAL REPORT ==========")

if valid:
    print("Registration Successful")
else:
    print("Registration Failed")