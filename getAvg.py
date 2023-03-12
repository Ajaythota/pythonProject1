def get_average():
    """
    Get average of the values after reading the file
    :return:
    """
    with open("files/Temp",'r') as file:
        data=file.readlines()
        values=data[1:]
        values=[float(i) for i in values]
        avg=sum(values)/len(values)
        return avg


average=get_average()
print(average)
print(get_average.__doc__)

