# for loop and while loop

# cnt = 0
# while True:
#     print(cnt)
#     cnt +=1
#     if cnt == 12:
#         break

# for cnt in range(10,-1,-1):
#     print(cnt)
# print(5, end="")
_str = "hello, world!"
# for a in _str:
#     print(a, end=str(len(_str)))
# cnt = 0
# for a in _str:
#     cnt += 1
# print(cnt)

# [print(a, end=" ") for a in _str]

# for i in range(len(_str)):
#     print(_str[i], end=":")

# [print(_str[i], end=":") for i in range(len(_str))]

# for b in _str:
#     if b == "Z":
#         break
#     print(b)
# else:
#     print(1000)

# st = "1. Hello, world! The version 3 of Python is more powerful than 2."
# for i in st:
#     if i.isdigit(): # isalpha
#         print(i, end=":")

# List - mutable, iterable, ordered, duplication enabled

# lst1 = [2, 4, 8, -4, 5, -6, -4, 101, 4, 5, 7]
# print(lst1)
#
# lst2 = [2.6, -9, "Hello", True, "3", "pyhton", -7, [3, 6, "kuku"], 2]
# print(lst2)
# print(lst2[3])
# print(lst2[-2][2])
# print(lst2[7:2:-1])
# lst3 = lst2
# print(id(lst2))
# print(id(lst3))
# lst2[0] = "world"
# print(id(lst2))
# print(id(lst3))
# print(lst3)
# lst3.clear()
# print(lst2)
# print(id(lst2))
# print(id(lst3))

# lst3 = lst2.copy()
# print(id(lst2[7]))
# print(id(lst3[7]))
#
# lst4 = list(lst2)
# print(id(lst4[7]))
# lst5 = lst2[::]
# print(id(lst5[7]))
#
# import copy
# lst6 = copy.deepcopy(lst2)
# print(id(lst6[7]))
# lst2[7][-1] = "hoho"
# print(lst4)
# print(lst6)

# fruits = ["apple", "cherry", "banana"]
# fruits2 = fruits.copy()
# print(fruits == fruits2)
# print(fruits is fruits2)

# if "banana" in fruits:
#     print(True)
# else:
#     print(False)

# print("banana" in fruits)

# fruits.append("melon")
# print(fruits)
# fruits[1:2] = ["orange", "cherry"]
# print(fruits)
# fruits[1:3] = ["orange"]
# fruits[1:3] = ["melon"]
# print(fruits)
# fruits.insert(2, "lemon")
# print(fruits)
# fruits.insert(8, "papaya")
# print(fruits)
# fruits.append("kiwi")
# print(id(fruits))
# tropical = ["guava", "pineapple", "mango"]
# fruits.extend(tropical)
# print(id(fruits))

# tropical.extend(fruits)
# print(tropical)

# new_fruits = fruits + tropical
# print(new_fruits)
# fruits = fruits + tropical + [4,5,6]# not equal to fruits += tropical
# print(fruits)
#
# print(fruits.pop(5))
# print(fruits)
#
# # del fruits
# print(fruits)

# st = "Hello world!What a beautiful day is today"
# # print(st.split())
#
# for a in st:
#     if a not in " ":
#         print(a, end="-")
#
# print(*[a+"|" for a in st if a not in " "])

# st = "Hello, world!!! Today is 18.06.2026."
#
# print([a for a in st if not a.isdigit() and a not in (" ","!",".",",")])

# * 5x6

# for i in range(5):
#     for j in range(6):
#         print('*', end=" ")
#     print()

# print([a for a in range(1, 101) if a**0.5 == int(a**0.5)])
#
# print([a*a for a in range(1, 11) ])

lst1 = [2, 4, 8, -4, 5, -6, -4, 101, 4, 5, 7]
fruits = ["apple1", "apple", "Orangegege", "kiwi", "cherry", "banana"]

# sort_lst = sorted(lst1, reverse=True)
# print(sort_lst)
# print(lst1)

sort_fruits = sorted(fruits, key=len, reverse=True)
print(sort_fruits)