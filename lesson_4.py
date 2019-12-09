# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets,and they have keys and values.
# a dict is made up of key and a value
john = {
    "height": 5.7,
    "country": "kenya",
    "language": ['python', 'java']

}

print(type(john))
print(john)
# height is the key and the 5.7 is the value

# accessing keys and values
# syntax : accessing a value
# dictvariale []
# john['height']
print(john['height'])
print(john['language'])

# dictname.get(key)

print(john.get('country'))

# changing a dictionary value

# syntax : dictname[key] = "new value"
john['country'] = 'Egypt'
print(john)

# looping through a dict
for data in john:
    print(data)

for data in john:
    print( john[data])

for data in john:
    print(data + ":" + str(john[data]))

key_list = []
value_list = []

for data in john:
    key_list.append(data)
    value_list.append(john[data])

print (key_list)
print (value_list)

# helper method

# looping through keys

for data in john :
    print (data)

# looping thru a value
print("printing keys and values")
for val in john.values():
    print(val)

for my_key, my_value in john.items():
    print(" _" + my_key + " _" + str (my_value))

# adding keys and values to an existing dict

# syntax : dictnmae[newkey] = new value

john['status'] = 'complicated'
john['occupation'] = 'python engineer'
print (john)

# assignment
# remove keys and values in a dict
# deleting a dict
# clearing a dict
# copying a dict

profile =  (("john", "male" , 1999))
print(profile[0])

shoppinglist = list()
john2 = dict()
profile2= tuple()


# sets are unordered and unindexed

# SETS
# are enclosed in {}
# Note: Sets are unordered, so you cannot be sure in which order the items will appear.
# You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set,
# by using the in keyword.
fruits = {"apple", "banana", "cherry"}

for fruit in fruits:
    print(fruit)

# adding
fruits.add('mango')
fruits.add('lemon')

for fruit in fruits:
    print(fruit)

# adding multiple items
fruits.update(['berry', 'avocado'])
print (fruits)