import StateOfwater as s
print(__name__)  #function name
wt=int(input("Enter water temperature:"))
state=s.State(wt)
print(state)
