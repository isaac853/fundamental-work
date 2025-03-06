import time, random,urllib.request,json
from urllib.error import HTTPError
from urllib.request import urlopen, Request

def isrealword(guess: str) -> bool:

    link = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
    url = link + guess

    try:
        with urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'})) as response:
            return response.status == 200
    except HTTPError as err:
        if err.code == 404:
            return False
        else:
            print("something's gone horribly wrong")
            raise  


def inputcheck(wordguess, letterlist) -> bool:

    lettercheck = [False,False,False,False,False,False,False,False]

    for i in range(len(wordguess)):
        count = 0
        if wordguess[i] in letterlist:

            for j in range(len(letterlist)):

                if wordguess[i] == letterlist[j] and not lettercheck[j]:
                    lettercheck[j] = True
                    break

                else:
                    count+= 1

                if count == 8:
                    return False
        else:
            return False
        
    return True
                
def fullgame(player,playerscore):
# weigh list towards scrabble distribution
# A-9, B-2, C-2, D-4, E-12, F-2, G-3, H-2, I-9, J-1, K-1, L-4, M-2, N-6, O-8, P-2, Q-1, R-6, S-4, T-6, U-4, V-2, W-2, X-1, Y-2, Z-1
    
    cons =  ["b","b","c","c","c","c","d","d","d","f","g","g","h","h","j","k","l","l","l","l","l","m","m","m","n","n","n","n","n","n","n","p","p","p","q","r","r","r","r","r","r","r","s","s","s","s","s","s","s","s","s","s","t","t","t","t","t","t","t","v","w","x","y","y","z"]
    vowels = ["a","a","a","a","a","a","a","a","e","e","e","e","e","e","e","e","e","e","e","e","i","i","i","i","i","i","i","i","i","o","o","o","o","o","o","o","o","u","u","u"]

    choices = ["vowel", "consonant","v","c"]
    letterlist = []
    


    print(player1, "turn")
    print("--------------------------------------------------")

    for i in range(8):
        while True:
            typechoice = input("do you want a vowel or a consonant (v/c) ")
            typechoice.lower()
            print("")

            if typechoice in choices:
                if typechoice == "consonant" or typechoice == "c":
                    letterlist.append(cons[random.randint(0,len(cons)-1)])
                    break

                elif typechoice == "vowel" or typechoice == "v":
                    letterlist.append(vowels[random.randint(0,len(vowels)-1)])
                    break
            else:
                print("invalid input")

        print(letterlist)
        
   
    print("think of a word ")
    print("")

    for i in range (30):
        print(29 - i)
        time.sleep(1)

    print("")

    print("your list is, ", letterlist)

    while True:
        wordguess = input("guess the longest word you can now, ")
        print("")

        if wordguess == "":
            break

        if inputcheck(wordguess, letterlist) and isrealword(wordguess):
            break

        else:
            time.sleep(1)
            print("your list is"," word", letterlist)
            print("")

    return playerscore + len(wordguess) 


player1 = input("player1, what is your name: ")
print("")
player2 = input("player2, what is your name: ")
print("")

player1score = 0
player2score = 0


for i in range (3):
    print("round", i + 1)
    print("----------------------------------------")
    
    player1score = fullgame(player1, player1score)
    player2score = fullgame(player2, player2score)

    print(player1,"your current score is:", player1score)
    print("")
    print(player2,"your current score is:", player2score)
    print("")

if player1score > player2score:
    print(player1, "wins")

elif player2score > player1score:
    print(player2, "wins")

else:
    print("draw")



#validate wordguess, making sure each letter is only as many times as it appears
    # if isrealword(wordguess):
    #     return playerscore + len(wordguess) 
    

#pick a number of vowels and consonants totaling to 8
#player makes longest word possible in 30 secs
#other play does the same
#round + 1