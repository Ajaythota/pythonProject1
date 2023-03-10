from collections import Counter

list1=['a','b','c','x','y','z','x','x','x','y','z']
tpl1=('a','b','c','x','y','z','x','x','x','y','z')
dict1={'x':4,'y':5,'z':10,'z':20,'x':6,'y':15}
str1="Python programming is fun"
dict2={'x':4,'y':-1,'z':-10}

#counter returns a dict sub class
dict=Counter(str1)
print(dict['m'])

c1=Counter(list1)
c2=Counter(tpl1)
c3=Counter(dict1)
c4=Counter(str1)
c5=Counter(dict2)

#empty counter
count_=Counter()
print(count_)
#update counter
count_.update("python")
print(count_)

#Arthimetic operations on counters
#negative values will NOT considered for calculations

print(c1)
print(c2)
print(c3) #returns only one value of 'z'
print(c4)

print(c1+c2)  #addition
print(c1-c3)  #substraction
print(c1&c4)  #intersection
print(c1|c2)   #union- max values from either counter
#negative values will NOT be  displayed in the counter
print(c1+c5)
print(c1.most_common())

#elements return keys with only positive values
element_=c5.elements()
for i in element_:
    print(i)