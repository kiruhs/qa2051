#Caesar cipher

# import string
# shift = 3
# template = string.ascii_letters
# print(template)
# def rotate_chr(c, rot_by):
#     """ This function encrypts the given string by Caesar cipher with given key (shift)
# It was developed by group 2051
# """
#
#
#     # rot_by = 3
# #    c = c.lower()
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     # keep punctuation and whitespaces
#     if c not in alphabet:
#         return chr(ord(c) + 4)
#     rotated_pos = ord(c) + rot_by
#     if rotated_pos <= ord(alphabet[-1]):
#         return chr(rotated_pos)
#     return chr(rotated_pos - len(alphabet)) # + rot_by) - not needed
#
# encrypt = "".join(map(lambda s: rotate_chr(s, shift), "My Secret message Goes here."))
# print(encrypt)

# def decrypt_chr(c, rot_by):
#     # rot_by = 3
# #    c = c.lower()
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     # keep punctuation and whitespaces
#     if c not in alphabet:
#         return chr(ord(c) - 4)
#     rotated_pos = ord(c) - rot_by
#     if rotated_pos >= ord(alphabet[0]):
#         return chr(rotated_pos)
#     return chr(rotated_pos + len(alphabet))
#
# print("".join(map(lambda s: decrypt_chr(s, shift), encrypt)))

# help(rotate_chr)

# exceptions

# while True:
#     try:
#         x = int(input("Enter a number: "))
#         print(x + 5)
#         print("Hello world!")
#         break
#     except ValueError as e:
#         print(e)

# try:
#     with open("test5.json") as f:
#         x = f.read()
#         print(x)
# except FileNotFoundError as err:
#     print(err)
    # print("Are you crazy? There is no such file")

# def division(x, y):
#     try:
#         res = x / y
#         print(res)
#     # except Exception as e: # not recommended
#     #     print(e)
#
#     # except ZeroDivisionError as z:
#     #     print(z)
#     # except TypeError as t:
#     #     print(t)
#
#     except (ZeroDivisionError, TypeError) as e:
#         print(e)
#
# try:
#     division(4, 2)
#     division(6, -3)
#     # division(7, 2, 4)
#     # division(4)
#     division(7, "0")
#     division(7, 0)
#     division(4, [4, 5])
#     print("hello, world!")
# except TypeError as te:
#     print(te)
#
# else:
#     print("main module is completed without errors")
#
# print("The program continues its running")

# import json

# def load_and_parse(filename, key):
#     try:
#         with open(filename) as f:
#             data = json.load(f)
#         try:
#             value = data[key]
#             # print(value)
#             return value
#         except KeyError:
#             print(f"Error: key '{key}' not found in this data")
#     except FileNotFoundError:
#         print(f"Error: file {filename} does not exists")
#     finally:
#         print("this log will be printed anyway")
#
# print(load_and_parse("new.json", "name2"))
# print("program continues")

# try:
#     try:
#         x = int(input("Enter the temperature value between 20 and 50 degrees: "))
#     except ValueError as er:
#         print(er)
#     else:
#         if x < 20 or x > 50:
#             raise ValueError ("You have entered invalid temperature value")
#         print("Good guy. You entered the valid temperature")
#         print(x)
# except ValueError as e:
#     print(e)

# words = {}
# try:
#     while True:
#         s = input("Enter a word: ")
#         if s in words:
#             print(f"Word {s} is translated to {words[s]}")
#         else:
#             print(f"Type the translation to russian for {s}: ")
#             words[s] = input()
# except KeyboardInterrupt:
#     print("Good bye!")
#     print(words)

# try:
#     f = open("0_euro.txt", encoding="utf-8") # , errors="ignore")
#     txt = f.read()
#     print(txt)
# except UnicodeDecodeError as e:
#     print(e)
# help(UnicodeDecodeError)
# print(UnicodeDecodeError.__mro__)

# iterators and generators

# st = {"hello", 3, 6, 7, "h", 'c', (1,2,3), False}
# for i in st:
#     print(i)

# x = 5
# for i in x:
#     print(i)

# d = [5, 3, 7, 10, 32]
# d = "python"
# r = range(5)
# it = iter(d)
# print(it)
# print(d.__sizeof__())
# print(it.__sizeof__())
# for i in r:
#     print(next(it))
# print("n" in it)
# print("y" in it)
# print("h" in it)
# print("o" in it)
# print("n" in it)
# it = iter(d)
# print("h" in it)
# it = iter(d)
# print("h" in it)
# print(next(it))
# next(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# def get_list():
#     for x in [1, 2, 3, 4]:
#         yield x
#
# a = get_list()
# print(a)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# lst = [1, 2 ,3]
# next(iter(lst))


print(dir(filter))