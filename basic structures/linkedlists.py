# linked lists

start = 0
nextfree = 7

linkedList = [
    {"data" : "ocean", "pointer": 1},
    {"data" : "fish", "pointer": 2},
    {"data" : "gold", "pointer": 3},
    {"data" : "silver", "pointer": 4},
    {"data" : "metal", "pointer": 5},
    {"data" : "heavy", "pointer": 6},
    {"data" : "light", "pointer": None},
    {"data" : "-", "pointer": 8},
    {"data" : "-", "pointer": 9},
    {"data" : "-", "pointer": None},
]

def traverseList():
    # go to each item in the list in order and output the data

    if next != None:
        currentpointer = start

        while currentpointer != None:
            print(linkedList[currentpointer]["data"])
            currentpointer = linkedList[currentpointer]["pointer"]

    else:
        print("the list is empty")

print(traverseList())

def find(term):
    #return True when item is find
    #return false if all items checked and item not found

    currentpointer = start

    while currentpointer != None:

        if linkedList[currentpointer]["data"] == term:
            return True

        currentpointer = linkedList[currentpointer]["pointer"]

    return False




def insert(position, term): 
    global nextfree, start

    #to insert it at the start
    if position == 0 and nextfree != None: 

        #set the next spot's data to the input
        linkedList[nextfree]["data"] = term
        #store the next nextfree pointer in temp
        temp = linkedList[nextfree]["pointer"]
        linkedList[nextfree]["pointer"] = start
        start = nextfree
        nextfree = temp

    #insert the item anywhere in the middle of the list
    else: #look at this again
        
        currentpointer = start
        count = 0

        while currentpointer != None and count < position -1:
            count += 1
            currentpointer = linkedList[currentpointer]["pointer"]

        temp = linkedList[currentpointer]["pointer"]
        linkedList[currentpointer]["pointer"] = nextfree
        linkedList[nextfree]["data"] = term
        nextfree = linkedList[nextfree]["pointer"]
        linkedList # replace pinter of new item to temp
    




print("")
insert(0,"geo")
traverseList()


print("")
insert(0,"list")
traverseList()





