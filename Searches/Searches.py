list = [1,2,3,4,5,6,7,8,9,10]
item = int(input("what do you want to find? "))


def linearsearch(list, item):
    for i in range(len(list)):
        if list[i] == item:
            return True, i
    
    return False, None


success, location = linearsearch(list,item)

print(success,location)



def binarysearch(list, item):
    left = 0
    right = len(list) - 1
    while left < right:
        middle = right + left // 2
        if list[middle] == item:
            return True, middle
        elif list[middle] > item:
            right = middle - 1
        else:
            left = middle + 1
    return False, None


success2, location2 = binarysearch(list, item)

print(success2, location2)
