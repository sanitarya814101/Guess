import random

print("Number Guessing Game")
print("Guess the number between 1 to 20")

chance = 5

print('You have total '+str(chance)+' chance')

number = random.randrange(1, 20)

guess = int(input("Enter your number: "))

while(chance != 1 and guess != number):
    if(guess > number):
        print("Your guess was too high. Guess a number smaller than " + str(guess))
        chance = chance-1
        print('You have total '+str(chance)+' chance left')
        guess = int(input("Enter your number: "))
    else:
        print("Your guess was too low. Guess a number greater than " + str(guess))
        chance = chance-1
        print('You have total '+str(chance)+' chance left')
        guess = int(input("Enter your number: "))

if guess == number:
    print("Congratulations. You guessed the correct number.")

if (chance <= 1 and guess != number):
    print("You lose in guessing the number")
    print("The correct number is: "+str(number))
