# Sample series of numbers
#numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
n=1
m=9
even_count = 0
odd_count = 0

for num in range(n,m+1):
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number Of even numbers :", even_count)
print("Number Of odd numbers :", odd_count)