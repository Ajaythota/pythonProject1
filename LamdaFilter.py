
result= lambda a:a if(a%3 ==0 and a%5 ==0) else 'not divisble'
print(result(40))

list1 = [2, 4, 9, 15, 20, 24, 29]
def even(num):
    if num % 2 == 0:
        return True
res = list(filter(even, list1))
print(res)

list1=[2,4,9,15,20,24,29]
even= lambda list2:list2 if (list2%2==0) else""
res=list(filter(even,list1))
print(res)

#map
list1=[2,5,7,9]
def addTen(x):
    x=x+10
    return x
res=list(map(addTen,list1))
print(res)

#reduce
from functools import reduce
list3=[3,4,5,6,0]
print(reduce(lambda x,y:x+y,list3))

list4=[4,6]
print(reduce(lambda x,y:x if(x >y) else y, list4))