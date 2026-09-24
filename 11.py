print("Enter lines (press Enter on blank line to stop):")

lines = []
while True:
    line = input()
    if line == "":  # blank line to terminate
        break
    lines.append(line)

# Print all in lower case
for l in lines:
    print(l.lower())