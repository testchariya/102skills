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
# Python???s reduce() implements a mathematical technique commonly known as folding or reduction. You???re doing a fold or
# reduction when you reduce a list of items to a single cumulative value. Python???s reduce() operates on any iterable???not
# just lists???and performs the following steps:
#
# Apply a function (or callable) to the first two items in an iterable and generate a partial result.
# Use that partial result, together with the third item in the iterable, to generate another partial result.
# Repeat the process until the iterable is exhausted and then return a single cumulative value.
# """

# 20. Create a list of integers.  Using filter and lambda functions find the integers that are multiples
# of 3. Using map and lambda functions multiply all integers of the list by 2 and add 15.  Use the reduce function from
# functools module to simply add all integers.

# import functools
# foo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 15, 17, 18, 21]
#
# bar = list(filter(lambda x: x % 3 == 0, foo))
# print(bar)
# bar2 = list(map(lambda x: x*2+14, foo))
# print(bar2)
# bar3 = functools.reduce(lambda x, y: x + y, foo)
# print(bar3)

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

# 21. Write a program to compute 1/2 + 2/3 + 3/4 + n/n+1 with a given n input by console (n>0)


# def convergence(n):
#     sum = 0
#     for num in range (0, n+1):
#         print(f"for {num} the current sum is {sum}")
#         sum += n/(n+1)
#     print(sum)
#
#
# foo = int(input("please provide an n>0: "))
# convergence(foo)

# 22. With a given list [12,23,35,24,88,120,155,88,120,155], write a program to print this list after removing
# all duplicate values with original order reserved.

# initial_list = [12,23,35,24,88,120,155,88,120,155]
# final_list = []
#
# for num in initial_list:
#     if num not in final_list:
#         final_list.append(num)
#     else:
#         print(f"{num} is a repeat")
#
# print(final_list)

# 23. In a given sentence, find all the adverbs and their positions using the re module

# import re
# text = "Clearly, he felt she was inexcusably wrong"
# for m in re.finditer(r"\w+ly", text):
#     print('%d-%d: %s' % (m.start(), m.end(), m.group(0)))

# 24. Using the re module, find a way to remove anything between parenthesis in a given string.

# import re
# text = "Clearly, he felt she was inexcusably (wrong)"
# print(re.sub(r" ?\([^)]+\)", "", text))
# print(text)

# 25. Open a text file and find the longest word in the text file and find the length.

# with open('text.txt', 'r') as infile:
#     words = infile.read().split()
# print(words)
# max_len = len(max(words, key=len))
# max_word = [word for word in words if len(word) == max_len]
# print(f"{max_word} has length {max_len}")

# 26. Open a text file and find out how many lines are in the text file.

# with open('text.txt', 'r') as infile:
#     lines = infile.readlines()
#
# print(lines)
# print(len(lines))
# print(lines[0])
# print(lines[354])

# 27. Using the NumPy module, create an arry of floating point values, square and find aboslute values of all elements

# import numpy as np
#
# x = np.arange(-7, 8, 0.5)
# print(x)
# y = np.power(x, 3)
# print(y)
# z = np.absolute(x)
# print(z)

# 28. Use the numpy module to compute the trigonometric sine, cosine and tangent array of angles given in degrees

# import numpy as np
#
# angles = [0, 30, 35, 60, 90]
# print("sine array: ", end="")
# print(np.sin(np.array(angles)*np.pi/180))
# print("cosine array: ", end="")
# print(np.cos(np.array(angles)*np.pi/180))
# print("tangent array: ", end="")
# print(np.tan(np.array(angles)*np.pi/180))

# 29. Develop a program to multiply two matrices.  first matrix of order 3x3 and second matrix of order 3x4.

# X = [[12, 7, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# Y = [[5, 8, 1, 2],
#      [6, 7, 3, 0],
#      [4, 5, 9, 1]]
#
# result = [[0,0,0,0],
#           [0,0,0,0],
#           [0,0,0,0]]
#
# for i in range(len(X)):
#     for j in range(len(Y[0])):
#         for k in range(len(Y)):
#             result[i][j] += X[i][k] * Y[k][j]
#
# for r in result:
#     print(r)

# 30. Design a program to create a diamon pattern using the asterisk symbol by taking the side length as input
# from the user.

# length = int(input("What length do you want to draw? "))
# for x in list(range(length)) + list(reversed(range(length-1))):
#     print('{: <{w1}}{:*<{w2}}'.format('', '', w1=length-x-1, w2=x*2+1))

# 31. Develop a simple encryption and decryption program by shifting a character 2 ASCII values down for encryption
# and 2 ASCII values back up for decryption

# request = input("(1) encrypt or (2) decrypt a message? ")
# message = input("Please enter your message now: ")
# result = ""
# print(message)
#
# if request == "1":
#     for i in range(0, len(message)):
#         result = result + chr(ord(message[i]) - 2)
#     print(f"Your message is: {result}")
# elif request == "2":
#     for i in range(0, len(message)):
#         result = result + chr(ord(message[i]) + 2)
#     print(f"Your message is: {result}")
# else:
#     print("You've failed to enter a valid request.")

# 32. Develop a function to implement Binary Search
# 1. sort an array
# 2. see if midpoint is the given search item
# 3. if not, if greater, go half way up, if lesser go half way down
# 4. repeat until number found or no more bisections left to complete

## MY SOLUTION
# from math import ceil
#
#
# def search(a, num, c, loc):
#     print(f"Attempt #{c}, looking for {num} at position {loc}")
#     c += 1
#     step = len(a)/2**c
#     print(f"The number {a[loc]} is at location {loc} and the current step is {step}")
#     if a[loc] == num:
#         print(f"Success!  The {num} was found in the list, found in {c} attempts at position {loc}")
#     elif step < 0.3:
#         print(f"Failure.  We could not find the number {num}, attempted {c} tries, closest number is {a[loc]} at"
#               f" position {loc}")
#     elif num > a[loc]:
#         loc += ceil(step)
#         search(a, num, c, loc)
#     elif num < a[loc]:
#         loc -= ceil(step)
#         search(a, num, c, loc)
#
#
# def bin_search(array, num):
#     a = sorted(set(array))
#     c = 1
#     print(a)
#     print(len(a))
#     loc = int(len(a)/2) - 1
#     search(a, num, c, loc)
#
#
# li = [2, 5, 7, 9, 11, 17, 17, 4, 1, 3, 4, 6, 8, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 30]
# print(bin_search(li, 11))
# print(bin_search(li, 32))
#
# ## THEIR SOLN
# import math
# def bin_search(li, element):
#     li = sorted(set(li))
#     bottom = 0
#     top = len(li)-1
#     index = -1
#     while top >= bottom and index == -1:
#         mid = int(math.floor((top+bottom)/2.0))
#         print(f"{bottom} {mid} {top} : {li[mid]} = {element}?")
#         if li[mid] == element:
#             index = mid
#         elif li[mid]>element:
#             top = mid-1
#         else:
#             bottom = mid+1
#     return index
#
# li = [2, 5, 7, 9, 11, 17, 17, 4, 1, 3, 4, 6, 8, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26,
# 27, 28, 29, 31, 30]
# print(bin_search(li, 11))
# print(bin_search(li, 32))

# 33. Write a function to implement Linear/Sequential Search
# In computer science, a linear search or sequential search is a method for finding an element within a list. It
# sequentially checks each element of the list until a match is found or the whole list has been searched.


# def seq_search(list, num):
#     l = sorted(set(list))
#     found = False
#     for x in l:
#         print(f"checking {x}")
#         if x == num:
#             print(f"{num} found in list")
#             found = True
#             break
#
#     if found == False:
#         print(f"{num} not found in list")
#
# li = [2, 5, 7, 9, 11, 17, 17, 4, 1, 3, 4, 6, 8, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26,
#       27, 28, 29, 31, 30]
# print(seq_search(li, 11))
# print(seq_search(li, 32))

# 34. Write a function to implement Bubble Sort
# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are
# in wrong order.
# li = [31, 2, 5, 7, 9, 11, 17, 17, 4, 1, 3, 4, 6, 8, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26,
#       27, 28, 29, 31, 30, 1]
#
#
# def bubble_sort(list):
#     print(list)
#     initial_list = list[:]
#     starting_count = len(list)
#     done = False
#     while not done:
#         done = True
#         for x in range(0, len(list)-1):
#             if len(list) > x + 1:
#                 print(f"checking if {list[x]} is larger than {list[x+1]}")
#                 if list[x] > list[x+1]:
#                     print(f"switching {x} and {x+1}")
#                     temp = list[x]
#                     list[x] = list[x+1]
#                     list[x+1] = temp
#                     done = False
#                 elif list[x] == list[x+1]:
#                     print(f"removing duplicate {list[x]} at position {x}")
#                     list.remove(list[x])
#                     done = False
#     print("\n\n")
#     print(initial_list)
#     print(f"starting list had {starting_count} elements")
#     print(list)
#     print(f"ending list has {len(list)} elements")
#
#
# print(bubble_sort(li))

## BOOK SOLUTION

# def bubblesort(nlist):
#     for passnum in range(len(nlist)-1,0,-1):  #Find the largest number and move it to the end
#         for i in range(passnum):
#             if nlist[i]>nlist[i+1]:
#                 temp = nlist[i]
#                 nlist[i] = nlist[i+1]
#                 nlist[i+1] = temp
#
#
# nlist = [31, 2, 5, 7, 9, 11, 17, 17, 4, 1, 3, 4, 6, 8, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26,
#       27, 28, 29, 31, 30, 1]
# bubblesort(nlist)
# print(nlist)

# 35. Write a function to implement Selection Sort
"""
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
 from unsorted part and putting it at the beginning. The algorithm maintains two sub-arrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is
picked and moved to the sorted subarray.
"""

# nlist = [31, 2, 5, 7, 9, 11, 17, 17, 4, 1, 3, 4, 6, 8, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26,
#       27, 28, 29, 31, 30, 1]
#
# slist = []
# ulist = nlist[:]
#
# for x in range(len(ulist)):
#     smallest_number = min(ulist)
#     slist.append(smallest_number)
#     ulist.remove(smallest_number)
#
# print(nlist)
# print(ulist)
# print(slist)

##BOOK SOLUTION

# def selectionSort(nlist):
#     for fillslot in range(len(nlist)-1,0,-1):
#         maxpos=0
#         for location in range(1,fillslot+1):
#             if nlist[location]>nlist[maxpos]:  # compare num (l2r) with num in last position
#                 maxpos=location
#
#         temp=nlist[fillslot]    # put num in the fillslot position in location of largest found number
#         nlist[fillslot]=nlist[maxpos]
#         nlist[maxpos]=temp
#
# nlist = [31, 2, 5, 7, 9, 11, 17, 17, 4, 1, 3, 4, 6, 8, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26,
#       27, 28, 29, 31, 30, 1]
# selectionSort(nlist)
# print(nlist)

# 36. Develop a function to implement Insertion Sort

"""
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands.
 The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed 
 at the correct position in the sorted part.
Algorithm 
To sort an array of size n in ascending order: 
1: Iterate from arr[1] to arr[n] over the array. 
2: Compare the current element (key) to its predecessor. 
3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one
 position up to make space for the swapped element.
"""
## 134 steps
# nlist = [31, 2, 5, 7, 9, 11, 17, 17, 4, 1, 3, 4, 6, 8, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26,
#          27, 28, 29, 31, 30, 1]
#
# count = 0
# for index1 in range(len(nlist)):
#     count += 1
#     print(count)
#     for index2 in range(len(nlist)):
#         if nlist[index1] < nlist[index2]:
#             temp = nlist[index2]
#             nlist[index2] = nlist[index1]
#             nlist[index1] = temp
#             count += 1
#             print(count)
#
# print(nlist)

## BOOK SOLN - takes 149 steps
# nlist = [31, 2, 5, 7, 9, 11, 17, 17, 4, 1, 3, 4, 6, 8, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26,
#          27, 28, 29, 31, 30, 1]
#
# def insertionsort(nlist):
#     count = 0
#     for index in range(1, len(nlist)):
#         count += 1
#         print(count)
#         currentvalue = nlist[index]
#         position = index
#         while position > 0 and nlist[position-1] > currentvalue:
#             nlist[position] = nlist[position-1]
#             position = position - 1
#             nlist[position] = currentvalue
#             count += 1
#             print(count)
#
#
# insertionsort(nlist)
# print(nlist)

# 37. Develop a function to implement Shell Sort

"""
What is Shell Sort?
In insertion sort, we could move the elements ahead only by one position at a time. If we wish to move an element to
 a faraway position in insertion sort, a lot of movements were involved thus increasing the execution time. Shell sort overcomes this problem of insertion sort by allowing movement and swap of far-away elements as well.

This sorting technique works by sorting elements in pairs, far away from each other and subsequently reduces their gap.
 The gap is known as the interval. We can calculate this gap/interval with the help of Knuth???s formula.

Knuth???s formula
Let h be the interval having an initial value = 1
Then, h = h*3 + 1

Characteristics of Shell Sort
Comparison-based sorting technique.
Inplace sorting technique just like insertion sort.
Works very well for medium-sized datasets.
Unstable sorting technique.
"""
## 46 g/6, 67 g/5, 58 steps at g/4, 62 steps at g/3, 63 g/2, 78 g/1
# nlist = [31, 2, 5, 7, 9, 11, 17, 17, 4, 1, 3, 4, 6, 8, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26,
#          27, 28, 29, 31, 30, 1]
#
# g = len(nlist)
# i = int(g/6 + 1)
# count = 0
#
# for y in range(i,1,-1):
#     h = y
#     count += 1
#     print(count)
#     for x in range(len(nlist) - h):
#         if nlist[x] > nlist[x+h]:
#             temp = nlist[x+h]
#             nlist[x+h] = nlist[x]
#             nlist[x] = temp
#             count+= 1
#             print(count)
#
# print(nlist)

# 38. Develop a function to implement Quick Sort
"""
Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given
 array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways. 

Always pick first element as pivot.
Always pick last element as pivot (implemented below)
Pick a random element as pivot.
Pick median as pivot.
The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot,
 put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all
  greater elements (greater than x) after x. All this should be done in linear time. 
"""

# pivot = int(len(nlist) / 2)
#
# def partition(arr, piv):
#     piv_val = arr[piv]
#     left_arr = []
#     right_arr = []
#     for i in range(len(arr)):
#         for j in range(len(arr+piv)):

## BOOK SOLUTION

#
# def quicksort(data_list):
#     quicksorthlp(data_list,0,len(data_list)-1)
#
#
# def quicksorthlp(data_list,first,last):
#     if first<last:
#         splitpoint = partition(data_list,first,last)
#         quicksorthlp(data_list,first,splitpoint-1)
#         quicksorthlp(data_list,splitpoint+1,last)
#
#
# def partition(data_list,first,last):
#     pivotvalue = data_list[first]
#     leftmark=first+1
#     rightmark=last
#     done = False
#     while not done:
#         while leftmark<=rightmark and data_list[leftmark]<=pivotvalue:
#             leftmark=leftmark+1
#         while data_list[rightmark]>=pivotvalue and rightmark>=leftmark:
#             rightmark=rightmark-1
#         if rightmark<leftmark:
#             done=True
#         else:
#             temp = data_list[leftmark]
#             data_list[leftmark]=data_list[rightmark]
#             data_list[rightmark]=temp
#     temp=data_list[first]
#     data_list[first]=data_list[rightmark]
#     data_list[rightmark]=temp
#     return rightmark
#
#
# data_list = [31, 2, 5, 7, 9, 11, 17, 17, 4, 1, 3, 4, 6, 8, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26,
#          27, 28, 29, 31, 30, 1]
# quicksort(data_list)
# print(data_list)

## ONLINE SOLN

# Quick sort in Python

# function to find the partition position
# def partition(array, low, high):
#
#   # choose the rightmost element as pivot
#   pivot = array[high]
#
#   # pointer for greater element
#   i = low - 1
#
#   # traverse through all elements
#   # compare each element with pivot
#   for j in range(low, high):
#     if array[j] <= pivot:
#       # if element smaller than pivot is found
#       # swap it with the greater element pointed by i
#       i = i + 1
#
#       # swapping element at i with element at j
#       (array[i], array[j]) = (array[j], array[i])
#
#   # swap the pivot element with the greater element specified by i
#   (array[i + 1], array[high]) = (array[high], array[i + 1])
#
#   # return the position from where partition is done
#   return i + 1
#
# # function to perform quicksort
# def quickSort(array, low, high):
#   if low < high:
#
#     # find pivot element such that
#     # element smaller than pivot are on the left
#     # element greater than pivot are on the right
#     pi = partition(array, low, high)
#
#     # recursive call on the left of pivot
#     quickSort(array, low, pi - 1)
#
#     # recursive call on the right of pivot
#     quickSort(array, pi + 1, high)
#
#
# data = [31, 2, 5, 7, 9, 11, 17, 17, 4, 1, 3, 4, 6, 8, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26,
#          27, 28, 29, 31, 30, 1]
# print("Unsorted Array")
# print(data)
#
# size = len(data)
#
# quickSort(data, 0, size - 1)
#
# print('Sorted Array in Ascending Order:')
# print(data)

# def partition(array, low, high):
#     pivot = array[high]
#     i = low - 1
#     for j in range(low, high):
#         if array[j] <= pivot:
#             i = i + 1
#             (array[i], array[j]) = (array[j], array[i])  # swap positions
#     (array[i + 1], array[high]) = (array[high], array[i + 1])
#     return i + 1
#
#
# def quicksort(array, low, high):
#     if low < high:
#         pi = partition(array, low, high)
#         quicksort(array, low, pi - 1)
#         quicksort(array, pi + 1, high)
#
#
# data = [31, 2, 5, 7, 9, 11, 17, 17, 4, 1, 3, 4, 6, 8, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26,
#         27, 28, 29, 31, 30, 1]
# quicksort(data, 0, len(data) - 1)
# print('Sorted Array in Ascending Order:')
# print(data)

## MERGE SORT
"""
In computer science, merge sort (also commonly spelled as mergesort) is an efficient, general-purpose, and
 comparison-based sorting algorithm. Most implementations produce a stable sort, which means that the order of 
 equal elements is the same in the input and output. Merge sort is a divide and conquer algorithm that was invented 
 by John von Neumann in 1945.[2] A detailed description and analysis of bottom-up merge sort appeared in a report by 
 Goldstine and von Neumann as early as 1948.[3]
 
 Like QuickSort, Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves,
  calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging
   two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and 
   merges the two sorted sub-arrays into one. See the following C implementation for details.
"""

## COUNTING SORT
"""
In computer science, counting sort is an algorithm for sorting a collection of objects according to keys that are small
 positive integers; that is, it is an integer sorting algorithm. It operates by counting the number of objects that
  possess distinct key values, and applying prefix sum on those counts to determine the positions of each key value in
   the output sequence. Its running time is linear in the number of items and the difference between the maximum key
    value and the minimum key value, so it is only suitable for direct use in situations where the variation in keys is
     not significantly greater than the number of items. It is often used as a subroutine in radix sort, another
      sorting algorithm, which can handle larger keys more efficiently.
"""

# test = [1,2]
# print(dir(test))  # The dir() method tries to return a list of valid attributes of the object.
# print(dir())

print("test of macbook pro editing")
