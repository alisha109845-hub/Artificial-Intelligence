# Take input
data = input("Enter comma separated 4-digit binary numbers: ")
binaries = data.split(",")

result = []
for b in binaries:
    b = b.strip()  # remove spaces
    decimal = int(b, 2)  # convert binary to decimal
    if decimal % 5 == 0:
        result.append(b)

print(",".join(result))