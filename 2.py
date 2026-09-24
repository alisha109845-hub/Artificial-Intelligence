# formula: c/5=(f-32)/9
def celsius_to_fahrenheit(c):
    f=(c * 9/5)+32
    return f
def fahrenheit_to_celsius(f):
    c=(f - 32) * 5/9
    return c

#test as per expected output
c=60
f=45

print(f"{c} C is {celsius_to_fahrenheit(c)} in Fahrenheit")
print(f"{f} C is {round(fahrenheit_to_celsius(f))} in Celsius")