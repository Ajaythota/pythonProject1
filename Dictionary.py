#string as keys
emp={'Name':['John','Sally','David'],'age':[23,28,40],'company':"ABC"}
print(emp)
print(emp['Name'])

for key in emp:
    print(f"{key}:{emp[key]}")

print(emp['company'])
print(emp['Name'][0])
emp['Name'][0]='George' # update - dict values are mutable
print(emp['Name'][0])
emp['Name']=['George','Peter','Paul']# can add new list
emp['phone']='7328888'# can add a new item
print(emp)
del(emp['phone']) # can delete existing items
print(emp)

dictNum={1:"one",2:"two"} #can use numbers as  keys
print(dictNum)

#dictionary with zip- zip returns object. need to convert to list
pb={'Name':['John','Sally','David'],'age':[23,28,40],'phone':[11111,22222,33333]}
#for name,age,phone in zip(pb['Name'],pb['age'],pb['phone']):
  #  print(f"{name}-{age}-{phone}")
zip1=zip(pb['Name'],pb['age'],pb['phone'])
zip1=list(zip1)
for name,age,phone in zip1:
    print(f"{name}-{age}-{phone}")
#unzip
listA,listB,listC=zip(*zip1)
print(listA)
print(listB)
print(listC)


#tuple in dictionary - see DictTuple.py