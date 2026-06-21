import turtle #imports turtle module to access time-based functions

#Modifies the overall layout of the program
screen = turtle.Screen()
screen.title("Board")
screen.setup(600, 600, 0, 0)
screen.bgcolor("#f1ebdf")

#Modifies the turtle cursors(position, thickness, color)
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.speed(0)
t2.speed(0)
t1.penup()
t2.penup()
t1.goto(-300, -300)
t2.goto(-300, -300)
t1.pendown() 
t2.pendown()
t1.pensize(2) #sets the size or width of the pen for t1
t2.pensize(2) #sets the size or width of the pen for t2
t1.pencolor("Blue") #sets the color of the t1's pen 
t2.pencolor("Blue") #sets the color of the t2's pen

"""
**************************************************
Function to draw the rows and columns on the board
**************************************************
"""
def rows_columns():
    for i in range(1,5):
        t1.forward(120*i)
        t2.left(90)
        t1.left(90)
        t2.forward(120*i)
        t1.forward(600)
        t2.right(90)
        t1.penup()
        t2.forward(600)
        t1.goto(-300, -300)
        t2.penup()
        t1.pendown()
        t2.goto(-300,-300)
        t1.right(90)
        t2.pendown()


l1 = turtle.Turtle() #Ladder 1
l2 = turtle.Turtle() #Ladder 2
l3 = turtle.Turtle() #Ladder 3
s1 = turtle.Turtle() #Snake 1
s2 = turtle.Turtle() #Snake 2
s3 = turtle.Turtle() #Snake 3
"""
************************************************************
Function to place LADDERS on specific positions on the board
************************************************************
"""
def ladders():
    screen.addshape("ladder.gif")
    l1.shape("ladder.gif")
    l1.speed(0) #sets speed for ladder 1
    l1.penup()
    l1.goto(-110, -70)
    screen.addshape("ladder2.gif")
    l2.shape("ladder2.gif")
    l2.speed(0) #sets speed for ladder 2
    l2.penup()
    l2.goto(0, 180)
    screen.addshape("ladder3.gif")
    l3.shape("ladder3.gif") 
    l3.speed(0) #sets speed for ladder 3
    l3.penup()
    l3.goto(250, -130)
    return l1, l2, l3 #returns the turtles: ladder 1, 2 and 3
"""
************************************************************
Function to place SNAKES on specific positions on the board
************************************************************
"""
def snakes():
    screen.addshape("snake.gif")
    s1.shape("snake.gif")
    s1.speed(0)
    s1.penup()
    s1.goto(130, 110)
    screen.addshape("snake2.gif")
    s2.shape("snake2.gif")
    s2.speed(0)
    s2.penup()
    s2.goto(10, -180)
    screen.addshape("snake3.gif")
    s3.shape("snake3.gif")
    s3.speed(0)
    s3.penup()
    s3.goto(-230, -50)
    return s1, s2, s3
    
"""
************************************************************
Function to place and generate the numbers from left to right
************************************************************
"""
def forward(x, y):
    for i in range(x, y):
        turtle.forward(120)
        turtle.write("%d" %(i), font=("Arial", 8, "normal"))
"""
************************************************************
Function to place and generate the numbers from right to left
************************************************************
"""
def backward(a, b):
    for i in range(a, b, -1):
        turtle.forward(120)
        turtle.write("%d" %(i), font=("Arial", 8, "normal")) 
    
"""
************************************************************
Function to place all the numbers on the board
************************************************************
"""
def nums():
    turtle.speed(0) #controls the speed of the turtle
    turtle.pencolor("red") #contols the color of the turtle pen
    turtle.penup() #stops the pen from drawing any visible lines when moving
    turtle.goto(-290, -200)
    turtle.write("1", font=("Arial", 8, "normal"))
    forward(2,6)
    turtle.goto(-290, -80)
    turtle.write("10", font=("Arial", 8, "normal"))
    backward(9, 5)
    turtle.goto(-290, 40)
    turtle.write("11", font=("Arial", 8, "normal"))
    forward(12, 16)
    turtle.goto(-290, 160)
    turtle.write("20", font=("Arial", 8, "normal"))
    backward(19,15)
    turtle.goto(-290, 280)
    turtle.write("21", font=("Arial", 8, "normal"))
    forward(22, 26)
    turtle.hideturtle()
    

"""
************************** 
Function to draw the board
**************************
"""
def draw_table():
    for i in range(4):
        t1.forward(600) #moves forward 600 pixels
        t1.left(90) #turns the turtle 90 degrees
    rows_columns()
    t1.hideturtle() #hides the 
    t2.hideturtle() 
    nums()
    ladders()
    snakes()
   


    
