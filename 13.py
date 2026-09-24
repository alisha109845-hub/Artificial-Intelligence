s = input("Enter a string: ")

letters = 0
digits = 0

for char in s:
    if char.isalpha():  # check if letter
        letters += 1
    elif char.isdigit():  # check if digit
        digits += 1

print(f"Letters {letters}")
print(f"Digits {digits}")