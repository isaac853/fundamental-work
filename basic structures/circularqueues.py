def displayQueue():
    print("front", front)
    print("rear", rear)
    print("------")
    for index,data in enumerate(queue):
        print(index, ":", data )

def enqueue(data):
    global rear, maxsize, queue, front

    if (rear + 1) % maxsize == front:
        print( "\n""queue is full.""\n")
    

    else:
        if front == -1:
            front = 0
            
        rear = (rear + 1) % maxsize
        queue[rear] = data
    
def dequeue():
    global front, rear, queue, maxsize

    if front == -1:
        print("queue is empty")

    else:
        temp = queue[front]
        if front == rear: 
            front = -1
            rear = -1
        else:
            front = (front + 1) % maxsize
        return temp
        
#initialise queue
maxsize = 10
queue = ["-" for i in range(maxsize)] #will make a list of 10 "-"
front = -1
rear = -1

for i in range(14):
    enqueue(3)
displayQueue()

for i in range(14):
    print(dequeue())
displayQueue()

for i in range(3):
    enqueue(i)

displayQueue()