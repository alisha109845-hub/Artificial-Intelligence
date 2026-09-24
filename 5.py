# Ask user for a word
word = input("Enter a word: ")

# Reverse using slicing [::-1]
reversed_word = word[::-1]

print("Reversed word:", reversed_word)

#[::-1] means start from the end and go backwards.
# First : means whole word
# Second : means default step
# -1 means go backwards