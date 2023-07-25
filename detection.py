import os

path = "C:\\Users\\Robbievans\\Desktop\\test"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("this is a file")
    elif os.path.isdir(path):
        print("that is a directory")
else:
    print("Location does not exist")