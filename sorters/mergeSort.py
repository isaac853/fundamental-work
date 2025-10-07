import random
data = [random.randint(0,100) for i in range(11)]
print(data)

def mergesort(data):
    if len(data) == 1:
        return data
    
    
    else:

        middle = len(data)//2
        left = mergesort(data[:middle])
        right = mergesort(data[middle:])
        newlist = []

        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                newlist.append(left.pop(0))

            else:
                newlist.append(right.pop(0))



        if len(left) != 0:
            newlist += left
        else:
            newlist += right
        return newlist


print(mergesort(data))