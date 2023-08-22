#I am creating rock papepr scissor game.
#I am using Random module for it.

import random

list1 = ["rock", "paper", "scissor"]

print("Welcome to the Rock Paper Scissor Game")

print("You have 10 chances to play this game")

user_score = 0
computer_score = 0

for i in range(1, 11):
    print("Enter Your Choice from the list: ", list1)
    user_choice = input()
    computer_choice = random.choice(list1)
    print("Computer Choice is: ", computer_choice)
    if user_choice == computer_choice:
        print("Same Choice by both , both will get 0 points")
        user_score = user_score + 0
        computer_score = computer_score + 0
    elif user_choice == "rock" and computer_choice == "paper":
        print("Computer won the game")
        computer_score = computer_score + 1
    elif user_choice == "rock" and computer_choice == "scissor":
        print("User won the game")
        user_score = user_score + 1
    elif user_choice == 'paper' and computer_choice == "rock":
        print("User won the game")
        user_score = user_score + 1
    elif user_choice == computer_choice:
        print("Same Choice by both , both will get 0 points")
        user_score = user_score + 0
        computer_score = computer_score + 0
    elif user_choice == "paper" and computer_choice == "scissor":
        print("Computer won the game")
        computer_score = computer_score + 1
    elif user_choice == "scissor" and computer_choice == "rock":
        print("Computer won the game")
        computer_score = computer_score + 1
    elif user_choice == "scissor" and computer_choice == "paper":
        print("User won the game")
        user_score = user_score + 1
    elif user_choice == computer_choice:
        print("Same Choice by both , both will get 0 points")
        user_score = user_score + 0
        computer_score = computer_score + 0
    else:
        print("please enter the correct choice")
        quit()


print("User Score is: ", user_score)
print("Computer Score is: ", computer_score)

if user_score > computer_score:
    print("Cpngratulations You Won the Game !")
elif user_score == computer_score:
    print("Game is Tie !")
else:
    print("Computer Won the Game !")
