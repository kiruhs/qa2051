# tpl = (3, 7, 9, 1, 3)
# # tpl1 = <3 7 9 1 3>
#
# class MuTuple(tuple):
#     def __init__(self, t):
#         if isinstance(t, tuple):
#             self.__t = t
#
#     def __str__(self):
#         res = ""
#         for c in self.__t:
#             res+= (str(c)+' ')
#         return '<'+res.strip()+'>'
#
# tp = MuTuple(tpl)
# print(tp)

# class Queue:
#     def __init__(self):
#         self.items = []
#
#     def enqueue(self, it):
#         self.items.append(it)
#
#     def dequeue(self):
#         if not self.is_empty():
#             return self.items.pop(0)
#         raise IndexError("Cannot dequeue from an empty queue")
#
#     def is_empty(self):
#         return len(self.items) == 0
#
# q = Queue()
# # q.dequeue()
# q.enqueue(2)
# q.enqueue(10)
# q.enqueue(0)
# first = q.dequeue()
# second = q.dequeue()
#
# print(first)
# print(second)
#
# print(q.items)

# pascal triangle

# x = int(input("Enter the size of triangle: "))
# pascal = []
# for _ in range(x):
#     pascal.append([1] + [0] * x)
#
# for i in range(1, x):
#     for j in range(1, i + 1):
#         pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
#
# for i in range(x):
#     print(" " * (x - i), end="")
#     for j in range(i+1):
#         print(pascal[i][j], end=' ')
#     print()
# # print(pascal)

# class Geom:
#     name = "Geom"
#
#
#     def get_perimeter(self):
#         a = 10 + 5
#         print(f"a= {a}")
#     def draw(self):
#         print("some figure drawing")


# class Rectangle(Geom):
#     name = "Rectangle"
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def draw(self):
#         return "drawing rectangle"
#
#     def get_perimeter(self):
#         return 2 * (self.width + self.height)
#
# class Square(Geom):
#     name = "Square"
#
#     def __init__(self, line):
#         self.line = line
#
#     def get_perimeter(self):
#         return 4 * self.line
#
# class Triangle(Geom):
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimeter(self):
#         #super().get_perimeter()
#
#         return self.a + self.b + self.c
#
# g = Geom()
# r = Rectangle(3, 6)
# print(r.get_perimeter())
# s = Square(5)
# print(s.get_perimeter())
# t = Triangle(3, 5, 9)
# print(t.get_perimeter())

# MyList

# [3, 4, 1]
# <<1, 3, 4>> sorted list
# my customer class should contain the numbers only, should be sorted and in << brackets

# class MyList(list):
#     """This class is a mutation of list class, that can get only numeric list, returns sorted list in << brackets
# returns length of positive numbers and zeros only
# """
#     def __init__(self, it):
#         for i in it:
#             if not isinstance(i, (int, float, bool)):
#                 raise NotImplementedError
#         super().__init__(sorted(it))
#         self.index = 0
#
#     def append(self, __object):
#         "This method blablabla"
#         if not isinstance(__object, (int, float, bool)):
#             raise NotImplementedError
#         super().append(__object)
#         self.sort()
#
#     def __str__(self):
#         return f"<<{', '.join(str(item) for item in self)}>>"
#
#     def __call__(self, start=None, end=None, step=None):
#         return f"<<{', '.join(str(item) for item in self[slice(start, end, step)])}>>"
#
#     def __getitem__(self, item):
#         if isinstance(item,slice):
#             return MyList(super().__getitem__(item))
#         return super().__getitem__(item)
#
#     def __len__(self):
#         cnt = 0
#         for i in self:
#             if i >= 0:
#                 cnt += 1
#         return cnt
#
#     @property
#     def dif(self):
#         return self[-1] - self[0]
#
#     def __add__(self, other):
#         if isinstance(other, list):
#             return MyList(super().__add__(other))
#
#     @property
#     def length(self):
#         return super().__len__()
#
#     def __sub__(self, other):
#         if not isinstance(other, int) or other < 0:
#             raise TypeError
#         if other > self.length:
#             print("The number is greater than the list length")
#             return None
#         for _ in range(other):
#             self.pop()
#         return self
#
#     def __lt__(self, other):
#
#         if self.length < MyList(other).length:
#             return True
#         return False
#
#     def __gt__(self, other):
#         if self.length > MyList(other).length:
#             return True
#         return False
#
#     def __ge__(self, other):
#         if self.length >= MyList(other).length:
#             return True
#         return False
#
#     def __radd__(self, other):
#         if isinstance(other, list):
#             return MyList(super().__add__(other))
#
#     def __next__(self):
#         if self.index >= self.length:
#             raise StopIteration
#         value  = self[self.index]
#         self.index += 1
#         return value
#
# l = MyList([3, 4, 1, -8, 0])
# print(l[1:5:2])
# print(l[2])
# l.append(-10)
# print(l)
# print(len(l))
# print(l.dif)
# lst = [2, -6, 70]
# ll = l + lst
# print(ll - 10)
# print(ll)
# print(l == lst) # __eq__
# ll = lst + l
# print(ll)
# print(next(ll))
# print(next(ll))
# print(ll)
#
#
# help(l.append)


# def say_name(name):
#     # name = "Kuku"
#     def say_goodbye():
#         print("Don't say me goodbye, " + name + "!")
#     return say_goodbye
#
#
# value = say_name("Alexander")
# value2 = say_name("John")
# value()
# value2()

# def counter(start=0):
#     def step():
#         nonlocal start
#         start +=1
#         return start
#     return step
#
# c1 = counter(10)
# c2 = counter()
# print(c1(), c2())
# print(c1(), c2())
# print(c1(), c2())
# print(c1(), c2())

# def shout(text):
#     return text.upper()
# print(shout("Hello"))
#
# yell = shout
# print(yell("Bye-bye"))

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def lst(text):
    return text.split()

def greet(func):
    greeting = func("Hi, I am created by a function passed as an argument")
    print(greeting)

greet(shout)
greet(whisper)
greet(lst)