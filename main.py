# 1. With a given number n, write a program to generate a dictionary that contains (i, i*i) such that is a number
# between 1 and n (both included).  and then the program should print the dictionary.

# i = int(input("Provide a number: "))
#
# dict = {}
#
# for num in range (1, i+1):
#     dict[num] = num*num
#
# print(dict)

# 2. Write a program which accepts a sequence of comma-separated numbers from console/user and generates a list and
# a tuple which contains every number

# list = input("Provide a list of comma separated numbers: ")
#
# my_list = list.split(",")
# print(my_list)
#
# new_list = []
# new_tuple = ()
#
# for i in my_list:
#     if i not in new_list:
#         new_list.append(i)
#         new_tuple = new_tuple + (i,)
#
# print(new_list)
# print(new_tuple)

# 3. Write a program which will find all the numbers which are divisible by 7 but are not a multiple of 5 between 1000
# and 1500 (both included).  The numbers obtained should be in a comma-separated sequence on a single line.

# list3 = []
#
# for num in range(1000, 1500):
#     if num % 7 == 0:
#         # print(f"{num} is divisible by 7")
#         if num % 5 != 0:
#             # print(f"{num} is not divisible by 5")
#             list3.append(num)
#
# # print(list3)
# # print(', '.join(list3))  ## THIS DOES NOT WORK BECAUSE THE LIST IS NOT STRINGS MUST USE THE MAP FUNCTION TO CONVERT
# print(', '.join(map(str, list3)))

# 4. Define a function which can compute the sum of two numbers

# def sum(a, b):
#     return a + b
#
# a = input("Give me a number: ")
# b = input("Give me another number: ")
# print(f"The sum is: {sum(int(a), int(b))}")

# 5. Define a function that can receive two integral numbers in string form and compute their sum then print it
# in console.

# def sum(a, b):
#     return a + b
#
# a = input("Give me a number: ")
# b = input("Give me another number: ")
# print(f"The sum is: {sum(int(a), int(b))}")

# 6. Write a program which can compute the given factorial of a number.

# def factorial(a):
#     pos = 0
#     fac = 1
#     for _ in range(1, a+1):
#         pos += _
#         fac *= _
#     print(f"the postorial is: {pos} and the factorial is {fac}")
#
#
# num = input("Give me a number: ")
# factorial(int(num))

# 7. Use list comprehension to square each odd number in a list.  The list is input by a sequence of
# comma-separated numbers.

# a = input("Give a list of comma-separated numbers: ")
# # print(a)
# b = a.split(",")
# c = [int(num)**2 for num in b if int(num) % 2 != 0]
# print(f"the odd numbers of your list squared are: {c}")

# 8. Write a program to roll a dice and get a random output (1-6)

# import random
#
#
# def roll_dice():
#     print(random.randint(1, 6))
#
#
# times = int(input("How many rolls would you like? "))
# for _ in range(times):
#     roll_dice()

# 9. Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
# and the values are square of keys.  The function should just print the values only

# def square(num=20):
#     dict = {}
#     for x in range(1, num+1):
#         dict[x] = x**2
#     # print(dict)
#     # print(dict.values())
#     # print(dict.items())
#     list = []
#     for (k, v) in dict.items():
#         list.append(v)
#     # print(*list)
#     print(*list, sep=", ")
#
#
# square(10)

# 10. Define a class which has at least two methods: getstring: to get a string from a user.  printsrting: to print
# the string in upper case.  include a test function to test the class methods


# class Strings:
#     def __init__(self):
#         self.text = ""
#
#     def getstring(self):
#         self.text = input("Provide a string: ")
#
#     def printstring(self):
#         print(self.text.upper())
#
#
# first = Strings()
# first.getstring()
# first.printstring()

# 11. Define a class, which have a class parameter and have a same instance parameter


# class Person:
#     default_name = "Unknown"
#
#     def __init__(self, name=default_name):
#         self.name = name
#
#
# jon = Person("Jon")
# print(jon.name)
# bob = Person()
# print(bob.name)
# bob.name = "Bob"
# print(bob.name)

# 12. Write a program that accepts a sentence and calculates the number of upper and lower case letters

# print("hello there")
# text = input("Please give me a sentence: ")
# upper = sum(1 for upp in text if upp.isupper())
# lower = sum(1 for low in text if low.islower())
# print(f"There are {upper} upper case and {lower} lower case letters in that sentence.")

# 13. Write a program to display the fibonacci series up to the nth term where the nth term is given by the user

# number = int(input("Provide a number to fibonacci: "))
#
# fib = [1, 1]
#
# for num in range(0, number-2):
#     n1 = fib[-1]
#     n2 = fib[-2]
#     n3 = n1 + n2
#     print(f"{num+3}: {n1} + {n2} = {n3}")
#     fib.append(n3)
#
# print(fib)

# 14.Define a class named American and its subclass NewYorker

# class American:
#     pass
#
#
# class NewYorker(American):
#     pass
#
#
# anAmerican = American()
# aNewYorker = NewYorker()
#
# print(anAmerican)
# print(aNewYorker)

# 15. Define a class Circle which can be constructed by a radius.  The Circle class has a method which can
# compute the area.

# class Circle:
#     def __init__(self, rad):
#         self.radius = rad
#
#     def area(self):
#         print(f"circle of radius {self.radius} has an area of {3.14*self.radius**2}")
#
#
# entry = input("give me a radius: ")
# myCircle = Circle(float(entry))
# myCircle.area()

# 16. Write a program using generator to print the even numbers between 0 and n in comma separated form while
# n is input by console.

# num = int(input("please provide a number: "))
#
# print(f"the even numbers between 0 and {num} are:")
#
# evens = []
#
# for x in range(0,num):
#     if x % 2 == 0:
#         evens.append(x)
#
# print(*evens)
# print(*evens, sep=", ")

# 17. Write statements using assert expression to verify that every number in the list [2,4,6,8] is even

# list = [2, 4, 6, 8, 9, 10, 11]
#
# print(f"testing for odds in {list}")
# for x in list:
#     try:
#         assert x % 2 == 0, print(f"{x} is not even")
#     except AssertionError:
#         print(f"There was an Assertion Error for {x}")
#     else:
#         print(f"{x} is even")

# 18. Write a program to compress and decompress the string "Hello world! Python is great!"

# import zlib
#
# string = "Hello world! Python is great!"
# s0 = string.encode("utf-8")
# print(s0)
#
# s1 = zlib.compress(s0)
# print(s1)
#
# s2 = zlib.decompress(s1)
# print(s2)
#
# s3 = string.encode("ascii")
# print(s3)

#############################################################################################
# 3.21.2022
#############################################################################################

# 19. Define three individual functions to implement the filter, map and reduce functions.
# Experiment on them as you like.

# import functools
#
#
# def f(x):
#     return x % 2 != 0 and x % 3 != 0
#
#
# output = list(filter(f, range(2,25)))
# print(output)
# # The filter() function extracts elements from an iterable (list, tuple etc.) for which a function returns True.
#
# def cube(x):
#     return x*x*x
#
#
# output2 = list(map(cube, range(1, 11)))
# print(output2)
# # map() function returns a map object(which is an iterator) of the results after applying
# # the given function to each item of a given iterable (list, tuple etc.)
#
#
# def add(x, y):
#     return x + y
#
#
# print(functools.reduce(add, range(1, 11)))
# """
# Python’s reduce() implements a mathematical technique commonly known as folding or reduction. You’re doing a fold or
# reduction when you reduce a list of items to a single cumulative value. Python’s reduce() operates on any iterable—not
# just lists—and performs the following steps:
#
# Apply a function (or callable) to the first two items in an iterable and generate a partial result.
# Use that partial result, together with the third item in the iterable, to generate another partial result.
# Repeat the process until the iterable is exhausted and then return a single cumulative value.
# """

# 20. Create a list of integers.  Using filter and lambda functions find the integers that are multiples
# of 3. Using map and lambda functions multiply all integers of the list by 2 and add 15.  Use the reduce function from
# functools module to simply add all integers.

import functools
foo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 15, 17, 18, 21]

bar = list(filter(lambda x: x % 3 == 0, foo))
print(bar)
bar2 = list(map(lambda x: x*2+14, foo))
print(bar2)
bar3 = functools.reduce(lambda x, y: x + y, foo)
print(bar3)

"""
lis = [1, 3, 4, 10, 4]

printing summation using accumulate()
print("The summation of list using accumulate is :", end="")
print(list(itertools.accumulate(lis, lambda x, y: x+y)))
 
printing summation using reduce()
print("The summation of list using reduce is :", end="")
print(functools.reduce(lambda x, y: x+y, lis))

Output
The summation of list using accumulate is :[1, 4, 8, 18, 22]
The summation of list using reduce is :22
"""