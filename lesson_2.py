# operator: used to perform operations to variables and values
# 1.Arithmetic
# 2.Assignment
# 3.comparison
# 4.Logical

# addition
x = 23
y = 32
print ("addition of {} {} is {} " .format(x, y, x + y))
print ("subtraction of {} {} is {} " .format(x, y, x - y))
print ("multiplication of {} {} is {} " .format(x, y, x * y))
print ("division of {} {} is {} " .format(x, y, x / y))
print ("exponential  of {} raised to {} is {} " .format(3, 2, 3 ** 2))
print ("modulus of {} {} is {} " .format(3, 2, 3 % 2))

# assignment
PIE = 3.142
radius = 7

print(PIE * radius)

# 2.assignment : used to assign a value to a variale
# 1. =
name = "john"
# 2. +=
x = 5
x = x + 6
x+= 6

# comparison operators
# 1. == equal sign
# 2. != not equal to
# 3. > , < , >= , <=

# the result of a comparison is always a boolean


# LOGICAL OPERATORS : used to combine conditional operations
# 1. And
# 2. Or
# 3. Not
# the return of the logical operators is a boolean

x = 3
y = 2

print(x > y and x < 10)
# and : returns True if both conditions are True

print(x > y or x < 10)
# or : returns True if one conditions is True

print(not(x > y and x < 10))
# not : returns False if a conditions is True
# not : returns True if a conditions is False

