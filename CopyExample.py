#Assignment
list1=[1,2,['a','b','c']]
list2=list1
list1.append(['d'])
list2[1]=3
print(list1)
print(list2)

#Copy (shallow copy)
import copy
old=[3,4,['A','B','C']]
new=copy.copy(old)
old.append(['D','E','F'])
new[0]=5
print(old)
print(new)
#copy with updates to existing list
old[2][0]='AAA'
old[3][0]='DDD'
new[2][1]='BBB'
print(old)
print(new)

#Copy (deep copy)
old=[3,4,['A','B','C']]
new=copy.deepcopy(old)
old.append(['D','E','F'])
new[0]=5
print(old)
print(new)
#copy with updates to existing list
old[2][0]='AAA'
old[3][0]='DDD'
new[2][1]='BBB'
print(old)
print(new)