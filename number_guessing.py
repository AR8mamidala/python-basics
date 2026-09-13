# Using Python's random module
import random
# A random integer between 1 and 100 is picked
number=random.randint(1,100)

print("I have generated a random number between 1 and 100. Have a guess!")
guess=0
guess_count=0

while guess_count<10:
    # This makes sure that the program doesn't crash out if a non-integer value is entered
    try:
        guess=int(input("Guess:"))
        guess_count=guess_count+1
    except ValueError:
        print("Please enter a valid number.")
        print()
        continue       
    if guess<1 or guess>100:
        print("Enter a number in the specified range!")
        print()
        print("Try again!")
        continue
    elif guess>number:
        print("Too high, try again!")
        print()
    elif guess<number:
        print("Too low, try again!")
        print()
    else:
        if guess_count<10:
            print(f"Well done the number is {number}.")
            print(f"You got it in {guess_count} guesses.")
            print()
            break

if guess==number and guess_count==10:
    print(f"Well done the number is {number}.")
    print("You got it in the final guess phew!")
elif guess!=number and guess_count==10:
    print("You have reached the maximum guess count, better luck next time.")
else:
    print("Bye bye!")