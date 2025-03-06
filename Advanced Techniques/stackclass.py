#take size as a parameter
#it should have a data atriboute whch will be an array set to the size given
#should have a top pointer attribute




class Stack:
    def __init__(self,size):
        self.topPointer = -1
        self.data = ["-" for i in range(size)]

    def push(self, data):
        if self.topPointer:
            pass

    def pop(self):
        pass

    def inspect(self):
        pass
stack = Stack(5)

print(stack.data)