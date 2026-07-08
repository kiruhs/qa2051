# EX1
# dct = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# Solution 1
# print(id(dct['C1']))
# def exercise(dictionary):
#     for key in dictionary:
#         dictionary[key].clear()
#     return dictionary
from sqlalchemy.util import symbol

# Solution 2
# def exercise(dictionary):
#     for key in dictionary:
#         dictionary[key] = []
#     return dictionary
# print(exercise(dct))
# print(id(dct['C1']))
# EX3
# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
# lst3 = [7, 8, 9]
#
# res = map(lambda x, y, z : x + y + z, lst1, lst2, lst3)
# print(list(res))

# lst = [10, 20, 30, 40, 50, 30, 30, 20, 30, 49, 50, 60, 70, 80]
# lst2 = []
# def longest(l):
#     if len(l) == 0:
#         return 0
#     maxl = 1
#     fin = 1
#     for i in range(len(l)-1):
#         if l[i] < l[i + 1]:
#             maxl += 1
#         else:
#             if fin < maxl:
#                 fin = maxl
#             maxl = 1
#     return max(fin, maxl)
#
# print(longest(lst))
# import math
# print(math.factorial(1_000))

# dct = dict(name= "John", age=40, height=180)
# dct = dict([("name", "John"),("age", 50), ("wife", "Mary"), (1, 2)])
# st = "12 23 4 53 6 7 4 99 8 7 56 3 42"
# dct = {int(key): int(key)*2 for key in st.split() if int(key)%2 == 0}
# print(dct)
# from pprint import pprint
# st = "Hello group qa2051, we are learning the Python, one of the greatest programming languages"
#
# def count_symbols(input_st):
#     symbol_dict = {}
#     for sym in input_st:
#         if sym.lower() in symbol_dict:
#             symbol_dict[sym.lower()] += 1
#         else:
#             symbol_dict[sym.lower()] = 1
#     return symbol_dict
#
# pprint(dict(sorted(count_symbols(st).items(), key=lambda item: item[1], reverse=True)), sort_dicts=False)
# print(count_symbols(st))

# dct = {"brand": "Ford", "model": "Mustang", "year": 2005}
#
# dct.setdefault("model", "Bronco")
# dct.setdefault("color", "yellow")
# print(dct)

# num = [2, 18, 5, 7, 2, 32, 6, 9, 4, 8, 9, 4,12, 14, 14, 5, 9, 2]
#
# d = {k: num.count(k) for k in num}
# print(d)

st = "Hello group qa2051, we are learning the Python, one of the greatest programming languages"

# cnt = {ch: st.count(ch) for ch in st}
# print(cnt)

# dct = {"brand": "Ford", "model": "Mustang", "year": 2005}
# print(dct.get("br", 5))

# cnt = {}
# for ch in st:
#     cnt[ch] = cnt.get(ch, 0) + 1
#
# print(cnt)

# from collections import Counter
# print(Counter(st))

# dct1 = {"item": "jacket", "size": "L", "color": "black"}
# dct2 = {"model": "western", "quantity": 50, "color": "blue"}

# dct1 = dct1 + dct2 doesn't work'

# new = {}
# for _ in dct1:
# new.update(dct1.items())

# for _ in dct2:
# new.update(dct2.items())
# print(new)

# new = dct1 | dct2
# print(new)
# print({**dct1, **dct2})

# interactive vocabulary

# words = {}

# print("This is the interactive dictionary, that you create yourself\n"
#       "just enter a word... (for exit input 'q' button)")
#
# while True:
#     w = input()
#     if w == 'q':
#         break
#     if w in words:
#         print(f"word {w} is translated as {words[w]}")
#     else:
#         words[w] = input("Input the translation in Russian: ")
#     print("enter a word... ")

# dct1 = {"item": "jacket", "size": "L", "color": "black", "quantity": 100}
# dct2 = {"model": "western", "quantity": 50, "color": "blue"}
#
# for common_key in dct1.keys() & dct2.keys():
#     print((common_key, dct1[common_key]),(common_key, dct2[common_key]))