from colorama import Back
import random

def isWord(word, wordList):
    return len(word) == 5 and word in wordList

def generateDictionary():
    wordList = list()
    englishFile = open(r"english.txt", "r")
    wordList = englishFile.readlines()
    englishFile.close()
    wordList = list(filter(lambda x: len(x) == 6 and "'" not in x, wordList))
    wordList = list(map(lambda x: x[0:5], wordList))
    return wordList


def __main__():
    wordList = generateDictionary()
    print("PyWordle by Caleb Brock")
    play(wordList)

def play(wordList):
    answer = wordList[random.randrange(len(wordList))]
    tries = 0
    print("[ ][ ][ ][ ][ ]")
    print("Please enter your guess:")
    while True:
        guess = input()
        if not isWord(guess, wordList):
            continue
        else:
            printResponse(guess, answer)

        tries += 1

        if guess == answer:
            print("Congratulations, you won in", tries, "tries!")
            if playAgain():
                play(wordList)
            else:
                break
        elif tries > 5:
            print("The word was", answer)
            if playAgain():
                play(wordList)
            else:
                break

def playAgain():
    print("Would you like to play again?")
    ans = input()
    return ans.lower() == "yes" or ans.lower() == "y"  

def containsCharacter(word, letter):
    return word.find(letter) != -1

def printResponse(guess, answer):
    response = ""
    for i in range(0, len(guess)):
        if guess[i] == answer[i]:
            response = response + Back.GREEN + "[" + guess[i] + "]" + Back.RESET
        elif containsCharacter(answer, guess[i]):
            response = response + Back.YELLOW + "[" + guess[i] + "]"  + Back.RESET
        else:
            response = response + "[" + guess[i] + "]" 
    print(response)
        
__main__()