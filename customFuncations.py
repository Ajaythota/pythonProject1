def get_todos():
    with open("data.txt", 'r') as file_r:
        todos_r = file_r.readlines()
    return todos_r

def write_file(todos):
    with open("data.txt", 'w') as file_w:
        file_w.writelines(todos)


while True:
     action = input("choose add, show ,edit,remove or exit:")
     todos=get_todos()
     print(todos)

     match action:
         case 'add':
             todo=input("enter todo:") +"\n"
             todos.append(todo)
             # file=open("data.txt" , 'w') #write to file as list and close
             # file.writelines(todos)
             # file.close()
             #with open("data.txt",'w')as file:
               #  file.writelines(todos)
             write_file(todos)


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

              #file = open("data.txt", 'w')  # write to file as list and close
              #file.writelines(todos)
              write_file(todos)
              #file.close()
         case 'remove':
              rm=int(input("enter the character to remove"))
              todos.pop(rm)
              write_file(todos)

         case 'exit':
             break
         case _:
             print(' type a valid entry')


#for loop for a string
#for L in 'loop': // will print individual characters of that string
   # print(L)