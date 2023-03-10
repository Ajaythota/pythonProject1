fb=int(input(" enter the count of fibonacci numbers:"))
n1,n2=0,1
print("fibonacci seed numbers",n1,n2,end=" ")  #end=" " is identified by white not new line
for i in range(2,fb):
    n3=n1+n2
    n1,n2=n2,n3
    print(n3,end=" ")
print()


