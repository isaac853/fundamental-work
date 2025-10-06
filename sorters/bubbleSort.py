data = [12314,22,1,24,64,9,37,12,-1,2302131,0]
isascending = True

def bubblesort(data: list, isascending: bool) -> list:
    sorted = False
    while sorted == False:
        sorted = True
        temp = 0

        if isascending:

            for i in range(len(data)-1):
                if data[i] > data[i + 1]:

                    temp = data[i+1]
                    data[i+1]=data[i]
                    data[i] = temp
                    sorted = False
                


        else:
            for i in range(len(data)-1):
                if data[i] < data[i +1]:
                    
                    temp = data[i+1]
                    data[i+1]=data[i]
                    data[i] = temp
                    sorted = False
        
    
    
    return data

# print(bubblesort(data, False))


def insertionsort(data: list, isascending: bool)-> list:
    # starting from 2nd item take each in turn
    #wihle the current item we're placing < the item to the left
    #and there are still items to the left
        #shuffle the left item
        #or swap the data with the one on the left
    temp = 0

    for i in range(1,len(data)):
        count = i 
        if isascending:
            while data[count] < data[count -1] and count != 0:
                temp = data[count]
                data[count] = data[count-1]
                data[count-1] = temp
                count -= 1 
        else: 
            while data[count] > data[count -1] and count != 0:
                temp = data[count]
                data[count] = data[count-1]
                data[count-1] = temp
                count -= 1 
    return data


print(insertionsort(data,False))