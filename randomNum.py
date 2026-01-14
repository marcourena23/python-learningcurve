import random

low_range = 1
hight_range = 10
answer= random.randint(low_range,hight_range)
guesses = 0
trying = True

print(f"Enter a number between {low_range} and {hight_range}")

while trying:
    guess = input("Enter your guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < low_range or guess > hight_range:
            print(f"{guess} is a number out of range")
            print(f"Enter a number between {low_range} and {hight_range}")
        elif guess < answer: print("Too Low! Try again :")
        elif guess > answer: print("Too hight! Try again :")
        else :
            print(f"Correct!!!! , The answer was {answer}")
            print(f"Numbers of guesses: {guesses}")
            trying = False
    else: print(f"Enter a number between {low_range} and {hight_range}")