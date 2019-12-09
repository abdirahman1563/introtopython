class MyClass:
    x = 'john' # attribute
    y = 12
    theList = [12, 34, 45, 6, 3]
# object creation

c1 = MyClass()
# c1 = object/instance of MyClass blueprint/class
print(c1.x)
print(c1.y)
print(c1.theList)

# second instance in same class
c2 = MyClass()
print(c2.x)
print(c2.y)
print(c2.theList)

class Person:
    def __init__(self ,name, age , country):
        self.thename = name # assigns the class "thename" attribute

        self.theage = age  # assigns the class "thename" attribute
        self.country = country


    def getter (self):
        print('hello world')


# creating objects
p1 = Person('john' , 34 ,'tanzania')
p2 = Person('mary' , 14 ,'kenya')

print(p1.theage)
print(p2.thename, p2.country, str(p2.theage))

p1.getter()
p2.getter()

# custom made function that prints what you want as the output

class Animal:
    def __init__(self, nature, prey, gender, name, feeding):
        self.thenature = nature
        self.theprey = prey
        self.thegender = gender
        self.thename = name
        self.thefeeding = feeding

    def getDetails(self):
        print(self.thenature)
        print(self.theprey)
        print(self.thegender)
        print(self.thename)
        print(self.thefeeding)

a1 = Animal("wild", "chicken", "male", "mongoose","carnivorous")
a1.getDetails()

a2 = Animal("domestic", "grass", "female", "goat","herbivorous")
a2.getDetails()

# create a class that has the following:
#     name = continents
#  attribute: size, number_of_countries,population,


