password = input("Enter password: ")

errors = []

if len(password) < 6 or len(password) > 16:
    errors.append("- Length must be 6 to 16 characters")

if not any('a' <= c <= 'z' for c in password):
    errors.append("- At least 1 lowercase letter [a-z] required")

if not any('A' <= c <= 'Z' for c in password):
    errors.append("- At least 1 uppercase letter [A-Z] required")

if not any('0' <= c <= '9' for c in password):
    errors.append("- At least 1 number [0-9] required")

if not any(c in "$#@" for c in password):
    errors.append("- At least 1 special character [$#@] required")

if not errors:
    print("Valid Password")
else:
    print("Invalid Password:")
    for e in errors:
        print(e)