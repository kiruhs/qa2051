# 1. Write a program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.
# Original list:
# ls = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
#
# def grouping_dictionary(l):
    # results = {}
    # for k, v in l:
    #     results.setdefault(k, []).append(v)
import time

# results = {}
    # [results.setdefault(k, []).append(v) for k, v in l] not recommended

    # return results


# print(grouping_dictionary(ls))

# 2.Write a  Python program to convert a list into a nested dictionary of keys.
# ls = [1, 2, 3, 4]
# {1: {2: {3: {4: {}}}}}

# def l2d(lst):
#     # rev = lst[::-1]
#     rev = reversed(lst)
#     d = {}
#     for item in rev:
#         d = {item: d}
#     return d
#
# print(l2d(ls))

# ls = [1, 2, 3, 4]
#
# new_dict = current = {}
# for name in ls:
#     current[name] = {}
#     current = current[name]
# print(new_dict)

# 3.Write a Python program to find the first non-repeated element in a list.
# lst = [1, 2, 3, 1, 2, 3]
#
# def first_non_repeated_el(l):
#     ctr = {}
#     for i in l:
#         if i in ctr:
#             ctr[i] +=1
#         else:
#             ctr[i] = 1
#
#     for i in l:
#         if ctr[i] == 1:
#             return i
#
# print(first_non_repeated_el(lst))

# import time
# import random
# num = 67
# BIG = 1_000_000
#
# start = time.time()
# ls = [random.randint(1, 100) for _ in range(BIG)]
# # s_ls = sorted(ls)
# x = num in ls
# print(f"search in list - {time.time() - start}")
# print(f"size of list - {ls.__sizeof__()}")
# start = time.time()
# d = {k + 1: v for k, v in enumerate(ls)}
# y = num in d.values()
# print(f"search in dictionary - {time.time() - start}")
# print(f"size of dictionary - {d.__sizeof__()}")

# dictionary is faster than list, but has more size; in our example: speed x3 in dict, but size x5 in dict

# prime numbers search algorithm


# from prime import *

# lst = [x for x in range(1, 100_001)]
# start = time.time()
# simple = list(filter(prime_simple, lst))
# print(f"for simple algorithm - {time.time() - start}")
# start = time.time()
# fast = list(filter(fast_prime, lst))
# print(f"for fast algorithm - {time.time() - start}")
# print(list(filter(lambda n: not prime_simple(n), lst)))
# start = time.time()
# erato = list(filter(fast_prime, lst))
# print(f"for erato algorithm - {time.time() - start}")


# st = "weeksyourweeks"
# tbl = {119: 103, 121: 102, 117: None}
# print(st.translate(tbl))

# student_list = {'S 001': ['Math', 'Sciences'], 'S      002': ['Math', 'English']}
# print(student_list)
#
# # remove extra spaces
# student_dict = {k.translate({32: None}): v for k, v in student_list.items()}
# print(student_dict)


# print(ord('h'))
# st = 'hello'
# table = {ord('h'): ord('h') + 2, ord('e'): ord('e') + 2, ord('l'): ord('l') + 2, ord('o'): ord('o') + 2}
# encrypt = st.translate(table)
# print(encrypt)
#
# decrypt = {v: k for k, v in table.items()}
# print(encrypt.translate(decrypt))

#Caesar cipher

# def rotate_chr(c):
#     rot_by = 3
#     c = c.lower()
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     # keep punctuation and whitespaces
#     if c not in alphabet:
#         return chr(ord(c) + 4)
#     rotated_pos = ord(c) + rot_by
#     if rotated_pos <= ord(alphabet[-1]):
#         return chr(rotated_pos)
#     return chr(rotated_pos - len(alphabet) + rot_by)
#
# print("".join(map(rotate_chr, "My secret message goes here.")))

# print("Hello")
# try:
#     print(x)
# except NameError as err:
#     print(err)
#     # print("Oops! Something gone wrong!")

try:
    x = int(input("Enter a number: "))
    print(x + 5)
except ValueError as e:
    print(e)

# if x.isdigit():
#     x = int(x)
#     print(x)
# else:
#     print("x is not digit")