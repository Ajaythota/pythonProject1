#list comprehension
#exercise 1

names=["john smith","jay santi","eva  "]
new_names=[i.title() for i in names]
print(new_names)

#exercise 2
usernames = ["john 1990", "alberta1970", "magnola2000"]
l=[len(i) for i in usernames]
print(l)

user_entries = ['10', '19.1', '20']
f=[float(i) for i in user_entries]
print(f)