import random #imported random module to choose a random word for the game

name = input("enter your name: ")
print() 
print()

print("lets start the game ", name)

print() 
print()

words = ['bless', 'jet', 'ear', 'frog' , 'kit', 'area', 'rage',
        'weave', 'dismissal', 'session', 'designer', 'week',
        'pleasure', 'vigorous','thought','debt','grateful',
        'freeze','green','machinery','computer','letter',
        'chauvinist','crossing','cooperation','nonsense',
        'neutral','account','dare','justify'] #list of words that are needed to be guessed in the game

word = random.choice(words) #random.choice chooses a random word from the lists of words

print("Guess the word ", name) # user guessing a word
GuessedWord = input()

print() 
print()

chances = 7 #the number of maximum chances given to the user are 7

while chances > 0 : # running a while loop for taking continuous input from the user and checking if the input matches with given word 

    failed = 0 # counter to count the number of failed attempt

    for char in word : # running a for loop to check if the characters in the input are there in the given word

        if char in GuessedWord :

            print(char, end="") # printing the character if it's present

        else:

            print("*",end="")

            failed = failed +1 # increasing thte failed count if the character is not there

    print() 
    print()
    print()

    if failed == 0:

        print("You win\nThe word was ", word) # if there no failed attempts then the "you win" will be displayed

        break # and the loop will be breaked

    NewGuess = input("Guess the word ") #if the user failed to guess the word then another try is given

    GuessedWord = GuessedWord + NewGuess # newly guessed word is concatenated with the previous guess

    if NewGuess not in word: 

        chances = chances - 1 # for every failed attempt the remaining chances are reduced

        print("Wrong") 

        print("You have", + chances, 'more guesses') # remaining number of chances are printed

        if chances == 0: print("You Loose\n The word is ", word)
        # if the user fails to guess the word in the given number of chances then he looses