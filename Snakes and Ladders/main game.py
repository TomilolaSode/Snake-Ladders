import turtle #imports the turtle module to enable the use of the graphics 
import random #imports the random module to generate random numbers from a given distribution 
import board #imports the board module to enable the use of the board for the game
import dice #imports the dice module to grant to access dice-related functions
import time #imports the time module to enable time-based functions
greeting_message = """Welcome players. The aim of this game is to get ONE player to position 25 to declare that player as the winner of the game."""
instructions = """Instructions
1. Choose between 0, 1 and 2 to access the desired function when prompted. This applys to the first prompt that you will receive once you receive this message.
 0 - Start New Game
 1 - View Leaderboard
 2 - Exit game
2. When the prompt comes up for a player to roll the dice, the player can do so by pressing the enter key.
3. The character rep of each player should be decided between the two players beforehand.
4. Have fun while testing out the features of this game. 

Note: If you are thinking about the fact that I added both wins and losses to the leaderboard instead of just pick between the two of them to keep the code slightly shorter. I just felt like adding them both ┏(･o･)┛♪┗ (･o･) ┓.Please, don't mind the silly names ☆*ヾ(-∀・* )*+☆"""      
print(greeting_message + "\n")
print(instructions + "\n")
"""
*********************
Setting the screen up 
*********************
"""
screen = turtle.Screen()
screen.title("Snakes and Ladders")
screen.setup(600, 600, 0, 0)
screen.bgcolor("#f1ebdf")
board.draw_table()
win_im = turtle.Turtle()

"""
*******************************************************************
Function to move player 1(the cow) up or down based on its position 
*******************************************************************
"""
def obs_p1():
    global p1_posc
    global p1_dicec
    if p1.pos() == p1_di[8]:
        p1.goto(p1_di[11])
        p1_posc += 3
    elif p1.pos() == p1_di[17]:
        p1.goto(p1_di[22])
        p1_posc += 5
    elif p1.pos() == p1_di[4]:
        p1.goto(p1_di[14])
        p1_posc += 10
    if p1.pos() == p1_di[19]:
        p1.goto(p1_di[0])
        p1_posc -= 19
    elif p1.pos() == p1_di[7]:
        p1.goto(p1_di[2])
        p1_posc -= 5
    elif p1.pos() == p1_di[23]:
        p1.goto(p1_di[13])
        p1_posc -= 10
    return p1
"""
********************************************************************
Function to move player 2(the bull) up or down based on its position 
********************************************************************
"""
def obs_p2():
    global p2_posc
    global p2_dicec
    if p2.pos() == p2_di[8]:
        p2.goto(p2_di[11])
        p2_posc += 3
    elif p2.pos() == p2_di[17]:
        p2.goto(p2_di[22])
        p2_posc += 5
    elif p2.pos() == p2_di[4]:
        p2.goto(p2_di[14])
        p2_posc += 10
        
    if p2.pos() == p2_di[19]:
        p2.goto(p2_di[0])
        p2_posc -= 19
    elif p2.pos() == p2_di[7]:
        p2.goto(p2_di[2])
        p2_posc -= 5
    elif p2.pos() == p2_di[23]:
        p2.goto(p2_di[13])
        p2_posc -= 10
    return p2

"""
*******************************************************
Functions to move the players across the board smoothly
*******************************************************
"""
def p1_forward():
    if (0 <= p1_posc <= 4) or (10 <= p1_posc <= 14) or (20 <= p1_posc <= 24):
        if (p1_posc == 10 and p1.pos() == p1_di[9]) or (p1_posc == 20 and p1.pos() == p1_di[19]):
            p1.goto(p1.xcor(), p1.ycor() + 120)
        else:
            p1.goto(p1.xcor() + 120, p1.ycor())
def p2_forward():
    if (0 <= p2_posc <= 4) or (10 <= p2_posc <= 14) or (20 <= p2_posc <= 24):
        if (p2_posc == 10 and p2.pos() == p2_di[9]) or (p2_posc == 20 and p2.pos() == p2_di[19]):
            p2.goto(p2.xcor(), p2.ycor() + 120)
        else:
            p2.goto(p2.xcor() + 120, p2.ycor())
def p1_backward():
    if (5 <= p1_posc <= 9) or (15 <= p1_posc <= 19):
        if (p1_posc == 5 and p1.pos() == p1_di[4]) or (p1_posc == 15 and p1.pos() == p1_di[14]):
            p1.goto(p1.xcor(), p1.ycor() + 120)
        else:
            p1.goto(p1.xcor() - 120, p1.ycor())
def p2_backward():
    if (5 <= p2_posc <= 9) or (15 <= p2_posc <= 19):
        if (p2_posc == 5 and p2.pos() == p2_di[4]) or (p2_posc == 15 and p2.pos() == p2_di[14]):
            p2.goto(p2.xcor(), p2.ycor() + 120)
        else:
            p2.goto(p2.xcor() - 120, p2.ycor())
                
        
#Player movement patterns and coordinates are placed here
p1_di = [(-250, -230), (-130, -230), (-10, -230), (110, -230), (230, -230), (230, -110), (110, -110), (-10, -110), (-130, -110), (-250, -110), (-250, 10), (-130, 10), (-10, 10), (110, 10), (230, 10), (230, 130), (110, 130), (-10, 130), (-130, 130), (-250, 130), (-250, 250), (-130, 250), (-10, 250), (110, 250), (230, 250)] 
p2_di = [(-270, -270), (-150, -270), (-30, -270), (90, -270), (210, -270), (210, -150), (90, -150), (-30, -150), (-150, -150), (-270, -150), (-270, -30), (-150, -30), (-30, -30), (90, -30), (210, -30), (210, 90), (90, 90), (-30, 90), (-150, 90), (-270, 90), (-270, 210), (-150, 210), (-30, 210), (90, 210), (210, 210)] 

p1_wins = 0 #number of player 1's wins
p2_wins = 0 #number of player 2's wins
p1_losses = 0 #number of player 1's losses
p2_losses = 0 #number of player 2's losses
'''snakes = [(-250, 130), (-10, -110), (110, 250), (-270, 90), (-30, -150), (90, 210)]
ladders = [(-130, -110), (-10, 130), (230, -230), (-150, -150), (-30, 90), (210, -270)]'''

menu = ""
menu_new = "0"
menu_leaderboard = "1"
menu_end = "2"
while (menu != menu_new) or (menu != menu_leaderboard) or (menu != menu_end):
    menu = input("What do you want to do today: ") 
    while menu == menu_new:
        p1 = turtle.Turtle()
        p2 = turtle.Turtle()
        screen.addshape("cow.gif")
        p1.shape("cow.gif")
        p1.penup()
        p1.speed(0)
        p1.goto(-250, -230)
        p1.speed(2)
        screen.addshape("bull.gif")
        p2.shape("bull.gif")
        p2.penup()
        p2.speed(0)
        p2.goto(-270, -270)
        p2.speed(2)
        
        p1_posc = 0 #the position of player 1
        p2_posc = 0 #the position of player 2
        p1_dicec = 0 #the number of times the dice has been rolled by this player
        p2_dicec = 0 #the number of times the dice has been rolled by this player
        while (p1_posc <= 24) or (p2_posc <= 24) and menu == menu_new:
            if p1_dicec == p2_dicec:
                p1_roll = input("Mama Moo, Press enter to roll the dice: ")
                p1_dicenum = random.randint(1, 6)
                dice.p1_diceroll(p1_roll, p1_dicenum)
                    
                if p1_dicenum == 1:
                    p1_posc += 1
                elif p1_dicenum == 2:
                    p1_posc += 2
                elif p1_dicenum == 3:
                    p1_posc += 3
                elif p1_dicenum == 4:
                    p1_posc += 4
                elif p1_dicenum == 5:
                    p1_posc += 5
                elif p1_dicenum == 6:
                    p1_posc += 6
                    
                if p1_posc < 24:
                    if p1_dicenum == 1:
                        p1_posc -= 1 
                        for x in range(p1_dicenum):
                            p1_posc += 1
                            p1_forward()
                            p1_backward()
                        obs_p1()
                    elif p1_dicenum == 2:
                        p1_posc -= 2
                        for x in range(p1_dicenum):
                            p1_posc += 1
                            p1_forward()
                            p1_backward()
                        obs_p1()
                    elif p1_dicenum == 3:
                        p1_posc -= 3
                        for x in range(p1_dicenum):
                            p1_posc += 1
                            p1_forward()
                            p1_backward()
                        obs_p1()
                    elif p1_dicenum == 4:
                        p1_posc -= 4 
                        for x in range(p1_dicenum):
                            p1_posc += 1
                            p1_forward()
                            p1_backward()
                        obs_p1()
                    elif p1_dicenum == 5:
                        p1_posc -= 5 
                        for x in range(p1_dicenum):
                            p1_posc += 1
                            p1_forward()
                            p1_backward()
                        obs_p1()
                    elif p1_dicenum == 6:
                        p1_posc -= 6 
                        for x in range(p1_dicenum):
                            p1_posc += 1
                            p1_forward()
                            p1_backward()
                        obs_p1()
                elif p1_posc > 24:
                    if p1_dicenum == 1:
                        p1_posc -= 1
                    elif p1_dicenum == 2:
                        p1_posc -= 2
                    elif p1_dicenum == 3:
                        p1_posc -= 3
                    elif p1_dicenum == 4:
                        p1_posc -= 4
                    elif p1_dicenum == 5:
                        p1_posc -= 5
                    elif p1_dicenum == 6:
                        p1_posc -= 6
                elif p1_posc == 24:
                    p1.goto(p1_di[24])
                    p1_wins += 1
                    p2_losses += 1
                    print("Player 1 Wins!!!") #prints a message for the winner
                    screen.addshape("win.gif")
                    win_im.shape("win.gif") 
                    win_im.showturtle() #displays image notifying players of win
                    time.sleep(0.5) #waits
                    menu = input("0, 1 or 2: ")
                    win_im.hideturtle() #hides the winning image
                    break
                p1_dicec += 1
                    
            if p2_dicec < p1_dicec:
                p2_roll = input("Bob the Bull, Press enter to roll the dice: ")
                p2_dicenum = random.randint(1, 6)
                dice.p2_diceroll(p2_roll, p2_dicenum)

                if p2_dicenum == 1:
                    p2_posc += 1
                elif p2_dicenum == 2:
                    p2_posc += 2
                elif p2_dicenum == 3:
                    p2_posc += 3
                elif p2_dicenum == 4:
                    p2_posc += 4
                elif p2_dicenum == 5:
                    p2_posc += 5
                elif p2_dicenum == 6:
                    p2_posc += 6
                            
                if p2_posc < 24:
                    if p2_dicenum == 1:
                        p2_posc -= 1
                        for x in range(p2_dicenum):
                            p2_posc += 1
                            p2_forward()
                            p2_backward()
                        obs_p2()
                    elif p2_dicenum == 2:
                        p2_posc -= 2
                        for x in range(p2_dicenum):
                            p2_posc += 1
                            p2_forward()
                            p2_backward()
                        obs_p2()
                    elif p2_dicenum == 3:
                        p2_posc -= 3
                        for x in range(p2_dicenum):
                            p2_posc += 1
                            p2_forward()
                            p2_backward()
                        obs_p2()
                    elif p2_dicenum == 4:
                        p2_posc -= 4
                        for x in range(p2_dicenum):
                            p2_posc += 1
                            p2_forward()
                            p2_backward()
                        obs_p2()
                    elif p2_dicenum == 5:
                        p2_posc -= 5
                        for x in range(p2_dicenum):
                            p2_posc += 1
                            p2_forward()
                            p2_backward()
                        obs_p2()
                    elif p2_dicenum == 6:
                        p2_posc -= 6
                        for x in range(p2_dicenum):
                            p2_posc += 1
                            p2_forward()
                            p2_backward()
                        obs_p2()
                elif p2_posc > 24:
                    if p2_dicenum == 1:
                        p2_posc -= 1
                    elif p2_dicenum == 2:
                        p2_posc -= 2
                    elif p2_dicenum == 3:
                        p2_posc -= 3
                    elif p2_dicenum == 4:
                        p2_posc -= 4
                    elif p2_dicenum == 5:
                        p2_posc -= 5
                    elif p2_dicenum == 6:
                        p2_posc -= 6
                elif p2_posc == 24:
                    p2.goto(p2_di[24])
                    p2_wins += 1
                    p1_losses += 1
                    print("Player 2 Wins!!!") #prints a message for the winner
                    screen.addshape("win.gif")
                    win_im.shape("win.gif")
                    win_im.showturtle()
                    time.sleep(0.5) #waits
                    menu = input("0, 1 or 2: ")
                    win_im.hideturtle() #hides the winning image
                    break
                p2_dicec += 1
#prints the leaderboard which contains the wins and losses of each player
    if menu == menu_leaderboard:
        print("%10s %10s %10s\n" %("Player", "Wins", "Losses"))
        print("%10s %10d %10d\n" %("Player 1", p1_wins, p1_losses))
        print("%10s %10d %10d\n" %("Player 2", p2_wins, p2_losses))
#prints a goodbye message and proceeds to exit the game for the player
    if menu == menu_end:
        print("Goodbye, Come back when you can (✿˵ゝᵕ •˵)")
        exit()
        
