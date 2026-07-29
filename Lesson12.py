# {} () []

s1 = "{fgt{rt)(ff}[fd ]}"   # LIFO
# }dfsefwe
# s2 =  "{()}"
# def is_balanced(s):
#     stack = []
#     mapping = {')':'(', ']':'[', '}': '{'}
#     for char in s:
#         if char in ('[', '{', '('):
#             stack.append(char)
#         elif char in mapping:
#             # if len(stack) > 0:
#             top_element = stack.pop() if stack else '#'
#             if mapping[char] != top_element:
#                 return False
#             # elif char not in ('[', '{', '('):
#             #     continue
#             # else:
#             #     stack.append(char)
#
#   #  if len(stack) == 0:
#     return not stack
#    # return False
#
# print(is_balanced(s1))

# n, m = 6, 7

# matrix = [[0]*m for _ in range(n)]
# print(matrix)
# dx, dy, x, y = 0, 1, 0, 0
#
# for i in range(1, n * m + 1):
#     matrix[x][y] = i
#     if matrix[(x+dx) % n][(y + dy) % m]:
#         dx, dy = dy, -dx
#     x += dx
#     y += dy
# # print(matrix)
#
# for line in matrix:
#     print(*(f"{i:<3}" for i in line), sep='')

# nestedlist = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10, 'a']]]
#
# new_list = []
#
# def list_unpack(lst):
#     for i in lst:
#         if isinstance(i, list):
#             list_unpack(i)
#         else:
#             new_list.append(i)
#
# list_unpack(nestedlist)
# print(new_list)

# tpl = (1, "hello", [4.2, 0])

# for x in tpl:
#     print(type(x))

# print(type(tpl))

# def multitype(obj):
#     if isinstance(obj,tuple):
#         return tuple(type(x) for x in obj)
#     return type(obj)
#
# print(multitype(tpl))

# class Point:
#     color = 'red'
#     circle = 2
#     x = 5
#     y = 10
#
# a = Point()
# b = Point()
# print(a.x, a.y, sep=";")
# b.x = 8
# b.y =4
# print(b.x, b.y, sep=";")

# class Point:
#     color = 'red'
#     circle = 2
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"The point with coords {self.x, self.y}"
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_coord(self):
#         return self.x, self.y
#
#
#
#
# a = Point(5, 10)
# print(a.__dict__)
# b = Point(-3, 2)
# print(b.__dict__)
# # print(Point.__dict__)
# a.set_coord(100, 200)
# print(a.get_coord())
# print(a)
# print(b)
# c = Point()
# print(c.__dict__)

# class Vector2:
#     MIN_COORD = 0
#     MAX_COORD = 100
#
#     @classmethod
#     def validate(cls, arg):
#         return cls.MIN_COORD <= arg <= cls.MAX_COORD
#
#     def __init__(self, x, y):
#         self.x = self.y = 0
#         if self.validate(x) and self.validate(y):
#             self.x = x
#             self.y = y
#         print(self.pwr(self.x, self.y))
#
#     def get_coord(self):
#         return self.x, self.y
#
#     @staticmethod
#     def pwr(x, y):
#         return x**y
#
# v = Vector2(20, 2)
# res = v.get_coord()
# # print(v.validate(5)) # not recommended
# print(Vector2.validate(70))
# print(res)
# print(Vector2.pwr(3, 4))

from accessify import private, protected

class Point:
    def __init__(self, x, y):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
    @private
    @classmethod
    def __check_value(cls, z):
        return type(z) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Coordinates should be numbers")

    def get_coord(self):
        return self.__x, self.__y

p = Point(1, 2)
# p.__x = 5
# p.__y = 5
# print(p.__x, p.__y)
# print(p.__dict__)
# p._Point__x = 100
print(p.__dict__)

p.set_coord(3.5, 6)
print(p.get_coord())
print(p.__dict__)

print(p._Point__check_value(5))