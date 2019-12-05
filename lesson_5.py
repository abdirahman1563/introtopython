# python function :
# 1.is a block of a code with a name
# 2.this only works when called/when in use
# 3.Helps to write repeated code

def nameOfFuncion():
    print('hello world')

nameOfFuncion() # calling a function

# naming funtion :
# 1.should start with a small letter
# 2.should start with a letter or an underscore

def greeting_1(name): # takes one argument
    print('hello world' + name)
greeting_1("john")
greeting_1('country')

def greeting_1(name , country, gender): # takes two argument
    print('my name is ' + name + ' i come from' + country + ' i am ' + gender)


greeting_1('john', 'kenya', 'male')

def greeting_3(name ="developer"):
    print ("hello " + name)
greeting_3("mary")
greeting_3()

def sum_of_two_num(number_1 , number_2):
    print (number_1 + number_2)
sum_of_two_num(3 , 5)

def sumOfTwoNum(number_1 , number_2):
    theSum = number_1 + number_2
    return theSum

ans = sumOfTwoNum (5,6)

print(ans)

# assignment: create a function that computes an area of a circle of a given radius

def area_of_circle(PIE , radius):
    area = PIE * radius
    return area
ans = area_of_circle(3.142 , 7)
print (ans)

shoppingList = ['soap', 'sugar', 'bread' , 'cooking oil', ['jam' , 'spoon'], {'name': 'john'}]
print (shoppingList[4][0])
def loopList (theList):
    for item in theList:
        print (item)
loopList(shoppingList)

print (shoppingList[4][0])
print (shoppingList[5]['name'])

