# tuple - кортеж
# iterable, ordered, duplications enable, immutable

# x = ()
# x
# type(x)
# y = tuple()
# y[0] # receive error
# x = x + (1, 2)
# x
# (1, 2)
# x = ()
# id(x)
# x = x + (1, 2)
# x
# id(x)
# y = (1, 2)
# y
# id(y)
# x == y
# x is y
# y = (2, 1)
# x == y
# z = (5)
# z = (5,)
# del y
# y = 1, 2
# del z
# z = 5,
# a = 1, 2 + 3, 4
# a
# a = (1, 2) + (3, 4)
# a
# a += 1+4+5-19,
# a

# print((1, 2))

# x, y = (3, 4) # equal to x, y = 3, 4
# print(x)
# x, y = ("Hello", "world!")
# print(x)
# *x, w, y, z = "hello"
# print(y)
# print(x)
# print(z)
# t = 0, 3, 5
# a, b, c = t
# print(b)

# tpl = ("hello", "world", 4, True, [4, 5])
# print(tpl)
# fruits = ("apple", "banana", "cherry", "orange")
# print(fruits[1:3])
# print(fruits[::-1])
# fruits[1] = "kiwi" # is not allowed
# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits
# print(f"the green fruit is {green}")
# print(f"the yellow fruit is {yellow}")
# print(f"the red fruit is {red}")

# for f in fruits:
#     print(f)
#
# for i in range(len(fruits)):
#     print(fruits[i])

# tpl1 = "a", "b", "c"
# tpl2 = 1, 2, 3
# tpl3 = tpl2 + tpl1
# print(tpl3)

# tpl4 = tpl3[:4] + ("w",) + tpl3[5:]
# print(tpl4)
#
# l = list(tpl3)
# l[4] = "w"
# tpl4 = tuple(l)
# print(tpl4)

# tpl = "apple", "banana", 4, 3.5, 4, True, (3, 5, 7), [10, 32, [], (), (4, 6, 7), -4]
# print(tpl)
# print(len(tpl))
# print(id(tpl))
# print(tpl[3])
# print(tpl[-1])
# # tpl[-1][:] = []
# print(tpl[-1][4][2])#  = 6
# tpl[-1].append(100)
# tpl[-1].pop(0)
# print(tpl)
# print(id(tpl))
# print(len(tpl))

# tpl = 1, 2, 3
# tpl = tpl * 3
# print(tpl)

# tpl = 1, 3, 7, 8, 7, 5, 4, 6, 8, 5
# print(tpl.index(2) if 2 in tpl else None)

# print(tpl.count(2))
# lst = [x**2 for x in range(11)]
# tpl = tuple(x**2 for x in range(11))
# print(tpl.__sizeof__())
# print(lst.__sizeof__())

# pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
# _sum = sum(x[0] for x in pairs)
# print(_sum)
# concatenation = "".join(x[1] for x in pairs)
# print(concatenation)

Input = [(4, 5), (2, 3), (6, 7), (2, 7)]

# ln = len(Input)
#
# for i in range(ln):
#     for j in range(ln -i -1):
#         if (Input[j][0]+Input[j][1]) > (Input[j+1][0]+Input[j+1][1]):
#             Input[j], Input[j+1] = Input[j+1], Input[j]
#
# print(Input)

# result = sorted(Input, key=sum)
# print(result)
# Input.sort(key=sum)
# print(Input)
#
# result = sorted(Input, key=lambda x: x[0] + x[1])
# print(result)
#
# Input.sort(key=lambda y: (sum(y), y[0]))
# print(Input)

# li = [4, 5, 6, "hello", 10, (1, 2, 4), "p", 11, -9, 0]
#
# def cnt(lst):
#     counter = 0
#     for num in lst:
#         if isinstance(num, tuple):
#             break
#         counter += 1
#     return counter
#
# print(cnt(li))

# Max = lambda a, b: a if a > b else b
#
# print(Max(11, 6))
#
# print((lambda a, b: a if a > b else b)(11, 90))

# Min = lambda a, b, c: f"{a} is the smaller" if a < b and a < c \
#     else f"{b} is the smaller" if b < c else f"{c} is the smaller"
#
# print(Min(60, 40, 20))

# subj_marks = [('English', 88), ('Science', 90), ('Math', 97), ('Sports', 82)]
# subj_marks.sort(key=lambda x: x[1])
# print(subj_marks)

# set - множество
# mutable, not ordered, iterable but not indexed, no duplications enabling, cannot contain other mutable types inside
# hashable

# set1 = {1}
# set1 = {100, 1, 3, 5, 3, 3, 5, 3,"hello", True, (1, 3), (1, 3), "Hello", 100.1}
# print(set1)
# print(len(set1))
# for s in set1:
#     print(s, end=',')
# # print(set1[2]) # not allowed
# print()
# print((1, 3) in set1)

# set2 = set()
# print(type(set2))

# set3 = {3, 7, *{5, 6}}
# print(set3)

# str1 = "abracadabra"
# s = set(str1)
# print(s)

# fruits = {"apple", "orange", "banana", "cherry"}
# tropical = {"kiwi", "pineapple", "mango"}
# fruits.add("apricot")
# print(fruits)
# fruits.update(tropical)
# print(fruits)
# x = "apple"
# print(hash(x))
# fruits.remove("mango")
# fruits.remove("mango")
# fruits.discard("mango")
# fruits.discard("mango")
# fruits.discard("mango")
# fruits.discard("mango")
# print(fruits)
#
# deleted = fruits.pop()
# print(deleted)
# fruits.clear()
# print(fruits)
# del fruits

