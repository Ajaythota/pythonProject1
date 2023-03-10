#Variable length  agruments *args & *kwArgs

#*Args
def sum(*args):
    i=0
    for j in args:
        i=i+j
    return i
def name(*args):
    str1=''
    for i in args:
        str1=str1+i
    return str1

list1=['x','y','z'] #list
tpl1=(100,200,300,400,500)

print(sum(10,20))
print(sum(-5,-6,1,5))
print(sum(100))
print(name('a','b','c'))
print(name(*list1))
print(sum(*tpl1))

#*KwArgs
def emp(**kwargs):
    str1=''
    for key,value in kwargs.items():
        str1=str1+(f" {key}={value} ")
    return str1

dict={"first":'A',"middle":'B',"last":'C',"age":40}

print(emp(first='A',middle='B',last='C'))
print(emp(**dict))

