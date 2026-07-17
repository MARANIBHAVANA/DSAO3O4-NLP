import re

resume = """
Name: Rahul Sharma
Email: rahul@gmail.com
Phone: 9876543210
Skills: Python, SQL, Machine Learning
Experience: 3 years
"""

# Extract Name
name = re.search(r"Name:\s*(.*)", resume)

# Extract Email
email = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", resume)

# Extract Phone
phone = re.search(r"\b[6-9]\d{9}\b", resume)

# Extract Experience
experience = re.search(r"(\d+)\s+years", resume, re.IGNORECASE)

# Detect Skills
skills = ["Python", "Java", "SQL", "Machine Learning", "NLP"]
found_skills = []

for skill in skills:
    if re.search(skill, resume, re.IGNORECASE):
        found_skills.append(skill)

print("\n========== RESUME SUMMARY ==========")
print("Candidate Name :", name.group(1))
print("Email          :", email.group())
print("Mobile         :", phone.group())
print("Skills         :", ", ".join(found_skills))
print("Experience     :", experience.group(1), "Years")

if "Python" in found_skills and int(experience.group(1)) >= 2:
    print("\nStatus : Eligible for Shortlisting")
else:
    print("\nStatus : Not Eligible")