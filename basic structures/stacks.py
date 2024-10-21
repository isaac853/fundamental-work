import os

def displayStack():
    print("top", top)
    print("------")
    for index,data in enumerate(stack):
        print(index, ":", data )

def push(data):
    global top
    if top < maxsize -1:
        top += 1
        stack[top] = data

    else:
        print("stack is full")

def pop():
    if top > -1:
        temp = stack[top]
        top -= 1
        return temp
    
    else:
        print("stack is empty")



# setting up the stack
maxsize = 10
stack = ["-" for i in range(maxsize)] #will make a list of 10 "-"
top = -1 # -1 is a common poiner used when nothing is in the stack. purely convention

# for i in range(11):
#     push(i)
# displayStack()


while True:

    os.system("clear")
    displayStack()

    options = ["push", "pop"]
    choice = input("push or pop? ")
    choice.lower
    if choice in options:
        if choice == "push":
            data = input("what do you want to push")
            push(data)
        else:
            print(pop())
            