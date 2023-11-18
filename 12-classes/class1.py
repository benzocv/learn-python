class MyClass:
    x = 5

# object of the class
p1 = MyClass()
print(p1.x)


#The __init__() Function
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    

p1 = Person("John", 36)
print (p1.name)
print (p1.age)



# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.
# Let us create a method in the Person class:
# Insert a function that prints a greeting, and execute it on the p1 object:
#
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self): # note the self parameter
        print("Hello my name is " + self.name + " and I am " + str(self.age) + " years old.")

p1 = Person("John", 36)
p1.myfunc()



# Modify Object Properties
# You can modify properties on objects like this:
# Set the age of p1 to 40:
#
p1.age = 40
p1.myfunc()


# Delete Object Properties
# You can delete properties on objects by using the del keyword:
# Delete the age property from the p1 object:
#
del p1.age
# p1.myfunc() # this will throw an error


# Delete Objects
# You can delete objects by using the del keyword:
# Delete the p1 object:
#
del p1

# print(p1) # this will throw an error because the object is deleted
