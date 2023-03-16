import glob
""" returns a list of files or folders that matches
 the path specified in the pathname argument.
"""
myfiles=glob.glob("files/*.txt")
print(myfiles)
for files in myfiles:
    with open(files,"r") as file:
        print(file.read())



