# import timeit
#
#
# def my_sort():
#
#     lst1 = [-140, -111, -95, -65, -14, -13, -10, -6, 1, 2, 3, 5, 7, 84, 99, 112, 189, 193, 201]
#     lst2 = [-400, -281, -211, -139, -111, -103, -101, -98,  -20, -19, 2, 4, 6, 7, 23, 34, 51, 58, 67, 69, 78, 84]
#     lst3 = []
#     i, j = 0, 0
#
#     while i < len(lst1) and j < len(lst2):
#         if lst1[i] < lst2[j]:
#             lst3.append(lst1[i])
#             i += 1
#             if i >= len(lst1):
#                 while j < len(lst2):
#                     lst3.append(lst2[j])
#                     j += 1
#         else:
#             lst3.append(lst2[j])
#             j += 1
#             if j >= len(lst2):
#                 while i < len(lst1):
#                     lst3.append(lst1[i])
#                     i += 1
#     # print(lst3)
#
# def jakob_sort():
#     L1 = [-140, -111, -95, -65, -14, -13, -10, -6, 1, 2, 3, 5, 7, 84, 99, 112, 189, 193, 201]
#     L2 = [-400, -281, -211, -139, -111, -103, -101, -98,  -20, -19, 2, 4, 6, 7, 23, 34, 51, 58, 67, 69, 78, 84]
#
#     x = []
#
#     while len(L1) > 0 or len(L2) > 0:
#         if len(L1) > 0 and len(L2)>0 and L1[0]<=L2[0]:
#             x.append(L1[0])
#             L1 = L1[1:]
#
#         elif len(L2) > 0 :
#             x.append(L2[0])
#             L2 = L2[1:]
#         else:
#             x.append(L1[0])
#             L1 = L1[1:]
#     # print(x)
#
# # my_sort()
# # jakob_sort()
# def classic_sort():
#     L1 = [-140, -111, -95, -65, -14, -13, -10, -6, 1, 2, 3, 5, 7, 84, 99, 112, 189, 193, 201]
#     L2 = [-400, -281, -211, -139, -111, -103, -101, -98, -20, -19, 2, 4, 6, 7, 23, 34, 51, 58, 67, 69, 78, 84]
#
#     x = sorted(L1 + L2)
#     # print(x)
# print(f"my sort: {timeit.timeit(my_sort, number=40) :.6f} mks")
# print(f"Jakob's sort: {timeit.timeit(jakob_sort, number=40) :.6f} mks")
# print(f"classic sort: {timeit.timeit(classic_sort, number=40) :.6f} mks")
from os import lstat

# def hello():
#     print("Hello, world!")
#
# f = hello
# f()
# print(id(hello))
# print(id(f))
#
# print(hello is f)

# def hello(name):
#     print("Hello, world!")
#
# f = hello
# f("")

# def hello(name=""):
#     print("Hello,", name)
#
# f = hello
# # f("Alexander")
# f()

# def max2(x, y):
#     if x > y:
#         return x
#     return y
# #
# # print(max2(4, 7))
#
# def max3(x, y, z):
#     return max2(max2(x, y), z)
#
# print(max3(-5, 110, 45))

# def my_country(country="Israel", x=10):
#     print(f"I'm from {country}, live {x} years")
# my_country(x=10)
# my_country("USA", 3)
# my_country()

# def call_child(*kids):
#     print("My child's name is", kids)
#
# call_child("Emile", "Mary", "Jonny")


# def personal_info(*args, **kwargs):
#     return *args, kwargs
#
# y = personal_info("John", "Jack", "Hello world", surname="Connor", age=17, mother="Sarah", stam="kuku")
# print(*y)
# y = 10
# def my_fun():
#     y = 5
#     return y*4
# print(my_fun())
# print(y)

# y = 0
# print(id(y))
# def my_fun(x_copy):
#     global y
#     print(id(y))
#     y = x_copy*x_copy
#     return y
# x = 5
# print(my_fun(x))
# print(x)
# print(y)

# recursion

# factorial 6! = 1*2*3*4*5*6  = 720  n! = (n-1)! * n

# n = 100
# def fact(n):
#     fct = 1
#     for i in range(1, n+1):
#         fct *= i
#     return fct
#
# print(fact(n))
#
# def fact_rec(n):
#     if n == 1:
#         return 1
#     return fact_rec(n-1) * n
#
# print(fact_rec(n))

# fibonacci
# 1, 1, 2, 3, 5, 8, 13, 21

# num = 100
# lst = [1, 1]
# def fibo(x):
#     for i in range(2, x):
#         lst.append(lst[i-1] + lst[i-2])
#
# fibo(num)
# print(lst)
#
#
# def fibo_rec(x):
#     if x == 1 or x == 2:
#         return 1
#     return fibo_rec(x-1) + fibo_rec(x-2)

# print(fibo_rec(num))

# O(n)
# x = 5
# for i in range(100):
#     x += i
#
# print(x)
# y = 5
# for i in range(100):      # O(n^2) 2^n
#     for j in range(100):
#         y += j
# print(y)

# lambda functions - anonymous functions

# def pr(st):
#     print(st)
# pr("Hello, world!")

# x = lambda : print("Hello, world!")
# x()

# x = lambda num: num*num
# print(x(8))
# print((lambda num: num*num)(10))
#
# lst = [5, 14, "hello", (lambda x: x*x)(14)]
# print(lst)

# lst = [1, 2, 3, 6]
# def fun_ls(ls):
#     ls[2] = 7
#
# fun_ls(lst)
# print(lst)

# def get_filter(ls, fil=None):
#     return [y for y in ls if fil(y)]
#
# lst = [1, 2, 4, 34, -4, -200, 45, 9]
#
# print(get_filter(lst, lambda x: x%2 == 1))

# map

# lst = [i for i in range(1000000)]
# # for i in range(len(lst)):
# #     lst[i] = str(lst[i])
# # print(lst)
#
# s = map(str, lst)
# l = list(map(str, lst))
# print(s.__sizeof__())
# print(l.__sizeof__())

# lst1 = [2, 5, -2]
# lst2 = [3, 3, 4]
# lst3 = [0, -40, 3]
# # print(*map(pow, lst1, lst2))
#
# print(*map(lambda x, y, z: x*y*z, lst1, lst2, lst3))

# filter
# lst = [*range(500)]
# # print(lst)
# f = filter(lambda x: x%2 == 0, lst)
# l = list(f)
# print(f.__sizeof__())
# print(l.__sizeof__())

seq = "Hello world! The evening is wonderful"
print(list(filter(lambda vowels: vowels in 'aeiouy', seq)))