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
#
# for i in my_list:
#     if i not in new_list:
#         new_list.append(i)
#         new_tuple = new_tuple + (i,)
#
# print(new_list)
# print(new_tuple)

# 3. Write a program which will find all the numbers which are divisible by 7 but are not a multiple of 5 between 1000
# and 1500 (both included).  The numbers obtained should be in a comma-sparated sequence on a single line.

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
