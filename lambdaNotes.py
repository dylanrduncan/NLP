remainder = lambda num: num % 2

print(remainder(5))

# this is the same as
# def remainder(num);
#   return num % 2

product = lambda x, y: x * y

print(product(2, 3))

# lambda functions are useful when you need a function for a short period of time
# Commonly for when you want to pass a function as an argument to higher-order functions, that is,


def testfunc(num):
    return lambda x: x * num


result1 = testfunc(10)
result2 = testfunc(100)
print(result1(9))
print(result2(9))
# Function takes one argument, and the argument is to be multiplied by a number that is unknown.


# The filter function takes a lambda function together witha  list as arguments.
# filter(object, iterable)
# The object here should be a lambda function which returns a boolean value.
# The object will be called for every tiem in the iterable

numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

filtered_list = list(filter(lambda num: (num > 7), numbers_list))

print(filtered_list)

# python program to demonstrate working
# of a map
# map() function returns a map object(which is an iterator) of the result
# applying the given function to each item ofa  given iterable (list,

# Return the doulbe of n:
def addition(n):
    return n + n


# we double all numbers using regular fucntion
numbers = [1, 2, 3, 4]
result = map(addition, numbers)
print(list(result))
# using function

numbers = [1, 2, 3, 4]
result = list(map(lambda x: x + x, numbers))
print(result)
# using lambda

numbers = [1, 2, 3, 4]
numbers2 = [5, 6, 7, 8]
result = list(map(lambda x, y: x + y, numbers, numbers2))
print(result)
# 2 variables

# lambda can have up to 3 variables within it
