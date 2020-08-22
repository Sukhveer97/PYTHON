import random
secretnumber = random.randint(1,20)
print("I am thinking of a number between 1 and 20, you have 5 guesses ")

for guessestaken in range(1, 6):
    guess = int(input("Take a guess: "))

    if guess < secretnumber:
        print("Your guess is too low")
    elif guess > secretnumber:
        print("Your guess is too high")
    else:
        break

if guess == secretnumber:
    print("Correct! You guessed the number in " + str(guessestaken) + " guesses")
else:
    print("Sorry, the number was in fact " + str(secretnumber))

