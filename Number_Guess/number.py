from art import logo
import random

print(logo)
print("I'm tinking a number between 1 and 100")
computer_number=random.randint(0,100)
# to test the code 
print(computer_number)
user_level=input("Choose a difficulty. Type 'easy' or 'hard': ")

def user_lives():
    if user_level=="easy":
        return 10
    elif user_level=="hard":
        return 5
    else:
        print("You entered a wrong input.Try again.....!")
        return 0

def level(lives):
    game_over=True
    if lives!=0:
        while game_over:
            print(f"You have {lives} attempts remaining to guess the number.")
            user_guess=int(input("Make a guess :"))
            if user_guess>computer_number:
                print("Too High.\nGuess again.\n")
                lives=lives-1
            elif user_guess<computer_number:
                print("Too low.\nGuess again.\n")
                lives=lives-1
            elif user_guess==computer_number:
                print(f"You got it! The answer was {computer_number}.")
                game_over=False
            if lives==0:
                print("You've run out of guesses, you lose.")
                game_over=False
    

attempts=user_lives()
level(attempts)


