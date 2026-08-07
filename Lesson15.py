# returning function from another function
# from Lesson14 import greet

# def create_adder(x):
#     def adder(y):
#         return y + x
#     return adder
#
# add_15 = create_adder(15)
# print(add_15)
# print(add_15(25))
# print(add_15(10))
# print(add_15(18.5))
#
# add_15 = create_adder(1)
# print(add_15(18.5))



# func()

# def mydecorator(fn):
#     def inner_func():
#         fn()
#         print("I am fine")
#     return inner_func
# # func = mydecorator(func)
#
# @mydecorator
# def func():
#     print("How are you?")
#
#
# func()

# def func_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("It is before function call")
#         func(*args, **kwargs)
#         print("It is after function call")
#         func(*args, **kwargs)
#
#     return wrapper
#
# @func_decorator
# def some_func(title, tag="Empty", name=""):
#     print(f"Function works in {title}, tag= {tag}, name={name}")
#
# some_func("Python", name="Alexander")

# import time
# def time_test(func):
#     def wrapper(*args, **kwargs):
#         start = time.time_ns()
#         res = func(*args, **kwargs)
#         print(f"The execution time of {func.__name__}is: {time.time_ns() - start}")
#         return res
#
#     return wrapper
#
# @time_test
# def get_nod(a, b):
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     return a

# @time_test
# def get_fast_nod(a, b):
#     if a < b:
#         a, b = b, a
#         while b:
#             a, b = b, a%b
#     return a
#
# print(get_nod(4, 10000))
# print(get_fast_nod(4, 10000))

def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner

def decor2(func):
    def inner():
        x = func()
        return 2 * x
    return inner

# @decor1
# @decor2
# def num1():
#     return 10
# print(num1())
#
#
# @decor2
# @decor1
# Comment
# def num2():
#     return 10
# print(num2())
#
# print(decor2(decor1(num2))())

# import math
from functools import wraps
#
# def df_decorator(name, dx):
#     def func_decorator(func):
#         @wraps(func)
#         def wrapper(x, *args, **kwargs):
#             # dx = 0.0001
#             print(name)
#             res = (func(x+dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
#             return res
#         # wrapper.__name__ = func.__name__
#         # wrapper.__doc__ = func.__doc__
#         return wrapper
#     return func_decorator
#
# @df_decorator("Alexander", 0.0001)
# def sin_df(x):
#     "This function calculates sinus of some value"
#     return math.sin(x)
#
# df = sin_df(math.pi/3)
# print(df)
# print(f"function name is: {sin_df.__name__}")
# # print(sin_df.__doc__)
# help(sin_df)

# def repeater(num_times):
#     def decorator_repeat(func):
#         @wraps(func)
#         def wrapper_repeat(*args, **kwargs):
#             for _ in range(num_times):
#                 value = func(*args, **kwargs)
#             return value
#         return wrapper_repeat
#     return decorator_repeat
#
# @repeater(3)
# def greet(name):
#     print(f"Hello, {name}!")
#
# greet("Alexander")
#
# @repeater(5)
# def sum2(x, y):
#     print(x + y)
# sum2(3, 4)

# measuring of memory usage

# import tracemalloc
#
# def measure_memory_usage(func):
#     def wrapper(*args, **kwargs):
#         tracemalloc.start()
#         result = func(*args, **kwargs)
#
#         snapshot = tracemalloc.take_snapshot()
#         top_stats = snapshot.statistics("lineno")
#
#         print(f"Memory usage of {func.__name__}: ")
#         for stat in top_stats[:5]:
#             print(stat)
#         return result
#     return wrapper

# @measure_memory_usage
# def create_list(l):
#     ls = [i**2 for i in range(l)]
#     return ls
#
# print(create_list(10))

# @measure_memory_usage
# def calculate_factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * calculate_factorial(n - 1)
# n = 8
# print(f"Factorial of {n}: {calculate_factorial(n)}")


# cache simulator

# def cache_result(func):
#     cache = {}
#     def wrapper(*args, **kwargs):
#         key = (*args, *kwargs.items())
#
#         if key in cache:
#             print("Retrieving result from cache...")
#             return cache[key]
#
#         result = func(*args, **kwargs)
#         cache[key] = result
#         return result
#     return wrapper
#
# @cache_result
# def calculate_multiply(x, y):
#     print("Calculating the product of two numbers...")
#     return x * y
#
# print(calculate_multiply(4, 5))
# print(calculate_multiply(5, 5))
# print(calculate_multiply(4, 5))
# print(calculate_multiply(4, 5))
# print(calculate_multiply(4, 9))
# print(calculate_multiply(4, 50))
# print(calculate_multiply(5, 5))
# from datetime import datetime
# # logger
# def log_decor(func):
#     def wrap(*args, **kwargs):
#         print(f"{datetime.now()}: Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"{datetime.now()}: {func.__name__} returned th following value: {result}")
#         return result
#     return wrap
#
# @log_decor
# def calculate_multiply(x, y):
#     print("Calculating the product of two numbers...")
#     return x * y
#
# print(calculate_multiply(3, 8))


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# p1 = Point(3, 4)
# print(p1.x)
# p1.y = 8
# print(p1.__dict__)
# p1.z = 7
# print(p1.z)
# print(p1.__dict__)
#
# class Point2D:
#     __slots__ = ("x", "y")
#     # z = 8
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# p2 = Point2D(3, 8)
# print(p2.x)
# p2.y = 5
# print(p2.y)
# print(p2.__dict__)
# print(p2.z)
# Point2D.z = 20

# print(p1.__dict__.__sizeof__())
# print(p2.__sizeof__())
# print(dir(p2))



class Point2D:
    __slots__ = ("x", "y")
    # z = 8
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point3D(Point2D):
    # __slots__ = "z",
    def __init__(self, x, y, z):
        self.z = z

p3 = Point3D(3, 4, 7)
# print(p3.__dict__)
p3.x = 9
# print(p3.__dict__)
print(p3.z)
p3.a = 4
print(p3.__dict__)