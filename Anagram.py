
str1="apple"
s1=sorted(str1.casefold())
#print(s1)
str2="Alpep"
s2=sorted(str2.casefold())
#print(s2)
if(s1==s2):
    print("Anagram")
else:
    print("Not an Anagram")