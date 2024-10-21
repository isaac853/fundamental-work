import  urllib.request,json,time
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

def typecheck(word: str) -> bool:
    word = word.lower()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in word:
        if i not in alphabet:
            return False
        
    return True

def listconstruction(word):
    global wordlist
    wordlist = []
    for i in range(len(word)):
        wordlist.append("_")

def inputword():
    global word
    word  = input("please enter a word  ")
    
    
    global count
    count = 0

    global letterlist
    letterlist = []

    while len(word) == 0 or not typecheck(word) or not isrealword(word):
        word = input ("please enter a real word with real letters  ")
        time.sleep(1)

    global incorrectlist
    incorrectlist = []

    listconstruction(word)

def guesslist(letterguess):
    global letterlist

    if letterguess in letterlist:
        return False

    else:
        letterlist.append(letterguess)
        return True

def letterguess():
    global word
    global wordlist
    global incorrectlist
    global count
    playerguess = str(input("guess a letter  "))
    while not typecheck (playerguess) or len(playerguess) != 1 or not guesslist(playerguess):
        playerguess = input("invalid input, try again:  ")


    for i in range(len(word)): 
        if word[i] == playerguess:
            wordlist[i] = playerguess

    if playerguess not in wordlist:
        incorrectlist.append(playerguess)
        count += 1

    print(wordlist,"known wrong letters,",incorrectlist, "incorrect guesses left:", 5-count)

    if "_" not in wordlist:
        return "win"

def rungame():
    inputword()
    while count != 5:
        if letterguess() == "win":
            print("you win")
            break
        if count == 5:
            print("game over")

rungame()









    