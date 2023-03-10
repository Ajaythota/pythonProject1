title= input("enter the title:") # input value is always a 'str' datatype
if(len(title)) < 20:
    print("Length of the title:",len(title))
else:
    print("Title too long")