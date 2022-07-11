import random
import main
from colorama import Fore

def generatePassphrase():
        numberOfWords = int(input("Number of words: "))
        retainWords = []
        # lenght validation
        if numberOfWords > 0 and numberOfWords <= 100:
                # Selecting words for the passphrase and put into the list
                for i in range(numberOfWords):
                        word = random.choice(main.words)
                        retainWords.append(word)
                                
                # Concatenate the list and print the passphrase
                passphrase = "-".join(retainWords)
                main.clear()
                print(f'Numbers of words {numberOfWords}')
                print(passphrase)
                                 
        else:
                print("invalid number")
        
def quitAbout():
        selectionBack = str(input("===> "))
        if selectionBack == 'q' or 'Q':
                main.clear()
                startScreen()
        else:
                quitAbout()

def startScreen():
        main.clear()
        print(Fore.YELLOW +' Welcome to')
        main.heading()
        select = input('===> ')
        if select == '1':
                generatePassphrase()
        elif select == '2':
                main.clear()
                main.about()
                quitAbout()
        elif select == '3':
                main.clear()
        else:
                main.clear()
                startScreen()
startScreen()