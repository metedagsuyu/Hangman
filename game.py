#allow game against a computer( comp chooses a random word from the dictionary file
#################################################################################################
# Game   : Main function for game, it will be called automatically
#          with help from source:
#          Docs.oracle.com,. N.p., 2015. Web. 1 Dec. 2015.
#          https://docs.oracle.com/javase/tutorial/collections/interfaces/examples/dictionary.txt
#
# Goal   : A command line Hangman game to use my Introductory Computer Science skills 
# Info   : Player 1 will be playing against a computer or against Player 2;
#          If Playing against a computer, computer chooses a word from the dictionary;
#          If Playing against another Player, they choose the word;
#          The spacing and lines are adjusted for my screen resolution (1366 by 768)
# Author : METEHAN DAGSUYU
# Date   : December, 2015
################################################################################################
from random import randint, choice
import time

#function below displays welcome message
def welcome():
    print("\n\n\n\n                   Welcome to my game of HANGMAN\n--------------------------------------------------------------------\n                              Enjoy              by: Metehan Dagsuyu\n\n")
    
#function below gets and checks the word 
def wordCheck():
    word = input('\n\n\n\nPlayer 2, enter a word: ')
    while word not in open('dictionary.txt').read() or 4 > len(word):
        if word not in open('dictionary.txt').read():
            print("--------------------------------------------------------------------")
            word = input('\n@     The word ('+ word.upper() +') is not in the dictionary,\n     PLease try again: ')
        if 4 > len(word):
            print("--------------------------------------------------------------------")
            word = input("\n@     The length (" + str(len(word)) + ") of the word (" + word + ") is too short,\n     Word should consist of more than 4 letters,\nTry again: ") 
    return word.lower()

#function below displays info on the word
def info(word):
    sline = []
    for a in range(len(word)):
        sline.append("_")
    print("                The word chosen is", len(word),
          "characters long \n                 ***********************************\n                  ********************************")    
    return sline

#function below displays non-guess info, and rearranges mystery word
def printMysteryWord(sline,guess,word):
    pos = [i for i, v in enumerate(word) if v == guess.lower()]
    for a in range(len(pos)):
        b = pos[a]
        sline[b] = guess.lower()
    print("\nTo restart game, type 're'\nTo quit game, type 'quit'\nTo get hint, type '?'\n\nMYSTERY WORD   :"," ".join(sline), end="" )
    return sline

#function below checks if game is over
def callGG(guessNumber,play,sline,word,man):
    allGuesses = ("".join(sline))
    if allGuesses == word.lower():
        print("\n--------------------------------------------------------------------\n\n      ---------------||   Current Game Over   ||---------------\n\n      <<<<<<<<<<       YOU WIN CONGRATULATIONS       >>>>>>>>>>\n\n                   --  Mystery Word was: ",word,"--\n--------------------------------------------------------------------\n")
        return again()
    elif guessNumber >= 7:
        print("\n--------------------------------------------------------------------\n\n      ---------------||   Current Game Over   ||---------------\n","".join(man)+"     @@@@@@@@     G G    @@@@@@@@@@\n                  Mystery Word was: "+word+"\nYou werent able to guess correctly with the amount of lives you had.\n--------------------------------------------------------------------\n")
        return again()
    else: return 0
    
#function below gets a guess, checks guess and directs the guess to according function
def checkGuess(previousGuesses,fullGuesses,word,hint):
    msg = ("You must be new, ","Hello, ","Vowels are easy help, ","Think Randomlyyy, ","Do you want a 'How to play' manual? ","You can do this, ","Are you slow? ","Alphabet has 26 characters, ","Maybe have a glass of water, ","It takes 10 years to be a pro at guessing, ","Are you giving up? Didnt thinks so, ")
    num = randint(0,10) 
    if len(previousGuesses)==0:
        sml = "None so far"
    else: 
        sml = previousGuesses
    print("\nPrevious Guesses  :",sml) 
    guess = input(msg[num]+ "Guess a letter : ") 
    giveMsg(guess,word)
    while len(guess) !=1 or guess.lower() in previousGuesses or guess == "!" or guess == "?":
        
        while fullGuesses <=0 and guess == "!":
            guess = input("@     No more activations left Newbie, now guess: ")
        if  guess =="!":
            return guess
        
        while hint <=0 and guess == "?":
            guess = input("@     No more hints left Newbie, now guess: ")
        if guess == "?":           
            return guess
        
        if (len(guess) !=1 and guess.lower() == "quit") or (len(guess) !=1 and guess.lower() == "re"):
            return guess.lower()
        if (len(guess) !=1 and guess.lower() != "quit") or (len(guess) !=1 and guess.lower() != "re"):
            guess = input("@     Guess ONE letter: ")
        if guess.lower() in previousGuesses or (len(guess) !=1 and guess.lower() != "quit")or (len(guess) !=1 and guess.lower() != "re"):
            guess = input("@     Guess ONE letter that you havent guessed before: ") 
            
        giveMsg(guess,word)       
    return guess

def hints(word,previousGuesses):
    a = ""
    while a in previousGuesses:
        a = word[randint(0,len(word)-1)]
    return a
    
    
#function below displays msg if user wants to quit or restart
def giveMsg(guess,word):
    if guess.lower()  == "quit":
        print("\n--------------------------------------------------------------------\n                 Mystery Word was: [",word,"]\n                 Go Have Fun Outside :)\n                 You Lost\n--------------------------------------------------------------------\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nType 'hangman()' to play again")
        
    elif guess.lower()  == "re":
        print("\n\n\n\n\n\n\n\n\n\n\n--------------------------------------------------------------------\nMystery Word was: [",word,"]\nNice Try, Thank you for playing again.\nYou Lost\n")

#function below displays information on previous guesses
def guessInfo(guessNumber,correct,fullGuesses,man,hint):
    print("\n      -----------------||   Current Game   ||-----------------")
    if 7 - guessNumber == 1:
        a = "(LAST GUESS BUDDY)"
    else:
        a = ""
    print("".join(man[:guessNumber+1]))
    print("\nNumber of lives left :",7 - guessNumber, a)
    
    if correct == 0:
        print("Number of correct guesses : 0 so far")
    else:
        print("Number of correct guesses :", correct)
        
    if guessNumber == 0:
        print("Number of wrong guesses   : 0 so far")
    else:
        print("Number of wrong guesses   :", guessNumber)
        
    if hint == 0:
        print("Number of hints remaining : 0 left")
    else:
        print("Number of hints remaining :", hint)    
        
    if fullGuesses == 0:
        print("Number of full guesses remaining: 0 left")
    else:
        print("Number of full guesses remaining: ", fullGuesses, "( Type ! to activate )") 
    return 7 - guessNumber

#function checks if your full guess was correct or not
def fullGuessCheck(guess, word, fullGuesses):
    if fullGuesses <= 0 :
        return 0
    full = "hi"
    if guess == "!":
        fullGuesses -= 1
        print("\n$@#$%^&())(*&^%$#@!@#$%^&^%$#!*)(*&^%$#@!!@#$A&^%$@#$^&*(%$#!@!\n$@#$%^&**&^$#!  ----  FULL GUESS ACTIVATED  ----  *(#!@*&^%$#@!\n$@#$%^&*$#@!@#$%^&*()(*$@&@$!@#%^()^%$#@!!@#$%^&*(*^$@)(*&^$#@!")
        full = input("Guess your full word: ")
    if full.lower()  == word:
        print("--------------------------------------------------------------------\n\n      ---------------||   Current Game Over   ||---------------")
        print("\n\n      <<<<<<<<<<       YOU WIN CONGRATULATIONS       >>>>>>>>>>\n\n                   -- Mystery Word was: ",word,"--\n----------------------------------------------------------------------\n")
        fullGuesses = 69
    elif full == "hi":
        a = 1    
    else: 
        print("---------------------------------------------------------------\n\n\n\n\n\n\n\n\n     ---------------|| Current Game Continues ||---------------\n\n\n\n      You have guessed the full word INCORRECTLY, what a fail!\n\n\n\n\n\n\n")
        time.sleep(3)
    return fullGuesses

#function below keeps tracking of all previous guesses
def addpreviousGuesses(guess,previousGuesses):
    if len(guess) != 1 or guess == "!":
        return previousGuesses
    else:
        previousGuesses += "["+guess+"]"
    return previousGuesses

#function below keeps track of correct guesses, displays if the guess was correct or not
def correctWrongTracker(guess,guessNumber,word,correct):
    print("\n\n--------------------------------------------------------------\n") 
    if guess == "!":
        return [guessNumber, correct]
    elif guess.lower() in word:
        if guess == "":
            a = 1
        else: 
            correct += 1        
            print("Last guess ["+guess+"] was   >>>>>>>>>>    CORRECT!")
    else:
        sign = "+"
        guessNumber = changeGuessNumber(sign,guessNumber)        
        print("Last guess ["+guess+"] was   >>>>>>>>>>    INCORRECT!")    
    return [guessNumber, correct]

#function below keeps track of wrong guesses
def changeGuessNumber(sign,guessNumber):
    if sign == "+" :
        guessNumber += 1
    if guessNumber <= 0 :
        return 0
    return guessNumber

#function below asks if user wants to play again once they win/lose
def again():
    play = input("If you want to play again type in 1 : ")
    if play == "1":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n--------------------------------------------------------------------\n                              Thank You                              \n--------------------------------------------------------------------\n\n     ~~~~~~~~~~~~~ {{   Starting A New Game   }} ~~~~~~~~~~~~~\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        return 1
    else:  
        print("\n--------------------------------------------------------------------\n                        Go Have Fun Outside :)                             \n--------------------------------------------------------------------\n")
        return 69
#function below asks if user wants to play against a computer or another person
def playerChoice():
    a = input("If you want to play against a COMPUTER type in 1: ")
    if a != "1":
        b = (input("If you want to play against another PLAYER (this isnt multiplayer) type in 1: "))
        if b != "1":
            print("\n\nWhy are you even here? I'll assume you want to verse a COMPUTER \n-------------------------------------------------------------------")
            
            time.sleep(7)
            return 1
        if b == "1":
            return 0
    elif a == "1":
        return 1
    
    
#function below controls everything: the game
def hangman():
    welcome()
    gamemode = playerChoice()
    if gamemode == 0 :
        word = wordCheck() #
    elif gamemode ==1:
        badword = choice(list(open('dictionary.txt')))
        word = badword[:-1]
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") #wing ide wont allow me to use echo for the word to be asterisk
    sline = info(word)
    man = ["      |____       ","\n           0      ","\n          /","|","\\","\n           |","\n          /"," \\"]
    play = 0
    guessNumber = 0
    previousGuesses = ""
    guess = ""
    correct = 0
    hint = 2
    fullGuesses = 2
    while play == 0 :
        a = correctWrongTracker(guess,guessNumber,word,correct)
        guessNumber = a[0]
        correct = a[1]
        live = guessInfo(guessNumber,correct,fullGuesses,man,hint)
        sline = printMysteryWord(sline,guess,word)
        play = callGG(guessNumber,play,sline,word,man)
        if play == 0  :
            guess = checkGuess(previousGuesses,fullGuesses,word,hint)
            if guess == "?":
                hint -= 1                 
                guess = hints(word,previousGuesses)
            if guess.lower()  == "re":
                hangman()
                return
            if  guess.lower()  == "quit":
                return
            fullGuesses = fullGuessCheck(guess, word, fullGuesses)
            if fullGuesses != 69:
                previousGuesses = addpreviousGuesses(guess,previousGuesses)
                previousguessNumber = guessNumber
            elif fullGuesses == 69 :
                play = again()
                if play == 1:
                    time.sleep(3)
                    hangman()                
        elif play == 1:
            time.sleep(3)
            print("\n\n\n\n\n\n\n\n\n\n")
            hangman()
hangman()
