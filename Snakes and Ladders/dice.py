import turtle #import turtle module to access turtle graphics
import random #import random module for random number generations
import board #import board module  
import time #import time module to access time-based functions
screen = turtle.Screen()
d1 = turtle.Turtle()
d2 = turtle.Turtle()
d3 = turtle.Turtle()
d4 = turtle.Turtle()
d5 = turtle.Turtle()
d6 = turtle.Turtle()

screen.addshape("dice1.gif")
d1.shape("dice1.gif")
d1.speed(0)
d1.hideturtle() 

screen.addshape("dice2.gif")
d2.shape("dice2.gif")
d2.speed(0)
d2.hideturtle() 
    
screen.addshape("dice3.gif")
d3.shape("dice3.gif")
d3.speed(0)
d3.hideturtle() 

screen.addshape("dice4.gif")
d4.shape("dice4.gif")
d4.speed(0)
d4.hideturtle()

screen.addshape("dice5.gif")
d5.shape("dice5.gif")
d5.speed(0)
d5.hideturtle()

screen.addshape("dice6.gif")
d6.shape("dice6.gif")
d6.speed(0)
d6.hideturtle()
"""
****************************************************************************************
Function to simulate dice roll for player 1 and show the image of the dice number rolled
****************************************************************************************
"""
def p1_diceroll(x, y):
    Enter_key = ""
    x = ""
    if x == Enter_key:
        print("You rolled a %d" %(y))
        if y == 1:
            d1.showturtle()
            d1.hideturtle()
        elif y == 2:
            d2.showturtle()
            d2.hideturtle()
        elif y == 3:
            d3.showturtle()
            d3.hideturtle()
        elif y == 4:
            d4.showturtle()
            d4.hideturtle()
        elif y == 5:
            d5.showturtle()
            d5.hideturtle()
        elif y == 6:
            d6.showturtle()
            d6.hideturtle()
    elif x != Enter_key:
        while x != Enter_key:
            x = input("If you could just press the enter key **sigh**: ")
    return y
"""
****************************************************************************************
Function to simulate dice roll for player 2 and show the image of the dice number rolled
****************************************************************************************
"""
def p2_diceroll(x, y):
    Enter_key = ""
    x = ""
    if x == Enter_key:
        print("You rolled a %d" %(y))
        if y == 1:
            d1.showturtle()
            d1.hideturtle()
        elif y == 2:
            d2.showturtle()
            d2.hideturtle()
        elif y == 3:
            d3.showturtle()
            d3.hideturtle()
        elif y == 4:
            d4.showturtle()
            d4.hideturtle()
        elif y == 5:
            d5.showturtle()
            d5.hideturtle()
        elif y == 6:
            d6.showturtle()
            d6.hideturtle()
    elif x != Enter_key:
        while x != Enter_key:
            x = input("If you could just press the enter key **sigh**: ")
    return y
