#rules
#------------------------------------------------------
# 1 - whatever players (probs add a limit anyway, but make it keep going)
# each player rolls all 5 die to decide who goes first then just go in order
# on each turn players roll all 5 dice at once, they can then select any dice they like to keep aside, and roll the rest. they can roll up to 3 times
# there are thirteen categories to be filled for each player. at the end of each turn they must fill one of these in either with a 0, or with the score achieved by fuffiling the category
# unless it has been 0'd consecutive yahtzee's give bonus points on top of the points earned from filling in a squeare
# bonus of 35 points if scoring more than 63 on the upper section

import random

def diceroll():
    return random.randint(1,6)

def intcheck(proposal) -> bool:
    for i in str(proposal):
        if i not in ["1","2","3","4","5","6","7","8","9","0"]:
            return False
    int()
    return True
            
def playerno():
    
    scorelist = []
    playercount = 0 

    newplayer  = [[["-" for i in range(6)],["-" for i in range(7)],[0]]]

    playerNoInput = input("how many players do you want? ")
    while True:
        if intcheck(playerNoInput):
            break
        playerNoInput = input ("invalid input, try again: ")

    for i in range(int(playerNoInput)):
        scorelist += newplayer
        playercount += 1

    return playercount, scorelist

def enum(list):
    for index, data in enumerate(list):
        print(index+1,":",data)

def scoringdisplay(scorelist, player):
    upperSection =[
    "aces(ones): total of aces only",
    "twos: total of twos only",
    "threes: total of threes only",
    "fours: total of fours only",
    "fives: total of fives only",
    "sixes: total of sixes only",
    ]

    lowerSection =[
    "3 of a kind: total of all 5 dice",
    "4 of a kind: total of all 5 dice",
    "full house: 25 points",
    "small straight: 30 points",
    "large straight: 40 points",
    "YAHTZEE(five of a kind): 50 points / 100 point bonus",
    "chance: total of all five dice",
    ]

    print("\nupper section \n--------------------------------------------------------")
    enum(upperSection)

    print("\nlower section \n--------------------------------------------------------")
    enum(lowerSection)

    print("\ncurrent placements \n--------------------------------------------------------")
    print("\nupper section \n--------------------------------------------------------")
    enum(scorelist[player][0])
    print("\nlower section \n--------------------------------------------------------")
    enum(scorelist[player][1])
    print("\ncurrent bonus \n--------------------------------------------------------")
    print(scorelist[player][2][0])

def dicekeep():
    dicekeeplist = []
    
    while len(dicekeeplist) < 5:
        choice = input("\ntype which dice you want to keep, leave blank if you have finished choosing: ")
    
        if choice == "":
            return dicekeeplist
        
        while True:
            if choice in ["1","2","3","4","5"] and choice not in dicekeeplist:
                break

            print("\ninvalid input, try again.")
            choice = input("type which dice you want to keep, leave blank if you have finished choosing: ")
            
            if choice == "":
                return dicekeeplist

        dicekeeplist.append(int(choice))
    
    return dicekeeplist

def handcreation():
    die = ["-","-","-","-","-"]
    dicekeeplist = []
    count = 0

    while True:

        for i in range(5):
            if (i+1) not in dicekeeplist:
                die[i] = diceroll()

            print("dice",(i+1),"roll:", die[i])
        
        count += 1
        if count == 3:
            break

        dicekeeplist = dicekeep()
        

    return die

def uppersection(scorelist, player: int,die):
    upperchoice = input("1-6, which of the upper section would you like access  ")

    while upperchoice not in ["1","2","3","4","5","6"]:
        print("\ninvalid input, try again.")
        upperchoice = input("1-6, which of the upper section would you like access  ")

    upperchoice = int(upperchoice)

    if scorelist[player][0][upperchoice-1] != "-":
        return "invalid"
    
    inputchoice = input("0 or score, which do you want to enter in this section  ")

    while inputchoice not in ["0", "score"]:
        print("\ninvalid input , try again.")
        inputchoice = input("0 or score, which do you want to enter in this section  ")

    if inputchoice == "0":
        return 0, upperchoice
    
    if inputchoice == "score" and upperchoice not in die:
        return "invalid"
    
    else:
        score = 0

        for i in range(5):
            if die[i] == upperchoice:
                score += upperchoice

        return score, upperchoice

def numbercount(die):
    numbercount = [0,0,0,0,0,0]
    for i in die:
        numbercount[i-1] += 1
    return numbercount

def dietotal(die):
    score = 0
    for i in die:
        score += i
    return score
        
def threeofakind(die):
    for i in numbercount(die):
        if i >= 3:
            return dietotal(die)

    return "invalid"

def fourofakind(die):
    for i in numbercount(die):
        if i >= 4:
            return dietotal(die)

    return "invalid"

def fullhouse(die):
    if 3 in numbercount(die) and 2 in numbercount(die):
        return 25
    
    return "invalid"

def smallstraight(die):
    die.sort()
    count = 0
    for i in range(4):

        if die[i+1] == die[i]+1:
            count += 1

        else: 
            count = 0

        if count == 3:
            return 30

    return "invalid"

def largestraight(die):
    die.sort()
    count = 0
    for i in range(4):

        if die[i+1] == die[i]+1:
            count += 1

        else: 
            count = 0
            
        if count == 4:
            return 40

    return "invalid"

def yahtzee(die):
    for i in numbercount(die):
        if i >= 5:
            return 50

    return "invalid"

def chance(die):
    return dietotal(die)

def yahtzeebonus(die):
    for i in numbercount(die):
        if i == 5:
            return True
    return False

def lowersection(scorelist, player: int, die):
    
    bonus = 0
    if yahtzeebonus(die):
        bonus = 100

    lowerchoice = input("1-7, which of the lower section would you like access  ")

    while lowerchoice not in ["1","2","3","4","5","6","7"]:
        print("\ninvalid input, try again.")
        lowerchoice = input("1-7, which of the lower section would you like access  ")

    lowerchoice = int(lowerchoice)

    if scorelist[player][1][lowerchoice-1] != "-":
        return "invalid"

    inputchoice = input("0 or score, which do you want to enter in this section  ")

    while inputchoice not in ["0", "score"]:
        print("\ninvalid input , try again.")
        inputchoice = input("0 or score, which do you want to enter in this section  ")

    if inputchoice == "0":
        return 0, lowerchoice, bonus
    
    else:
        if lowerchoice == 1:
            return threeofakind(die), lowerchoice, bonus

        if lowerchoice == 2:
            return fourofakind(die), lowerchoice, bonus

        if lowerchoice == 3:
            return fullhouse(die), lowerchoice, bonus
        
        if lowerchoice == 4:
            return smallstraight(die), lowerchoice, bonus
    
        if lowerchoice == 5:
            return largestraight(die), lowerchoice, bonus
        
        if lowerchoice == 7:
            return chance(die), lowerchoice, bonus

        if lowerchoice == 6:
            return yahtzee(die), lowerchoice, bonus

def playerturn(scorelist, player: int):
    
    print("\nplayer",(player + 1),"turn \n--------------------------------------------------------")
    
    die = handcreation()
    while True:
        scoringdisplay(scorelist, player)
        print("\ncurrent rolls:",die)

#add a display for the players current filled sections
        sectionchoice = input("\nwhich section, upper or lower: ")

        while sectionchoice not in ["upper", "lower"]:
            print("\ninvalid input, try again")
            sectionchoice = input("\nwhich section, upper or lower: ") 
        
        if sectionchoice == "upper":
            if "-" in scorelist[player][0]:
                result = uppersection(scorelist, player,die)

            else:
                print("\nupper section is full")
                continue

            if 'invalid' in result:
                print("\naction not allowed, try again")
                continue

            scorelist[player][0][result[1]-1] = result[0]
            break

        else:
            if "-" in scorelist[player][1]:
                result = lowersection(scorelist, player,die)

            else:
                print("\nlower section is full")
                continue

            if "invalid" in result:
                print("\naction not allowed, try again")
                continue

            scorelist[player][1][result[1]-1] = result[0]
            scorelist[player][2][0] += result[2]
            break

    return scorelist

def playerscore(player, scorelist):
    score = 0
    upperscore = 0

    for i in range(6):
        upperscore += scorelist[player][0][i]

    if upperscore >= 63:
        score += 35
    score += upperscore

    for i in range(7):
        score += scorelist[player][1][i]

    score += scorelist[player][2][0]

    return score

def doloop(scorelist):
    for i in range(len(scorelist)):
        for j in range(len(scorelist[i])):
            for k in scorelist[i][j]:
                if k == "-":
                    return True
    return False

def fullgame(scorelist, playercount):
    turn = random.randint(0,playercount-1)

    loop = True
    while loop:
        scorelist = playerturn(scorelist, turn)
        turn = (turn +1) % playercount
        loop = doloop(scorelist)

    finalscorelist = []
    for i in range(playercount):
        finalscorelist.append({"player": ("player",(i+1)),"score": playerscore(i, scorelist)})
        print("player",i,"score:",finalscorelist[i]["score"],"\n")

    def sortingsomehow(e):
        return  e["score"]
    
    finalscorelist.sort(key = sortingsomehow, reverse=True)

    for i in range(len(finalscorelist)):
        print(finalscorelist[i]["player"],":",finalscorelist[i]["score"])

temp = playerno()
playercount = temp[0]
scorelist = temp[1]
del temp

# scorelist = playerturn(scorelist, 0)[0]
# print(scorelist)

fullgame(scorelist, playercount)