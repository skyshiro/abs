import random

secretNumber = random.randint(1,20)

print('I am thinking of a number between 1 and 20...')

tries = 7

for guessesTaken in range(tries):

    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Guess is low')
    elif guess > secretNumber:
        print('Guess is high')
    else:
        break

if guess == secretNumber:
    print('Correct! You guessed the number in: ' + str(guessesTaken) + ' guesses')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
