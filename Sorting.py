wait_list=["John","john","Adam","Kathy"]
wait_list.sort()
print(wait_list)
for index, item in enumerate(wait_list):
     row=f"{index+1}-{item}"
     print(row)