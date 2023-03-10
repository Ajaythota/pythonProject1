FREEZING_POINT=0
BOLING_POINT=100
print(__name__)  #function name

def State(temp):
    if(temp<=FREEZING_POINT):
        return "Solid"
    elif(temp >FREEZING_POINT and temp <=BOLING_POINT):
        return "Liquid"
    else:
        return "Gas"


