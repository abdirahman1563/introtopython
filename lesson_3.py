shoppingList=['toothpaste', 'cake', 'pen']
item0=shoppingList[0]

# list slicing
print(shoppingList[1:2])
print(type(shoppingList))

# chaging item in a list

shoppingList[0]= 'book'
print(shoppingList)

# list length

print(len(shoppingList))

# list method

# apend: adds an item to the end of the list

shoppingList.append('toothpaste')
print(shoppingList)

# insert()......adds an item where exactly u want it eg at index 2

shoppingList.insert(2,'milk')
print (shoppingList)

# pop().... removes the last item on the list

shoppingList.pop()
print (shoppingList)

# del.... deletes the whole list

todo=['eat', 'code', 'sleep','repeat']
print(todo)
# del (todo)

print (todo)

# checking if an item is present in your list

if 'cake' in shoppingList:
    print('cake is present')

else:
    print ( 'cake is absent')
#
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# tuples

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print('banana' in thistuple)


thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

print(type(thistuple))

# Note: The search will start at index 2 (included) and end at index 5 (not included).

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into
# a tuple.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    # for marks in student score
  print(x)

# Check if Item Exists

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Tuple Length
# To determine how many items a tuple has, use the len() method:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple", "banana", "cherry")

# To create a tuple with only one item, you have add a comma after the item, unless Python will not
# recognize the variable as a tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# SETS
# are enclosed in {}
# Note: Sets are unordered, so you cannot be sure in which order the items will appear.
# You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set,
# by using the in keyword.
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

# Once a set is created, you cannot change its items, but you can add new items.

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# Add multiple items to a set, using the update() method:

thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)

# To remove an item in a set, use the remove(), or the discard() method.
