# fruits = ["apple1", "kiwi", "apple", "Orangegege", "kiwi", "cherry", "banana"]

# sort_lst = sorted(lst1, reverse=True)
# print(sort_lst)
# print(lst1)

# sort_fruits = sorted(fruits, key=len, reverse=True)
# print(sort_fruits)
# print(id(fruits))
# fruits.sort(key=len)
# print(fruits)
# print(id(fruits))
# print(fruits.index("kiwi", 2,3)) # if not found the error displayed

# list comprehension - object generation

# syntax: newlist = [ element for base of element in iterable ]

# newlist = [x*x + 5 for x in range(10)]
# print(newlist)
#
# simple_for = []
# for y in range(10):
#     simple_for.append(y*y + 5)
# print(simple_for)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# new_list = [x.upper() for x in fruits]
# print(new_list)

# d_inp = input("Enter the integer numbers separated by space: ")
#
# nl = [int(x) for x in d_inp.split()]
# print(nl)

# nl = [x if x == "kiwi" else "pomegranate" for x in fruits]
#
# print(nl)

# import time
#
#
# start = time.time()
# words_classsic = []
# for i in range(2_000_000):
#     words_classsic.append(str(i))
# print(f"the time for classic for - {time.time() -start}")
#
# del words_classsic
# # print(words_classsic)
# time.sleep(2)
# start = time.time()
# words_copmr = [str(i) for i in range(2_000_000)]
# print(f"the time for list comprehension - {time.time() -start}")
# print(words_copmr)


# a = []
# for i in range(5):
#     for j in range(3):
#         a.append((i, j))
#
# A = [(i, j) for i in range(5)
#      for j in range(3)]
#
# print(a)
# print(A)

# Nested generator

# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# A = [x**2 for row in a for x in row]
#
# print(A)
#
# AA = [[x**2 for x in row] for row in a]
#
# print(AA)

# img = [[1, 2, 3], [1, 2, 8], [0, 0, 0], [2, 2, 4]]
#
# print(id(img[1]))
# # img[1] = [1, 1, 1, 1]
# img[1] = [1] * 4
# print(id(img[1]))
# img[1][:] = [300] *5 #[2, 5, 7,3, 9 , 0, 6]
#
# print(img)
# print(id(img[1]))

# join - string

# ls = ["h", "e", 4.2, "l",3, "l", True, "o"]
# st = "".join(i for i in ls if isinstance(i, str))
#
# st = "".join(i if isinstance(i, str) else str(i) for i in ls)
# print(st)

# phone = "972 - 54-375- 1512"
#
# ph = "".join(i for i in phone if i in "0123456789")
# print(ph)

# names = ['Java', 'Python', 'Go']
# delimiter = ','
# single_string = delimiter.join(names)
# print('String: ', single_string)
# spl = single_string.split(delimiter)
# print('List: ', spl)
# spl =single_string.split(delimiter, 1)
# print('List: ', spl)

# s1 = "Hello"
# s2 = "World"
# s3 = "{}<-->{}".format(s1, s2)
# print(s3)
#
# s4 = "{obj1} +*/<> {obj2}".format(obj1=s2, obj2=s1)
# print(s4)

# x = 8
# y = 10
# z = y
# y = x
# x = z

# x, y = y, x

# print(f"x={y}, y={x}")


# lst1 = [1, 2, 3, 5, 7, 84, 99]
# lst2 = [2, 4, 6, 7, 23, 58, 67, 69]
#
# lst3 = []
# i, j = 0, 0
#
# while i < len(lst1) and j < len(lst2):
#     if lst1[i] < lst2[j]:
#         lst3.append(lst1[i])
#         i += 1
#         if i >= len(lst1):
#             while j < len(lst2):
#                 lst3.append(lst2[j])
#                 j += 1
#     else:
#         lst3.append(lst2[j])
#         j += 1
#         if j >= len(lst2):
#             while i < len(lst1):
#                 lst3.append(lst1[i])
#                 i += 1
#
# print(lst1)
# print(lst2)
# print(lst3)

# lst = [56, 13, 37.3, 5, 0, 37, -1, -4, -50.4, -134, 0.2, -4, 53]
#
# for i in range(len(lst)-1):
#     for j in range(len(lst) - 1 - i):
#         if lst[j] > lst[j+1]:
#             lst[j], lst[j+1] = lst[j+1], lst[j]
#
# print(lst)

# built-in

# function


    #pass
# from stam.tmp import hello  # *

# def hello():
#     print("Hello world!")
#
# hello()
# print(dir())

def hello(name, age):
    print(f"Hello,{name}! You are {age}")

hello("Alexander", "54")