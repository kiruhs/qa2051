# file handling

# f = open("test01.txt", 'r') # r, w, a, r+, w+, a+
# print(f.read()) # by default all symbols of the file, or number that set in parentheses

# for each in f:
#     print(each, end="")
#
# f.close()
# lst = []
# with open("test01.txt", 'r') as f:
    # print(f.read()) # read until EOF end of file
    # f.seek(0) # move file descriptor to position 0 or for your choice
    # for _ in range(2):
    #     print(f.readline(), end="") # one line only
    #     # print(f.readline())
    # txt = f.readlines()
    # for each in f:
    #     lst.append(each)
        # print(each)
    # print(f.tell()) # describes the current descriptor position
# f.read()   # your object f is currently closed and is not visible for Python
# print(lst)
# print(txt)


# with open("out.txt", 'w') as file:
#     file.write("Hello4\n")
    # file.write("Hello5\n")
    # file.write("Hello6")

# l = ["This is New York\n", "This is Paris\n", "This is London\n"]
#
# with open("cities.txt", 'a+') as cap:
#     cap.writelines(l)
#     cap.seek(0)
#     c = cap.read()
#
# for i in c.split("\n"):
#     print(i)
# with open("out1.txt", 'r+') as file:
#     file.seek(5)
#     file.write("Hello14\n")
#     file.write("Hello15\n")
#     # file.write("Hello13\n")
#     file.seek(0)
#     print(file.read())


# interactive vocabulary saved into file

# words = {}
# with open("vocabulary.txt", 'a+', encoding='utf8') as file:
#     file.seek(0)
#     lst = file.readlines()
#     for i in lst:
#         k, v = i [:-1].split(":")
#         words.update({k: v})
#
# print(lst)
# print(words)
# print("This is the interactive dictionary, that you create yourself\n"
#       "just enter a word... (for exit input 'q' button)")
#
# while True:
#     w = input()
#     if w == 'q':
#         break
#     valid = True
#
#     for ch in w:
#         code = ord(ch)
#         if not (65 <= code <= 90 or 97 <= code <= 122):
#             valid = False
#             break
#     if not valid:
#         break
#     if w in words:
#         print(f"word {w} is translated as {words[w]}")
#     else:
#         with open("vocabulary.txt", 'a+', encoding="utf8") as file:
#             words[w] = input("Input the translation in Russian: ")
#             file.write(f"{w}: {words[w]}\n")
#     print("enter a word... ")

from pathlib import Path

# directory = Path("c:/tmp")
# print(type(directory))
# print(directory.is_file())

# create iterator by folder content

# dir_iter = directory.iterdir()
# print(dir_iter)
# text = []
# for path in dir_iter:
#     # print(path)
#     if path.is_file() and path.suffix == ".csv":
#         text.append(path.read_text())
#
# for txt in text:
#     print(txt)


# JSON files
import json

# with open("test.json") as jf:
#     data = json.load(jf)
    # print(data)
    # print(data[0]["fields"]["name"])
    # for i in data:
    #     print(i["fields"]["abbrevation"])


# dct = {
#     "name": "Ford",
#     "Model": ["Fiesta", "Edge", "Mustang"],
#     "year" : 2023,
#     "owner": {
#         "Las_name": "Smith",
#         "First_name": "John",
#         "City": "New York"
#     }
# }

# print(type(dct))
# # convert to JSON
# j_data = json.dumps(dct)
# print(j_data)
# print(type(j_data))
# with open("new.json", "a+") as file:
#     file.write(j_data)

# with open("new.json") as file:
#     new_json = json.load(file)
#
# print(type(new_json))


import os
# os.system("notepad") # call to system program
# os.mkdir("c:/tmp/new")

# lst = os.listdir("c:/tmp")
# for i in lst:
#     print(i)
# print(os.getcwd())

# os.system("dir")

# print(os.popen("dir /B *.py").read())

pipe = os.popen("ping 10.8.8.8")
pull = pipe.read()

cnt = 0

for i in pull.split():
    if i == "Reply":
        cnt += 1

if cnt == 4:
    print("Ping answered fully")