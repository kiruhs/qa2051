# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __getattribute__(self, item):
#         # print("method __getattribute__()")
#         # print("it is my method")
#         if item == 'x':
#             raise ValueError("no access")
#         else:
#             return object.__getattribute__(self, item)
#
#     def __setattr__(self, key, value):
#         if key == 'z':
#             raise AttributeError("not allowed name")
#         else:
#             print("__setattr__")
#             object.__setattr__(self, key, value)
#             # self.x = value infinite recursion call
#
#     def __getattr__(self, item):
#         print("__getattr__: " + item)
#         return False
#
#     def __delattr__(self, item):
#         print("now the attribute is deleted: " + item)
#         object.__delattr__(self, item)
# p1 = Point(2, 4)
# y = p1.y
# print(p1.y)
# p1.y = 6
# p1.z = 10
# print(p1.y)
# print(p1.z)
# # print(dir(object))
# del p1.y
# print(p1.__dict__)

# property

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         self.__age = age
#
#     @age.deleter
#     def age(self):
#         del self.__age

    # age = property(get_age, set_age)
    # age = age.setter(set_age)
    # age = age.getter(get_age)

# p = Person("John", 30)
# p.__dict__['age'] = "age in object p"
# print(p.__dict__)
#
# p.age = 45
# print(p.age)
# del p.age
# print(p.__dict__)

# dunder method __call__

# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, step=1, *args, **kwargs):
#         # print("method works")
#         self.__counter +=step
#         return self.__counter
#
# c = Counter()
# c2 = Counter()
# c()
# c()
# res = c(10)
# print(res)
# res2 = c2(-5)
# print(res2)

# class StripChars:
#     def __init__(self, chars):
#         self.__counter = 0
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise TypeError("The argument should be a string")
#         return args[0].strip(self.__chars)
#
# obj = StripChars("?:,.;! ")
# res = obj("?: Hello, world!!!   ")
# print(res)

# class Point:
#     def __init__(self, *args):
#         self.__coords = args
#
#     def __len__(self):
#         return len(self.__coords)
#
#     def __abs__(self):
#         return list(map(abs, self.__coords))
#
# p = Point(1, -2)
# p2 = Point(2, 4, -8, 4, 5, -76)
#
# print(len(p))
# print(len(p2))
# print(abs(p))
# print(abs(p2))

# Inheritance - Наследование

# class Geom:
#     name = 'Geom'
#
# class Line(Geom):
#     # name = "Line"
#     def draw(self):
#         print("Line drawing")
#
# g = Geom()
# l = Line()
# print(g.name)
# print(l.name)
# l.draw()
# g.draw() # is not working in this direction

# class Geom:
#     name = 'Geom'
#
#     def set_coords(self, x1, x2, y1, y2):
#         self.x1 = x1
#         self.x2 = x2
#         self.y1 = y1
#         self.y2 = y2
#
# class Line(Geom):
#     def draw(self):
#         print("Line drawing")
#
# class Rect(Geom):
#     def draw(self):
#         print("Rectangle drawing")
#
#
# l = Line()
# r = Rect()
# l.set_coords(1, 1, 5, 6)
# r.set_coords(2, 2, 5, 5,)
# print(l.__dict__)
# print(r.__dict__)

# class Geom:
#     pass
#
# class Line(Geom):
#     pass
#
# g = Geom()
# l = Line()

# print(issubclass(g, object)) # doesn't work with objects, classes only
# print(isinstance(l, Geom))
# print(Line.mro()) # returns the whole chain until object
# print(Line.__bases__) # returns the parent

# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
# v = Vector([1, 2, 3])
# print(v)

class Geom:
    name = 'Geom'
    def __init__(self, x1, x2, y1, y2):
        print(f"Initialization Geom for {self.__class__}")
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

class Line(Geom):



    def draw(self):
        print("Line drawing")

# class Rect(Geom):
#
#     def __init__(self, x1, x2, y1, y2, fill=None):
#         super().__init__(x1, x2, y1, y2)
#         print("Rect initialization")
#         self.fill = fill
#
#     def draw(self):
#         print("Rectangle drawing")
#
# l = Line(1, 3, 5, -4)
# r = Rect(3,2, 8, 7, 'solid')
# print(l.__dict__)
# print(r.__dict__)

# class Person:
#     def person_info(self, name, age):
#         print("Inside Person class")
#         print("Name:", name, "Age:", age)
#
# class Company:
#     def company_info(self, c_name, location):
#         print("Inside Company class")
#         print("Name:", c_name, "Location:", location)
#
#     def person_info(self, name2, age):
#         print("Inside Person class")
#         print("Name2:", name2, "Age:", age)
#
# class Employee(Person, Company):
#     def employee_info(self, salary, skill):
#         print("Inside Employee class")
#         print("Salary:", salary, "Skill:", skill)
#
# emp = Employee()
# emp.person_info("John", 35)
# emp.company_info("Google", "Palo Alto")
# emp.employee_info(12000, "Machine learning")

# polymorphism
# x = 5
# y = 7
# print(x + y)
# a = "5"
# b = "7"
# print(a + b)