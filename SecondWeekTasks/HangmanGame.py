import pdb
import sys
#pdb.set_trace()

def hangman(clue_word):
    count = 0
    isWordGuessed = 0
    l = len(clue_word)
    charsGuessedUpToNow = []
    print("Welcome to Hangman! Let's play!")
    for i in range(len(clue_word)):
        charsGuessedUpToNow.append('-')
        
    for i in charsGuessedUpToNow:
        print(i,end='')    
    print()
    while count < 10 and isWordGuessed < len(clue_word) :
        print("Guess a letter:")
        currentLetter = input()
        i = 0
        guessed = False

        while i < len(clue_word):
            if(currentLetter == clue_word[i]):
                charsGuessedUpToNow[i] = currentLetter
                isWordGuessed+=1
                i += 1
                guessed = True
            
            i+=1
            if(i == len(clue_word) - 1 and  not guessed):    
                count +=1
                print("Incorrect")
            
            
        for c in charsGuessedUpToNow:
            print(c,end = '')


    if(count == 10):
        print("You are hanged")
    else:
        print("You won")


def main():
    hangman(sys.argv[1])


if(__name__ == "__main__"):
    main()