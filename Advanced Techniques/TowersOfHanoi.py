class Stack:
    def __init__(self, towerSize):
        self.size = towerSize
        self.topPointer = -1
        self.data = [None for i in range(towerSize)]

    def push(self,disk):
        self.topPointer += 1
        self.data[self.topPointer] = disk


    def pop(self):
        if self.topPointer == -1:
            print("this tower is empty")
            return False

        else:
            temp = self.data[self.topPointer]
            self.data[self.topPointer] = None
            self.topPointer -= 1
            return temp

    def displaydata(self):
       return self.data

    def displaysize(self):
        return self.topPointer
class Game:
    def __init__(self,towerSize):
        #use a dictionary for this
        self.towers = [Stack(towerSize),Stack(towerSize),Stack(towerSize)]
        
        for i in range(towerSize, 0, -1):
            self.towers[0].push(i)
        
    def displayGame(self):
        #  TODO make this more visual later
        print(self.towers[0].displaydata())
        print(self.towers[1].displaydata())
        print(self.towers[2].displaydata())

    def ordercheck(self,proposal, tower):
        data = tower.displaydata()
        toppointer = tower.displaysize()
        if data[toppointer] > proposal:
            return True

    def moveDisk(self):
        while True:
            startTower = int(input("FROM: "))
            endTower = int(input("TO: "))

            pop = self.towers[(startTower - 1)].pop()

            if not pop:
                continue
            
            self.ordercheck(pop,self.towers[(endTower - 1)])

            self.towers[(endTower - 1)].push(pop)
            break

game = Game(7)

while True: 
    game.moveDisk()

    game.displayGame()


