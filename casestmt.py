
todos=[]

while True:
     action = input("choose add, show ,edit,remove or exit:")
     match action:
         case 'add':
             todo=input("enter todo:")
             todos.append(todo)
         case 'show':
             for index,items in enumerate(todos): ## enumerate
                 #items=items.capitalize()
                 #print(index,items.capitalize())
                 row=f"{index}-{items.capitalize()}"  ## f string
                 print(row)
         case 'edit':
              edit_num=int(input("input the list item to edit"))
              edit_num=edit_num-1
              edit_value=input(" input new value ")
              todos[int(edit_num)]= edit_value
              #todos.__setitem__(edit_num, edit_value)
         case 'remove':
              rm=input("enter the character to remove")
              todos.remove(rm)

         case 'exit':
             break
         case _:
             print(' type a valid entry')


#for loop for a string
#for L in 'loop': // will print individual characters of that string
   # print(L)






