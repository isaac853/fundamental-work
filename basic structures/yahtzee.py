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

#give each player an empty list with 13 slots, have it filled with placeholders, replace these with the scores , gonna have to make function for each category, long af
def intcheck(proposal) -> bool:
    for i in str(proposal):
        if i not in ["1","2","3","4","5","6","7","8","9","0"]:
            return False
    int()
    return True
            
def playerno():
    
    scorelist = []
    playercount = 0 

    newplayer  = [[["-" for i in range(6)],["-" for i in range(7)]]]

    playerNoInput = input("how many players do you want? ")
    while True:
        if intcheck(playerNoInput):
            break
        playerNoInput = input ("invalid input, try again: ")

    for i in range(int(playerNoInput)):
        scorelist += newplayer
        playercount += 1

    return playercount, scorelist

temp = playerno()
playercount = temp[0]
scorelist = temp[1]
del temp

def enum(list):
    for index, data in enumerate(list):
        print(index+1,":",data)

def scoringdisplay():
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

def lowersection(scorelist, player: int,die):
    pass

def playerturn(scorelist, player: int):
    
    print("\nplayer",(player + 1),"turn \n--------------------------------------------------------")
    
    die = handcreation()
    while True:
        scoringdisplay()

        sectionchoice = input("which section, upper or lower: ")

        while sectionchoice not in ["upper", "lower"]:
            print("\ninvalid input, try again")
            sectionchoice = input("which section, upper or lower: ") 
        
        if sectionchoice == "upper":
            if "-" in scorelist[player][0]:
                result = uppersection(scorelist, player,die)

            else:
                print("upper section is full")
                continue

            if result == 'invalid':
                print("action not allowed, try again")
                continue

            scorelist[player][0][result[1]-1] = result[0]



        else:
            lowersection(scorelist, player,die)

#do lowersection
#add a selection for the first players turn, then use mod to traverse the list numerically from there
#still need scoring including bonuses for yahtzees and for getting more than 63 in uppersection

playerturn(scorelist, 0)
