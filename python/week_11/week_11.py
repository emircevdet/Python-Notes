# open/close - with open
# read() - write() - readlines() - readline()
# tell() - seek()
# "r", "w", "a", "rb", "wb"
# copy-paste (nested with open)

# READ without using with open
f = open("file.txt", "r") # returns error if not exist (default "r")
content = f.read()
print(content)
f.close()
# new_content = f.read() # can't read after closing it unless you open it again

f = open("file2.txt", "w")
f.write("file2 is opened and modified.")
f.close()

f = open("file2.txt")
content = f.read()
print(content)
f.close()

# READ using with open
with open("file.txt", "r") as f: # default "r"
    content = f.read()
    print(content)
# new_content = f.read() # file already closed

with open("file.txt", "r") as f:
    content = f.readlines() # readlines()
    print(content)
    for line in content:
        print(line) # end=""

for i in range(10):
    print(i, end="") # end=""
print()

with open("file.txt") as f: # to read line by line and assign each line to list
    for line in f:
        print(line, end="")
print()

with open("file.txt") as f:
    content = f.readline() # readline()
    print(content, end="")
    # content = f.readline()
    # print(content, end="")
    # content = f.readline()
    # print(content, end="")
    cur_pos = f.tell() # tell() --> tell cursor position
    print(cur_pos)
    f.seek(0) # seek() --> send cursor and position
    content = f.readline()
    f.seek(0)
    content = f.read(10) # to read by part from huge data
    print(content, end="")
    content = f.read(10) # but this is inefficient
    print(content, end="")
    content = f.read(10) # but this is inefficient
    print(content, end="")
    print()

# read batch in an efficient way
with open("file.txt") as f:
    line_to_read = 10
    content = f.read(line_to_read)
    while len(content) > 0:
        print(content, end="")
        content = f.read(line_to_read) # to replace with new content

# WRITE
with open("file3.txt", "w") as f: # file is created if not exist
    f.write("INF382") # write "Python"

# APPEND
with open("file3.txt", "a") as f:
    f.write("-Python")

# COPY FILE.TXT and PASTE IT INTO FILE3.TXT
with open("file.txt") as fr:
    with open("file3.txt", "w") as fw:
        for line in fr:
            fw.write(line)
        # content = fr.readlines() # equivalent of above
        # for line in content:
        #     fw.write(line)

# PNG COPY PASTE "rb" --> "wb"
with open("image.png", "rb") as fr:
    with open("image2.png", "wb") as fw:
        to_read = 1024
        content = fr.read(to_read)
        while len(content) > 0:
            fw.write(content)
            content = fr.read(to_read)

