#Difference sort and sorted

print(__name__) #display the name of the function

n=[6,1,4,10,-2,0,345,15]
s=sorted(n) #sorted sorts the orig list and returns a  new list
print(s)
print(n) #original list in tact

n=[6,1,4,10,-2,0,345,15]
n.sort() # sorts the list but returns none
print(n) #original list changed

#bubble sort
b=[6,1,4,10,-2,0,345,15]
def bubbleSort(args):
    for i in range(len(args)):
        for j in range(0,len(args)-i-1):
            if(args[j]>args[j+1]):
              # args[j],args[j+1]=args[j],args[j+1]
                temp=args[j]
                args[j]=args[j+1]
                args[j+1]=temp

    print("aaa")
    print(args)

bubbleSort(b)