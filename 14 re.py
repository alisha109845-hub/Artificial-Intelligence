import re

password = input("Enter password: ")

errors = []

if len(password) < 6 or len(password) > 16:
    errors.append("- Length must be 6 to 16 characters")

if not re.search(r"[a-z]", password):
    errors.append("- At least 1 lowercase letter [a-z] required")

if not re.search(r"[A-Z]", password):
    errors.append("- At least 1 uppercase letter [A-Z] required")

if not re.search(r"[0-9]", password):
    errors.append("- At least 1 number [0-9] required")

if not re.search(r"[$#@]", password):
    errors.append("- At least 1 special character [$#@] required")

if not errors:
    print("Valid Password")
else:
    print("Invalid Password:")
    for e in errors:
        print(e)