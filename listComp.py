#list comprehension
old=[1,2,3]
new=[i+10 for i in old]
print(new)
#list comprehension using if condition
list1=[3,5,7,15,25,30]
list2=[x for x in list1 if (x%3==0 and x%5==0)]
print(list2)
