import numpy as np
arr=np.array([[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,9,2,-4,-4,0],[0,0,0,-2,0,0],[0,0,-1,-2,-4,0]])
print(arr)
arr1=[]

for i in range(4):
    for j in range(4):
        l1=arr[i][j]+arr[i][j+1]+arr[i][j+2]
        l2=arr[i+1][j+1]
        l3=arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
        arr1.append(l1+l2+l3)

print(arr1)
arr2=np.array(arr1)
print(type(arr2))
print(arr2)
print(arr2.sum())