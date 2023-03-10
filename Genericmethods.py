#setdefault
car ={'make':'Toyota','color':'beige','year':'1997'}
x=car.setdefault('color','white') # if exists returns the value
y=car.setdefault("model","camry") # is does not exist , inserts and returns the value
print(x)
print(y)
print(car)

#swap 2 numbers without a temp
a=20
b=30
a,b=b,a
print(a)
print(b)

#print concatenated string
vowels = ['a', 'e', 'i', 'o', 'u']
str1 = input("enter string")
str2 = ''
str3 = ''
for i in vowels:
     if i in str1:
          str2 = str2 + i
     else:
          str3 = str3 + i

print(str2)
print(str3)

#nested loops
x=[1,2,3]
y=['a','b','c']
for i in x:
    for j in y:
        print(i,j)