password = input("Enter password: ")

errors = []

# 1. Length check
if len(password) < 6 or len(password) > 16:
    errors.append("Length must be 6 to 16 characters")

# 2. Lowercase check
has_lower = False
for c in password:
    if 'a' <= c <= 'z':
        has_lower = True
        break
if not has_lower:
    errors.append("At least 1 lowercase [a-z] required")

# 3. Uppercase check
has_upper = False
for c in password:
    if 'A' <= c <= 'Z':
        has_upper = True
        break
if not has_upper:
    errors.append("At least 1 uppercase [A-Z] required")

# 4. Digit check
has_digit = False
for c in password:
    if '0' <= c <= '9':
        has_digit = True
        break
if not has_digit:
    errors.append("At least 1 digit [0-9] required")

# 5. Special char check
has_special = False
for c in password:
    if c in "$#@":
        has_special = True
        break
if not has_special:
    errors.append("At least 1 special character [$#@] required")

# Final result
if len(errors) == 0:
    print("Valid Password")
else:
    print("Invalid Password. Missing:")
    for e in errors:
        print("-", e)