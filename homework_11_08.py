# def valid_decorator(func):
#     def wrapper(num, *args, **kwargs):
#         if not isinstance(num, int):
#             raise TypeError("Entered number must be an integer")
#         elif num < 0:
#             raise ValueError("Entered number must be positive")
#         res = func(num, *args, **kwargs)
#         return res
#     return wrapper
#
# @valid_decorator
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial("hello"))
from unicodedata import digit

num = 1633
# def armstrong_num(n):
#     # return sum(int(digit)**len(str(n)) for digit in str(n)) == num
#     res = 0
#     if n <= 0:
#         return ValueError("Entered number must be positive")
#     st = str(n)
#     for i in st:
#         res += int(i) ** len(st)
#     return res == n
#
# # print(armstrong_num(num))
#
# arm = [i for i in range(10, 10000)]
# # print(arm)
# print(*filter(armstrong_num, arm))

def isArmstrong(n):
    s = n
    l = len(str(n))
    sm = 0
    while n != 0:
        r = n%10
        sm += r**l
        n //= 10
    return sm == s

arm = [i for i in range(10, 10000)]
# print(arm)
print(*filter(isArmstrong, arm))
