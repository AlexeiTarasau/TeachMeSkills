import os

os.mkdir("mydir")

os.chdir("mydir")

open("file1.txt", "w").close()
open("file2.txt", "w").close()
open("file3.txt", "w").close()

file_list = os.listdir()
print("List of files in a directory mydir: ")
for file in file_list:
    print(file)
