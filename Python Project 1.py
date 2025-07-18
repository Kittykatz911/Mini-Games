import random
import math
from collections import counter

print("/nThis program is designed to Practice and learn skills in Python")
#Read the Players answer selection
selection = int(input("/nMake your selection: "))

#Number Guessing Game

Number_Guessing()



lower = int(input("/n Enter the lowest number: "))
upper = int(input("/n Good now enter the highest number: "))

x = random.randint(lower,upper)
print("/n Chances: ", round(math.log(upper - lower + 1, 2)), " >:)")

count = 0

while count < math.log(upper - lower + 1, 2):
    count += 1
    guess = int(input("Guess the number: "))
    if x == guess:
        print("/n Wow! You're pretty good at this!!!")
        break
    elif x > guess:
        print("/n Hmmm not quite try a lower number....")
        break
    elif x < guess:
        print("/n Umm no try a higher number!")
        break
    
if count >= math.log(upper - lower +1,2):
    print("/n Oof you're out of tries!/n The number was: ")
    print(x)
#Hangman

#Word Guessing Game

#Rock Paper Scissors

#Hotel Management

#Employment Management

#Emoji into text Generator
