todos=[]
while True:
     action = input("choose add, show ,edit,remove or exit:")
     #file = open("data.txt", 'r')  # read from file as list and close
     #file=open(r"C:\Users\AjayThota\PycharmProjects\pythonProject1",'r')- absolute path
     #open(r--   suppress the special characters like \t etc.
     #todos = file.readlines()
     #file.close()

     #using the with command- context manager
     with open("data.txt",'r') as file:
         todos=file.readlines()

     match action:
         case 'add':
             todo=input("enter todo:") +"\n"
             todos.append(todo)
             # file=open("data.txt" , 'w') #write to file as list and close
             # file.writelines(todos)
             # file.close()
             with open("data.txt",'w')as file:
                 file.writelines(todos)


         case 'show':
             for index,items in enumerate(todos): ## enumerate
                 #items=items.capitalize()
                 #print(index,items.capitalize())
                 row=f"{index}-{items.capitalize()}"  ## f string
                 print(row)
         case 'edit':
              edit_num=int(input("input the list item to edit"))
              edit_num=edit_num-1
              edit_value=input(" input new value ") +"\n"
              todos[int(edit_num)]= edit_value

              file = open("data.txt", 'w')  # write to file as list and close
              file.writelines(todos)
              file.close()
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
