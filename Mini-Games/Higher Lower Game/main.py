
from art import logo, vs
from game_data import data
import random

print(logo)
print("Welcome to the Higher Lower game!")

# Shuffle my game_data
random.shuffle(data)

# Initial parameters
game_end = False
num_count = 0
score = 0

while not game_end:
    for _ in range(len(data)-1):    
        print(f"Compare A: {data[num_count]['name']}, a {data[num_count]['description']}, from {data[num_count]['country']}.")
        #print(data[num_count]['follower_count'])
        print(vs)
        print(f"Against B: {data[num_count+1]['name']}, a {data[num_count+1]['description']}, from {data[num_count+1]['country']}.")
        #print(data[num_count+1]['follower_count'])
        user_input = input("Who has more followers? Type 'A or 'B': ").lower()
        if (data[num_count]['follower_count'] > data[num_count+1]['follower_count'] and user_input == "a") or (data[num_count+1]['follower_count'] > data[num_count]['follower_count'] and user_input == "b"):
            score += 1
            num_count +=1
            print(f"You are right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_end = True
            break
