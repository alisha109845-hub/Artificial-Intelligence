#objects and classes
class MyClass:x=5
p1=MyClass()
print (p1.x)

#_init_ function
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p2=Person("John",36)
print(p2.name)
print(p2.age)


#object methods
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello my name is "+self.name)
p3=Person("John",36)
p3.myfunc()

 
