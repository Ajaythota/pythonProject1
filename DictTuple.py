dictTpl={('a','b'):[1]}
for a,b in dictTpl:
    print(a,b,dictTpl['a','b'][0])

dict={('John','Smith'):[77777777],('A','B'):[8888888]}
for key ,value in dict.items():
    print(f"{key[0]} {key[1]}: {value[0]}")


pb={'Name':['John','Sally','David'],'age':[23,28,40],'phone':[11111,22222,33333]}
for name,age,phone in zip(pb['Name'],pb['age'],pb['phone']):
    print(f"{name}-{age}-{phone}")