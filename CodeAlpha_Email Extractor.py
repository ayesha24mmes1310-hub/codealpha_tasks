# CodeAlpha Python Internship
# Task 3 - Email Extractor
# Developed by: Ayesha Iqbal
# Dictionary containing stock prices

import re
# Open the text file
file = open("sample.txt", "r")
text = file.read()
file.close()

# Find email addresses
emails = re.findall(r"\S+@\S+", text)

# Save emails in another file
output = open("emails.txt", "w")
for email in emails:
    print(email)
    output.write(email + "\n")
output.close()
print("\nEmails extracted successfully!")