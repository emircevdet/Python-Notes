import os
import time
from datetime import date

# getcwd()
print(os.getcwd())

# listdir()
print(os.listdir())

# chdir() --> /
os.chdir("C:/Users/yusuf/Documents/Python")
print(os.getcwd()) # approve change

print(os.listdir())
print(type(os.listdir()))
for file in os.listdir():
    print(file)

# mkdir() --> creates only one directory
os.mkdir("test-1") # doesn't run in the second
print(os.listdir())
os.mkdir("test-1/test-2")
print(os.listdir("C:/Users/yusuf/Documents/Python/test-1"))
os.mkdir("test-1/test-2/test-3/test-4") # doesn't work

# makedirs() --> creates a directory recursively even intermediate dir is miss.
os.makedirs("test-1/test-2/test-3/test-4")

# search for differences of mkdir & makedirs on:
# https://www.w3schools.com/python/module_os.asp

# rmdir() --> removes directory if it is empty
os.rmdir("test-1") # doesn't run as it isn't empty
os.rmdir("test-1/test-2/test-3/test-4") # runs at once

# removedirs() --> removes dirs sequentially
os.removedirs("test-1/test-2/test-3")

# remove() --> is used to remove a file path, not any directory
os.mkdir("test-1")
os.remove("test-1/text.txt")

# rename()
os.rename("test-1", "test-10")
os.rename("test-10/text.txt", "test-10/txt.txt")

# stat()
print(os.stat("test-10/txt.txt").st_birthtime)
print(date.fromtimestamp(os.stat("test-10/txt.txt").st_atime))
print(os.stat("test-10/txt.txt").st_size) # byte in size

# walk()
for curr, folders, files in os.walk("C:/Users/yusuf/Documents/Python/2425-2"):
    print("Current Folder: ", curr)
    print("Folders: ", folders)
    print("Files: ", files)
    print()

# path
print(os.path.join("test1", "test2", "test3","text.txt"))
print(os.path.isfile("C:/Users/yusuf/Documents/Python/test-10"))
print(os.path.isfile("C:/Users/yusuf/Documents/Python/test-10/txt.txt"))
print(os.path.isdir("C:/Users/yusuf/Documents/Python/test-10/txt.txt"))
print(os.path.isdir("C:/Users/yusuf/Documents/Python/test-10"))
print(os.path.splitext("C:/Users/yusuf/Documents/Python/test-10/txt.txt"))

# # os.path --> https://docs.python.org/3/library/os.path.html

# time() --> float
time1 = time.time()
print(type(time1))
print(time1)

# # to evaluate computation time
# start = time.time()
# my_list = []
# for i in range(100000):
#     my_list.append(i)
# end = time.time()
# print(end - start)

# ctime() --> str
time2 = time.ctime()
print(type(time2))
print(time2)

# localtime() --> time.struct_time
time3 = time.localtime()
print(type(time3))
print(time3)

print(time3.tm_year)
print(time3.tm_mon)
print(time3.tm_mday)

# strftime()
time4 = time.strftime("%d/%m/%Y - %H:%M %p")
print(type(time4))
print(time4)

# # sleep()
# print("This is printed immediately.")
# time.sleep(3)
# print("This is printed 3 seconds later...")

# datetime methods and properties
bugun = date.today()
print(bugun)
print(type(bugun))
print(bugun.year)
print(bugun.month)
print(bugun.day)
print(bugun.weekday())
print(bugun.isoweekday())

# gecmis_tarih = date(1970, 1, 1)
# print(bugun - gecmis_tarih)
# print((bugun - gecmis_tarih).days)

# print(bugun.strftime("%d-%m-%Y %A"))