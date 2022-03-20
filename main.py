# 1. With a given number n, write a program to generate a dictionary that contains (i, i*i) such that is a number
# between 1 and n (both included).  and then the program should print the dictionary.

# i = int(input("Provide a number: "))
#
# dict = {}
#
# for _ in range (1, i+1):
#     dict[_] = _*_
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
# a = input("Give me a number: ")
# factorial(int(a))

# 7. Use list comprehension to square each odd number in a list.  The list is input by a sequence of
# comma-separated numbers.
#
# a = input("Give a list of comma-separated numbers: ")
# print(a)
# b = a.split(",")
# c = [2 * int(num) for num in b if int(num) % 2 == 0]
# print(c)

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

# def square(num = 20):
#     dict = {}
#     for x in range(1,num+1):
#         dict[x] = x**2
#     print(dict)
#     print(dict.values())
#     print(dict.items())
#     # for (k, v) in dict.items():
#     #     print(v)
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
#
# print("hello there")
# text = input("Please give me a sentence: ")
# upper = sum(1 for upp in text if upp.isupper())
# lower = sum(1 for low in text if low.islower())
# print(f"There are {upper} upper case and {lower} lower case letters in that sentence.")

# 13. Write a program to display the fibonacci series up to the nth term where the btg tern is given by the user

number = int(input("Provide a number to fibonacci: "))

fib = [1, 1]

for num in range(0, number+1):
    n1 = fib[-1]
    n2 = fib[-2]
    n3 = n1 + n2
    print(f"{num}: {n1} + {n2} = {n3}")
    fib.append(n3)

print(fib)
