import random
import math

#Menu1:
def Menu1():
    print("\t1. Numbers")
    print("\t2. Hangman")
    print("\t3. Words")
    print("\t4. Rock Paper Scissors")
    print("\t5. Management")
    print("\t6. Emoji Generator")
    print("\t7. Quit")

#Number game HAS A BUG!
def Number_Guessing():
    print("\nWelcome to Guess the Number!")
    lower = int(input("\nEnter the lowest number: "))
    print()
    upper = int(input("Good now enter the highest number: "))

    x = random.randint(lower,upper)
    count = 3
    print("\nChances: " + str(count) + " >:)\n")

    guess = int(input("Guess the number: "))

    while (x != guess):

        if (x == guess):
            print("\nWow! You're pretty good at this!!!\n")
            break
        elif (guess > x):
            print("\nHmmm not quite try a lower number....")
        elif (guess < x):
            print("\nUmm no try a higher number!")
        
        #int(count) = count - 1
        
        if (count == 0):
            print("\nOof you're out of tries!\nThe number was: " + str(x) +'\n')
            break;
        
        guess = int(input("Guess the number: "))
        
#Hangman
def Hangman():
    print("\nWelcome to Hangman!\n")
    #Mini menu for exit:
    
    pk = 0

    while(pk != 2):
        print("\t1. Play")
        print("\t2. exit")
        pk = int(input("\nMake your selection: "))

        #into the switch-case:
        match(pk):
            case 1: 
                #Insert that massive glob of code:
                getit = input("Do you know how to play: ")
                
                while(getit != "yes" and getit != "no"):
                    print("\nPlease enter an appropriate answer and try again....")
                    getit = input("\nDo you know how to play: ")
                
                while(getit == "yes"):
                   #Begin the game:
                    print("Great! Let's begin!\n")
                    
                    #Insert horrible jumble of code-gameplay: Tuples
                    data_Base = "hangman", "icecream","shoes","right","left","up","down"
                    dash = '_'
                    
                    # A list to alter the values more easily
                    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                    
                    mystery = "" #need to assign an initial value before I can use it
                    hang = False # boolean to represent a players lose of the game
                    
                    #Make a class or tuple to hold the characters of the word:
                    grab = random.choice(data_Base)
                    for i in grab:
                        mystery = mystery + dash
                    
                    print(mystery + "\n" + grab) # Testing 1 2 Testing 1 2
                    
                    guess = input("Enter your letter: ")

                    while len(guess) > 1 or len(guess) < 1:
                        print("Please enter a character only and try again...")
                        guess = chr(input("Enter your letter: "))
                    
                    for i in grab:
                        if guess in grab:
                            end = mystery[grab.index(i) + 1:]
                            mystery = mystery[:grab.index(i)] + i + end
                            abc.insert(abc.index(guess), '*')
                            abc.remove(guess)
                            break

                while(getit == "no"):
                    print("\nThat's okay! Here are the instructions:\n")

                    print("\tTo begin, the game HANGMAN is a 2-player game, a GUESSER and PROVIDER is required. This cannot be played solo.\n")
                    print("\tThe PROVIDER provides the word to be guessed while the GUESSER attempts to guess said word.\n")
                    print("\tThere is a limit to the number of tries. This will be dependent on how long the word is.\n")
                    print("\tFor the sake of the 1st round, I will be the PROVIDER and you, the player, the GUESSER.\n")

                    proceed = input("Do you understand now: ")

                    while(proceed != "yes") and (proceed != "no"):
                        print("\nPlease enter an appropriate response and try again....")
                        proceed = input("Do you understand now: ")

            case _:
                if(pk == 2):
                    break
                else:
                    print("Please enter an appropriate answer and try again....")
    print("\nExiting HANGMAN......\n")

#Word Guessing Game complete!
def Words():
    print("\nWelcome to Guess the Word!")
    #Entering looop:
    pk = 0

    while(pk != 2):
        print("\n\t1. Play")
        print("\t2. Exit")

        pk = int(input("\nMake your selection: ")) #This is taking an integer input

        match (pk):
            case 1:
                #Enter the gameplay
                things = input("\nDo you know how to play: ") # This is the default way. It takes STRINGS ONLY so input  1 is "1"
                while (things != "yes" and things != "no"):
                    print("\nPlease enter an appropriate response and try again....")
                    things = input("\nDo you know how to play: ")
                if(things == "yes"):
                    print("\nGreat let the game begin!\n")

                    #Begin with an array, list, or tuple of words:
                    Words = ("chicken", "purple", "clever", "turtle", "sky","crowd","shadow","light","computer")
                    pick = random.randint(0,8)
                    
                    # Now we need the players guess (str input):
                    match pick:
                        case 0:
                            print("Hint: it has wings and is delicious.")
                            guess = input("Enter your guess: ")
                            if guess == Words[pick]:
                                print("You win! The word was " + Words[pick])
                            else:
                                print("Aw, you lose! The word was " + Words[pick] + " Play again?")
                        case 1:
                            print("Hint: It's my creators favorite color.")
                            guess = input("Enter your guess: ")
                            if guess == Words[pick]:
                                print("You win! The word was " + Words[pick])
                            else:
                                print("Aw, you lose! The word was " + Words[pick] + " Play again?")
                        case 2:
                            print("Hint: Smart people are also often seen as ___")
                            guess = input("Enter your guess: ")
                            guess.lower()
                            if guess == Words[pick]:
                                print("You win! The word was " + Words[pick])
                            else:
                                print("Aw, you lose! The word was " + Words[pick] + " Play again?")
                        case 3:
                            print("Hint: It allows you to draw in python. It's eggs are found on the beach.")
                            guess = input("Enter your guess: ")
                            if guess == Words[pick]:
                                print("You win! The word was " + Words[pick])
                            else:
                                print("Aw, you lose! The word was " + Words[pick] + " Play again?")
                        case 4:
                            print("Hint: Look up.")
                            guess = input("Enter your guess: ")
                            if guess == Words[pick]:
                                print("You win! The word was " + Words[pick])
                            else:
                                print("Aw, you lose! The word was " + Words[pick] + " Play again?")
                        case 5:
                            print("Hint: Lots of people.")
                            guess = input("Enter your guess: ")
                            if guess == Words[pick]:
                                print("You win! The word was " + Words[pick])
                            else:
                                print("Aw, you lose! The word was " + Words[pick] + " Play again?")
                        case 6:
                            print("Hint: It follows you everywhere you go.")
                            guess = input("Enter your guess: ")
                            if guess == Words[pick]:
                                print("You win! The word was " + Words[pick])
                            else:
                                print("Aw, you lose! The word was " + Words[pick] + " Play again?")
                        case 7:
                            print("Hint: It doesn't follow you everywhere you go. Usually represents the heros.")
                            guess = input("Enter your guess: ")
                            if guess == Words[pick]:
                                print("You win! The word was " + Words[pick])
                            else:
                                print("Aw, you lose! The word was " + Words[pick] + " Play again?")
                        case 8:
                            print("Hint: You're literally using it to play this dumb but clever game.")
                            guess = input("Enter your guess: ")
                            if guess == Words[pick]:
                                print("You win! The word was " + Words[pick])
                            else:
                                print("Aw, you lose! The word was " + Words[pick] + " Play again?")

                while (things == "no"):
                    print("\nThat's okay. Here are the instructions:\n")

                    #Insert list of instructions here:
                    print("\tTo start, at least 2 players are required to play, GUESSER and CHOOSER.")
                    print("\n\tThe CHOOSER picks the word to be guessed and the GUESSER guesses said word.")
                    print("\n\tFor the sake of this game I will be CHOOSER and you, the player will be GUESSER.")

                    proceed = input("\nDo you understand now: ")
                    while(proceed != "yes" and proceed != "no"):
                        print("\nPlease enter an appropriate answer and try again....")
                        proceed = input("\nDo you understand now: ")
                    if(proceed == "yes"):
                        print("\nGreat let's begin!")

            case _:
                if (pk == 2):
                    break
                else:
                    print("\nPlease enter an appropriate response and try again....")
    #End of Program
    print("\nExiting WORD GUESS....")

#Rock Paper Scissors Game complete!
def RPS():
    print("\nWelcome to Rock Paper Scissors!\n")
    pk = 0

    while(pk != 2):
        print("\t1. Play")
        print("\t2. Exit")

        pk = int(input("Make your selection: "))

        match pk:
            case 1:
                get = input("\nDo you know how to play: ")
                while(get == 'yes'):
                    print("\nGreat let's begin!\n")
                    rounds = 0
                    player_Wins = 0
                    computer_Wins = 0

                    while rounds < 3:
                        # Make a tuple:
                        Computer = "rock","paper","scissors"
                        Hand = random.randint(0,2)
                        # Get user input:
                        hand = input("Rock, Paper, Scissors \nShoot: ")
                    
                        if(hand == Computer[Hand]):
                            print("\nWe tied! I had " + Computer[Hand] + "\n")
                        elif hand == "scissors" and Computer[Hand] == "paper":
                            print("\nWOW! You won this round I had " + Computer[Hand] + "\n")
                            player_Wins = player_Wins + 1
                        elif hand < Computer[Hand]:
                            if hand == "paper" and Computer[Hand] == "scissors":
                                print("\nVictory is mine this time! I had " + Computer[Hand] + "\n")
                                computer_Wins = computer_Wins + 1
                            else:
                                print("\nWOW! You won this round I had " + Computer[Hand] + "\n")
                                player_Wins = player_Wins + 1
                        else:
                            print("\nVictory is mine this time! I had " + Computer[Hand] + "\n")
                            computer_Wins = computer_Wins + 1
                        
                        #increment the number of rounds:
                        rounds = rounds + 1
                    
                    if player_Wins > computer_Wins:
                        print("Wow! You won the game with " + str(player_Wins) + " wins!")
                    elif player_Wins == computer_Wins:
                        print("Huh?! A tie game! GG pal!")
                    else:
                        print("HA! I won the game with " + str(computer_Wins) + " wins!")
                    print("\nHit Play to play again friend!")
                    break;
                    
                while(get == 'no'):
                    print("\nThat's okay! Here are the instructions: \n")
                    #Jumble of instructions for the game:
                    print("\n\tTo start, this game requires at least 2 players. The computer will generate rock, paper, or scissors.")
                    print("\n\tYou, the player will then input Rock, Paper, or Scissors.")
                    print("\n\tThe computer then prints the results of the match. The matches are best out of 3.")
                    
                    #Re-asking if they understand the rules:
                    get = input("\nDo you understand the rules now: ")
            case 2:
                print("\nThanks for playing! Goodbye!")
            case _:
                print("\nPlease select from the options above and try again.\n")
                
#Hotel Management
def hotel_Management():
    print("\nWelcome to the hotel management system!")

#Employment Management
def employee_Management():
    print("\nWelcome to the Employee Management System!")
    #Insert list of menu options here:
    opt = int(input("Select from the selection listed above: "))

#Emoji into text Generator
def emoji_Gen():
    print("\nWelcome to the text generator!")

#Insert main function here:
def main_shell():
    print("\nThis program is designed to Practice and learn skills in Python")
    #Read the Players answer selection:
    Menu1()
    selection = int(input("\nMake your selection: "))
    while selection != 6:
        match selection:
            case 1:
                #Number Guessing Game
                print("Guess the number selected!\nLoading....")
                Number_Guessing()
            case 2:
                #Hangman
                print("\nHangman selected!\nLoading....")
                Hangman()
            case 3:
                #Words
                print("\nGuess the word selected!\nLoading....")
                Words()
            case 4:
                #RPS
                print("\nRock Paper Scissors selected!\nLoading....")
                RPS()
            case 5:
                #Emplyee Management System
                print("\nLoading the Management System....")
                employee_Management()
            case 6:
                #Emoji Generator
                print("\nLoading Emoji Generator....")
                emoji_Gen()
            case _:
                if selection == 7:
                    break #breaks out of the while loop. Apparently breaks work differently in python
                else:
                    print("\nPlease select from the selection above. Try Again....")
        #reprint menu and prompt for a new selection until the user wants to end things altogether
        Menu1()
        selection = int(input("\nMake you selection: "))
    #End of program
    print("\nExiting....\nThank you. Goodbye.")          

main_shell()
