#exercise 1
#file=open("files\essay.txt",'r')
#line=file.readline()
#print(f"print the line with Caps:  {line.title()}")
#readLines returns list , readline/read return string

#exercise 2
#print(f"num of character in the file:{len(line)}")
#file.close()

#exercise 3
# fileR=open("files/members.txt",'r')
# list=fileR.readlines()
# fileR.close()
# user_input=input("Add a new member:") +"\n"
# list.append(user_input)
# fileW=open("files/members.txt",'w')
# fileW.writelines(list)
# fileW.close()

#exercise 4
# review examplefileCreateZip

#excercise 5
filenames=["a.txt","b.txt","c.txt"]
for files in filenames:
    file=open(f"files/{files}",'r')
    content=file.read()
    print(content)
    file.close()
