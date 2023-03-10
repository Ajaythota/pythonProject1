# list
filenames1=["test1.txt","test2.txt","text3.txt"]
for fileList in filenames1:
    print(fileList.replace("txt","pdf"))

filenames1[1]="test2222.txt"
print(filenames1) ## list mutable
#tuple
filenames2=("test1.txt","test2.txt","text3.txt") # round brackets for tuples
for filetuple in filenames2:
    print(filetuple.replace("txt","pdf"))
#filenames2[1]="test3333.txt"  # tuples not mutable


