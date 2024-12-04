# 3 levels
def displayQueue():
    queueTitles = ["TOP","MID","LOW"]
    for title, queue in zip(queueTitles, priorityqueues):
        print(title)
        for row, item in enumerate(queue):
            print(row,item)
    
 
maxsize = 5

priorityqueues = [
    ["-" for i in range(maxsize)],
    ["-" for i in range(maxsize)],
    ["-" for i in range(maxsize)]]

fronts = [-1,-1,-1]
rears = [-1,-1,-1]

def isempty(priority) -> bool:
    global fronts, rears, priorityqueues
    if rears[priority - 1] == -1:
        return True
    return False

def dequeuelevel():
    if isempty(1) and isempty(2):
        return 3
    elif isempty(1):
        return 2
    return 1

def fullenqueue( prioritylevel: int, data):
    global fronts, rears, priorityqueues

    if (rears[prioritylevel -1 ]+1) % maxsize == fronts[prioritylevel - 1]:
        print( "\n""this queue is full.""\n")

    else:
        if fronts[prioritylevel -1] == -1:
            fronts[prioritylevel -1] = 0
            
        rears[prioritylevel -1 ] = (rears[prioritylevel -1 ] + 1) % maxsize
        priorityqueues[prioritylevel - 1] [rears[prioritylevel -1 ]] = data


def fulldequeue():
    global fronts, rears, priorityqueues

    priority = dequeuelevel()

    if rears[priority - 1] == -1:
        print("queue is empty")

    else:
        temp = priorityqueues[priority - 1][fronts[priority - 1]]
        if fronts[priority - 1] == rears[priority - 1]: 
            fronts[priority - 1] = -1
            rears[priority - 1] = -1
        else:
            fronts[priority - 1] = (fronts[priority - 1] + 1) % maxsize
        return temp
    
while True:

    inputlist1 = ["enqueue", "dequeue","d","e"]
    choice = input("enqueue or dequeue:  ")
    choice.lower()
    while choice not in inputlist1:
        print("try again")
        choice = input("enqueue or dequeue:  ")

    if choice == "d" or choice == "dequeue":
        print(fulldequeue())

    else:
        inputlist2 = [1,2,3]
        priority = input(" what is the priority, 1-3 with 1 being highest priority: ")
        while priority not in inputlist2:
            print("try again")
            priority = input(" what is the priority, 1-3 with 1 being highest priority: ")
        
        data = input("what is the case:  ")

        fullenqueue(priority, data)

    displayQueue()

    loopchoice = input("\n""y/n, do you want to add /remove another case?")
    while loopchoice not in ["y","n"]:
        print("invalid input")
        loopchoice = input("\n""y/n, do you want to add /remove another case? ")
    if loopchoice == "n":
        break
       