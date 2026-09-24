# First two numbers of Fibonacci
a = 0
b = 1

print("Fibonacci series between 0 to 50:")

while a <= 50:
    print(a, end=" ")
    # Next number is sum of previous two
    c = a + b
    a = b
    b = c