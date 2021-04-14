import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard' ")

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

answer = random.randint(1, 100)

is_game_over = False


while not is_game_over:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == answer:
        print("You guessed correctly, you win!")
        is_game_over = True
    elif guess > answer:
        print("Too high.")
        attempts -= 1
    elif guess < answer:
        print("Too low.")
        attempts -= 1
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        is_game_over = True
    elif guess != answer:
        print("Guess again.")
    
