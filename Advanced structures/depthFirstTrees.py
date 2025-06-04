import random

def postOrder(root):
    global binaryTree
    currentNode = binaryTree[root]
    # print(currentNode)
    if currentNode["left"] != None:
        postOrder(currentNode["left"])

    if currentNode["right"] != None:
        postOrder(currentNode["right"])

    print(root)


binaryTree = {
    "A":{"left" : "B", "right" : "C"},
    "B":{"left" : "D", "right" : "E"},
    "C":{"left" : "I", "right" : "J"},
    "D":{"left" : "F", "right" : None},
    "E":{"left" : "G", "right" : "H"},
    "F":{"left" : None, "right" : None},
    "G":{"left" : None, "right" : None},
    "H":{"left" : None, "right" : None},
    "I":{"left" : None, "right" : None},
    "J":{"left" : "K", "right" : "L"},
    "K":{"left" : None, "right" : None},
    "L":{"left" : None, "right" : None}}
#postOrder("A")

bst = [
{"left":None, "right":None,"data":None},
{"left":None, "right":None,"data":None},
{"left":None, "right":None,"data":None},
{"left":None, "right":None,"data":None},
{"left":None, "right":None,"data":None},
{"left":None, "right":None,"data":None},
{"left":None, "right":None,"data":None},
{"left":None, "right":None,"data":None},
{"left":None, "right":None,"data":None},
]

class Node:
    
    def __init__(self, givendata):
        self.data = givendata
        self.left = None
        self.right = None


    def displaydata(self):
        return [self.data, self.left, self.right]
    
    
    def setdata(self, givendata2):
        self.data = givendata2

    def addconnections(self, data, left: bool):
        if left:
            self.left = data
        else:
            self.right = data


class Tree:

    def __init__(self):
        self.bst = []
        self.nextfree = 0

    def addNode(self,givendata):
        
        if len(self.bst) == 0:
            self.bst.append(Node(givendata))
            
            
        currentNode = self.bst[self.nextfree]
    
        if len(self.bst) != 0:
            while True:
                if currentNode.displaydata()[0] >= givendata:
                    if currentNode.displaydata()[1] == None:
                        
                        self.bst.append(Node(givendata))
                        currentNode.addconnections(self.nextfree, True)
                        self.nextfree += 1
                        break

                    else:
                        currentNode = self.bst[currentNode.displaydata()[1]]
                        continue

                if currentNode.displaydata()[0] <= givendata:
                    if currentNode.displaydata()[2] == None:
                        
                        self.bst.append(Node(givendata))
                        currentNode.addconnections(self.nextfree, True)
                        self.nextfree += 1
                        break

                    else:
                        currentNode = self.bst[currentNode.displaydata()[2]]
                        continue

    def search(self, data):
        pass

    def displaytreePostOrder(self,rootlocation):
        if len(self.bst) == 0:
            print("ts empty")
        
        else:
            currentNode = self.bst[rootlocation]
            if currentNode.displaydata()[1] != None:
                self.displaytreePostOrder(currentNode.displaydata()[1])
            
            if currentNode.displaydata()[2] != None:
                self.displaytreePostOrder(currentNode.displaydata()[2])
            
            print(currentNode.displaydata[0])


        

mytree = Tree()

for i in range(10):
    mytree.addNode(random.randint(1,100))

mytree.displaytreePostOrder(0)