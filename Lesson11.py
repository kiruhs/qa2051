# Z
from wx.lib.masked import value

#***
# *
#***
n = 4
# def zed(l):
#     print("* "*l)
#
#     for i in range(l-2):
#         print(' '*(2*(l-2-i))+'*')
#     print("* " * l)

# def zed2(l):
#     for i in range(l):
#         if i == 0 or i == l - 1:
#             print(l * '* ')
#         else:
#             print(' ' * 2 * (l -i -1)+'*')
#
# zed2(n)

# zed(n)

# dct = {'a': 1, 'b': {'c': {'d': {'e':{}}}}}
# dct = {}
# def dd(d):
#     if type(d) != dict:
#         return 0
#     if len(d.keys()) == 0:
#         return 1
#     k1, v1 = d.popitem() # we change the source dictionary here
#     return max(dd(v1) + 1, dd(d))
# dct = {'a': 1, 'b': {'c': {'d': {'e':{}}}}}
#
# def depth(d):
#     if not isinstance(d, dict):
#         return 0
#     if not d:
#         return 1
#     return max(depth(v) + 1 for v in d.values())
# print(depth(dct))
# print(dct)

# 1
# {'c': {'d': {'e':{}}}}
# {'d': {'e':{}}}
# {'e':{}}
# {}

# 0
# 2
# 3
# 4 + 1

# Merge two files into third one

# try:
#     with open("merged.txt", 'w') as outfile:
#         for file in ["file1.txt", "file.txt"]:
#             with open(file) as infile:
#                 outfile.write(infile.read())
#                 outfile.write("\n")
#         print(f"Files merged into {outfile.name}")
# except FileNotFoundError as e:
#     print(e)

# import random
# import time
# random.seed(124)
# print(random.randint(1, 100))

# print(int(str(time.time())[-2:]))

# import math
# num = 10_000_000
# def func(n):
#     res = []
#     cnt = 0
#     while cnt < n:
#         res.append(math.sqrt(cnt))
#         cnt += 1
#         yield res
#
# number = func(num)
# # print(number)
# for i in range(6400):
#     next(number)
# # [6345277])
# print(next(number)[6400])
# print(number.__sizeof__())

# def gen():
#     print("Start of the program...")
#     while True:
#         # return 1
#         print("Before")
#         yield 1
#         print("Between")
#         yield 2
#         print("After")
        # return 3
# g = gen()
# print(g)
# print(g)
# try:
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     # print(next(g))
#     # print(next(g))
#     # print(next(g))
# except StopIteration as e:
#     print(e)

# def gen(n):
#     while True:
#         print("First")
#         yield n
#         print("Second")
#         yield n
#
# g1 = gen(5)
# g2 = gen(10)
#
# print(next(g1))
# print(next(g2))
# print(next(g2))
# print(next(g2))
# print(next(g1))

# def gen(n):
#     while n > 0:
#         print("Before")
#         value = yield n
#         n -= 1
#         print("Got: ", value)
#         print("After")
#         return value
# g = gen(55)
# print(g.send(None))
# print(next(g))
# try:
#     print(g.send(55))
#     print(next(g))
#     print(next(g))
#     print(g.send(55))
# except StopIteration as e:
#     print(e.value)

# print(next(g))

num = 300

# def fibo():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# fib = fibo()
# print(fib.__sizeof__())
# for _ in range(num):
#     print(next(fib), end=" ")

class Point:
    color = 'red'
    circle = 2

a = Point()
b = Point()
# print(b.circle)
#
# print(a.__dict__)
# a.color = 'green'
# print(a.__dict__)
# print(b.__dict__)
# del a.color
# print(a.color)
# del a.color

a.coord = (5,10)
print(a.coord)
# print(b.coord) object b doesn't have such attribute
# print(Point.coord) class Point doesn't have such attribute as well

