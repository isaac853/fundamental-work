class Graph:
    def __init__(self):
        #a list of nodes and corresponding adjacencies, with the index being the letter of the node
        self.adjacencies = {
            "A":["B","C"],
            "B":["A"],
            "C":["A"],
            "D":[],
            "E":[]
        }

    def showAdjacencies(self, node):
        return self.adjacencies[node]
    
    def addEdge(self,startNode,endNode):
         """creates an edge between the two given nodes - if it doesn't already exist!"""
         if endNode in self.adjacencies[startNode]:
            print("edge already exists")

         else:
            self.adjacencies[startNode].append(endNode)
    
    def removeEdge(self, startNode, endNode):
        """removes the edge between the two given nodes - if it exists!"""
        if endNode not in self.adjacencies[startNode]:
            print("edge does not exist")

        else:
            self.adjacencies[startNode].remove(endNode)
                
    
    def addNode(self,nodeName):
        """creates a new node with the given name"""
        {"F":"deletesdawdawsd"}

    def deleteNode(self, nodeName):
        """deletes the node with the given name and any edges to it"""
        pass

mygraph = Graph()
mygraph.removeEdge("A","B")
# mygraph.addEdge("A","D")
adj = mygraph.showAdjacencies("A")

print(adj)