# Build a Number guessing game, in which the user selects a range.
# Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
# Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses

import random
import math

#Calculate the minimum number of trials taken to guess a number
def GuessTheNumber(computer_generated, guess, low, high, trials):   
    count = 0
    while(count < trials):

        if computer_generated == guess:
            return count
        elif computer_generated > guess:
            count += 1
            try:
                guess = int(input('Sorry! Enter a Upper Bound \n'))
            except ValueError:
                print('Please Enter a valid Integer between {0} and {1}' .format(low,high))                  
        else:
            count += 1
            try:
                guess = int(input('Sorry! Enter an Lower bound \n'))
            except ValueError:
                print('Please Enter a valid Integer\n')
                
    return False

#Select a range
low = 1
high = 100

computer_generated = random.randint(low, high)

trials = round(math.log(high-low,2))
print("Maximum trials : ", trials)
try:
    guess = int(input('Guess the number between 1 to 100 \n'))
    
except ValueError:
    guess = int(input('Please Enter a valid Integer\n')) 
while guess < low or guess > high:
    if guess < computer_generated or guess > computer_generated:
        guess = int(input('Please Enter an Integer ranging between {0} and {1} \n' .format(low, high)))

result = GuessTheNumber(computer_generated, guess, low, high, trials)

if result:

    if result == 4:
        #print('You won')
        print('You guessed the number in {0} trials \n Average! \n' .format(result+1))
         
    elif result == 3:
        print('You guessed the number in {0} trials \n Good! \n' .format(result+1))
        
    elif result  == 2:
        print('You guessed the number in {0} trials \n Great! \n' .format(result+1))
        
    elif result == 1:
        print('You guessed the number in {0} trials \n Excellent! ' .format(result+1))
             
    else:
        print('Hooray! You won')
    print('Computer generated Number : ', computer_generated)
    
else:
    print('You exceeded maximum trials \n')
    print('You Lost :(')
    print('Computer generated Number : ', computer_generated)


