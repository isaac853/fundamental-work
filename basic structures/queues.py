def displayQueue():
    print("front", front)
    print("rear", rear)
    print("------")
    for index,data in enumerate(queue):
        print(index, ":", data )

def enqueue(data):
    global rear,maxsize,queue

    if rear != maxsize - 1:
        rear += 1
        queue[rear] = data

    else:
        print( "\n""queue is full.""\n")
    
def dequeue():
    global front,rear, queue
    if front == rear:
        print("queue is empty")
    else:
        front += 1
        return queue[front]
        


maxsize = 10
queue = ["-" for i in range(maxsize)] #will make a list of 10 "-"
front = -1
rear = -1

displayQueue()
for i in range(12):
    enqueue("3")

displayQueue()

for i in range(13):
    dequeue()

displayQueue()

enqueue("olly is the root of variance")