#calling a function
def my_function():
    print ("Hello from a function")
my_function()

#Parameters
def my_function(fname):
    print(fname+ "Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

#default parameter
def my_function(country="Norway"):print("i am from "+ country)
my_function(" Sweden")
my_function(" India")
my_function()
my_function(" Brazil")


#passing a list as parameter
def my_function(food):
    for x in food:
        print(x)
fruits=["apple","banana","cherry"]
my_function(fruits)

#return values
def my_function(x):
    return 5*x
print(my_function(3))
print(my_function(5))
print(my_function(9))

#keyword arguments
def my_function(child3, child2, child1):
    print("The youngest child is "+child3)

my_function(child1="Emil",child2="Tobias",child3="Linus")