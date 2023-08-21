#In this programme i will build a turtule game using turtule module in python.
#This game is very simple and easy to understand.

#Importing the module
import turtle
import random
import winsound

print("both players will get alternate chances to roll the dice.") 
print("if you get even number you will move forward and if you get odd number you will move backward.")
#Creating a screen
#screen = turtle.Screen()
turtle.bgcolor("black")
turtle.title("Turtle Racing Game")
player1=turtle.Turtle()
player1.pen(pencolor="pink", fillcolor="black", pensize=5, speed=5)
player1.color("pink")
player1.shape("turtle")
player1.penup()
player1.goto(-250,120)

player2=player1.clone()
player2.pen(pencolor="yellow", fillcolor="black", pensize=5, speed=5)
player2.color("yellow")
player2.penup()
player2.goto(-250,-90)
player1.goto(320,80)
player1.pendown()
player1.begin_fill()
player1.circle(45)
player1.end_fill()
player1.penup()
player1.goto(-250,120)
player2.goto(320,-125)
player2.pendown()
player2.begin_fill()
player2.circle(45)
player2.end_fill()
player2.penup()
player2.goto(-250,-90)

die = [1,2,3,4,5,6]

for i in range(20):
    if player1.pos() >= (320,100):
        for i in range(5):
            winsound.Beep(1000,10)
        print("Player 1 Is The Winner !")
        break
    elif player2.pos() >= (320,-20):
        for i in range(5):
            winsound.Beep(1000,10)
        print("Player 2 Is The Winner !")
        break
    else:
        player_1_chance = input("Press Enter To Roll The Dice For Player 1 : ")
        die_output = random.choice(die)
        print("The Dice Output Is : ",die_output)
        if die_output % 2 == 0:
            player1.forward(20*die_output)
            print("Player 1 Is Moving Forward !")
        else:
            player1.backward(20*die_output)
            print("Player 1 Is Moving Backward !")
        player_2_chance = input("Press Enter To Roll The Dice For Player 2 : ")
        die_output = random.choice(die)
        print("The Dice Output Is : ",die_output)
        if die_output % 2 == 0:
            player2.forward(20*die_output)
            print("Player 2 Is Moving Forward !")
        else:
            player2.backward(20*die_output)
            print("Player 2 Is Moving Backward !")
