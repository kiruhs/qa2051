# set1 = {'a', 'b', 'c', (1, 2, 3)}
# set2 = {1, 2, 3, 'a', 'c', (1, 2, 3)}
# set3 = {"John", "Elena"}

# myset = set1.union(set2, set3)
# myset = set1 | set2 | set3
# set1 |= set2 # set1 = set1 | set2
# print(set1)

# int_sec = set1.intersection(set2)
# int_sec = set1 & set2
# print(set1)
# print(int_sec)
# set1.intersection_update(set2)
# set1 &= set2
# print(set1)

# set1 = {'a', 'b', 'c', (1, 2, 3)}
# set2 = {1, 2, 5, 'a', 'c', (1, 2, 3)}

# print(set1.difference(set2))
# print(set2 - set1)

# set1.difference_update(set2)
# print(set1)
# set2 -= set1
# print(set2)

# print(set1.symmetric_difference(set2))
# print(set1 ^ set2)

# set2.symmetric_difference_update(set1)
# set2 ^= set1
# print(set2)

# set1 = {2, 6, 0, 5, 4}
# set2 = {6, 4, 2}
#
# print(set1.issubset(set2))
# print(set1.issuperset(set2))


# performance
import time

# MAX_VALUE = 10_000_000
# SEARCH_ITEM = 9_999_990
# lst = [i*i for i in range(MAX_VALUE)]
# st = {i*i for i in range(MAX_VALUE)}
# # print(lst)
# # print(st)
#
# start = time.time_ns()
# print(SEARCH_ITEM**2 in lst)
# print(f"searching time in list - {time.time_ns() - start}")
#
# start = time.time_ns()
# print(SEARCH_ITEM**2 in st)
# print(f"searching time in set - {time.time_ns() - start}")

# set1 = {3, 5, "hello"}
# print(hash(3)) # password
# print(hash(5))
# print(hash("hello"))

# (1, 2, 3), 3 --> (1, 2)

# def del_from_tuple(tpl, elem):
#     lst = list(tpl)
#     for i in lst:
#         if i == elem:
#         lst.remove(elem)
#     return tuple(lst)
#
# print(del_from_tuple(("hello", 3, 5, 3, True, {3, 6}, 3), 3))

# dictionaries
# ls = ["john", "smith", 40, 231152142, 180, 78]
# iterable, not subscriptable (no indexes), not ordered(until 3.7), no duplicates(in keys), contain pairs, key:value

# dct = {}
# dct2 = dict()
# print(type(dct2))

# dct = {"brand": "Ford",
#        "year": 2000,
#        "model": ["Mustang", ["Focus Sedan", "Focus hatchback"], "Fiesta"],
#        "year": 1980,
#        "year": 1977}
# print(dct)
# print(len(dct))
# print(id(dct["model"]))
# print(dct["brand"])
# print(dct.get("year"))
# dct["model"].append("Focus")
# dct["type"] = "Sedan"
# print(dct)
# print(id(dct["model"]))
# # dct["model"][1][1] = "Coupe"
# print(dct)

# new_dict = dict(name= "John", last_name= "Smith", age= 40, gender= "male", country= "USA")
# print(new_dict)
# print(new_dict.keys())
# print(new_dict.values())

# print(new_dict.items())

# new_dict.update({"countr": "Ireland"}) # doesn't control existence of keys
# print(new_dict)
# print(id(new_dict))
# print(new_dict.popitem())
# print(new_dict)
#
# print(new_dict.pop("age")) # returns the value only
# print(new_dict)
#
# print(new_dict.clear())
# print(new_dict)
# print(id(new_dict))
#
# del new_dict

# for x in new_dict:
#     print(x)

# for x in new_dict.keys():
#     print(x)

# for x in new_dict.values():
#     print(x)

# for x in new_dict:
#     print(new_dict[x])

# for k, v in new_dict.items():
#     print(k, v, sep=" : ")

# newest_dict = new_dict
# copy_dict = new_dict.copy()
# sec_copy_dict = dict(new_dict)
# print(newest_dict is new_dict)
# new_dict["age"] = 45
# new_dict["weight"] = 45
# print(newest_dict)
# print(copy_dict)
# print(copy_dict is new_dict)
# print(sec_copy_dict)
# print(40 in new_dict.values())

# if "country" in new_dict.keys():
#     print("We have a country")

# for k, v in new_dict.items():
#     if v == 45:
#         print(k)
from pprint import pprint
# my_kids = {
#     "child1": {
#         "name": "Bob",
#         "dob": 2004
#     },
#     "child2": {
#         "name": "Alice",
#         "dob": 2011
#     },
#     "child3": {
#         "name": "John",
#         "dob": 2014,
#         "hobby": "painting"
#     }
# }
# pprint(my_kids)
# print(my_kids["child2"]["name"])
# my_kids["child3"]["hobby"] = "signing"
# pprint(my_kids)

# child1 = {"name": "Bob", "dob": 2004}
# child2 = {"name": "Mary", "dob": 2014, "hobby": "running"}
#
# my_kids = {"kid1": child1, "kid2": child2}
# pprint(my_kids)

import itertools

tpl = ("day1", "day2", "day3", "day4", "day5", "day6", "day7")
# d = dict.fromkeys(tpl, 1)
# print(d)

tpl2 = (1, 2, 3, 4)
# print(tuple(zip(tpl, tpl2)))
print(dict(zip(tpl, tpl2)))
print(dict(itertools.zip_longest(tpl,tpl2, fillvalue="0")))