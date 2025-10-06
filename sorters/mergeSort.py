import random
data = [random.randint(0,100) for i in range(11)]
print(data)

def mergesort(data):
    if len(data) > 1:
        middle = len(data)//2
        left = mergesort(data[:middle])
        right = mergesort(data[middle:])
        newlist = []
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                newlist.append(left[0])
                del left[0]
            else:
                newlist.append(right[0])
                del right[0]

        if len(left) != 0:
            newlist.append(left)
        else:
            newlist.append(right)
        return newlist
    else:
        return data

print(mergesort(data))