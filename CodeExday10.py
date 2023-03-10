#try except  code
#exercise 1
print("----exercise 1 \n")
while True:
    try:
        t=float(input("enter total value:"))
        if(t>0):
            v=float(input("enter value:"))
            p=v*100/t
            print(f"that is {p}%")
            break
        else:
            print("your total value cannot be zero")
            continue
    except ValueError:
        print("you need to enter a number")
        continue

print("----exercise 2 \n")

while True:
    try:
        t=float(input("enter total value:"))
        v=float(input("enter value:"))
        p=v*100/t
        print(f"that is {p}%")
        break

    except ZeroDivisionError:
        print("your total value cannot be zero")
        continue
    except:
        print("you need to enter a number")
        continue