# 1.conditional statements
# 2. looping
# a.if... checks if a single condition is true
# b. if... else ... executes the condition that is not true
# c. if ... elif ... else executes the conditions before it , if they are not true
#
# if statements most of the time make use of thr assignment operators ie ,<, > , <=, >=, !=

x = 5
y = 3
if x < y: #check for true situation only
    print('{} is greater than {}'.format(x,y))
    print(str(x) + " is greater than " + str(y))
elif x < 10:
    print('{} is less than {}'.format(x, 10))
else: #checks for false condions
    print('{} is not less than {}'.format(x, y))

if x > y:
    if y > 2:
        print('y is greater than 2 , but less than {}'.format(x))
    else: print('y is not greater than {} and {}'.format((2, x)))
else: print("{} is not greater than {}".format(x, y))


# looping

# while loops
count = 0
while count < 10:
    print('hello world')
    # count = count + 1
    count+= 1

num= 0
while num <= 10:
    print(num)
    num = num + 1

# breaking and continue statements
num2= 0
while num2 <= 10:
    if num2 == 5:
        print('at the middle ')
        break
    print(num2)
    num2 = num2 + 1

num3= 0
while num3 <= 10:
    num3 = num3 + 1
    if num3 == 5:
        # print(num3)
        continue # if true skip this instance
    print(num3)


# for loops
for letter in "john" :
    print(letter)

for i in range (3,10 , 2):
    print(i)
# range(starting point , ending point , increment value)
# else statement with a for loop
for i in range(10):
    print (i)
else:
    pass

# assignment: write  a program that prints the smallest and the largest number in this list
numbers = [210, 0, 34, 65, 33, 54, 54, 54, 3, 65]
mini = 0
for items in numbers:
    if items >= mini:
        print(False)
        mini += 1
    print(items)










