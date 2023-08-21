 #importing libraries
import turtle
import random
import time


#creating turtle screen
screen = turtle.Screen()                #creating a object to turtle to create screen
screen.title('SNAKE GAME')              #window name is setted as sanke game
screen.setup(width = 650, height = 650) #setting width and height of the window
turtle.bgcolor('yellow')                #selecting background colour



##creating a border for our game

screen.tracer(0)            #hides the movement of turtle arrow
'''turtle.speed(1)             #increase the speed of arrow
turtle.pensize(5)           #selecting the size of pen,thickness
turtle.penup()              #lifting pen from 0,0 and moving it to desired location
turtle.goto(-400,250)       #we want border to starts from here
turtle.pendown()            #dropping pen in above mentioned locaton and starts from there
turtle.color('black')       #selecting outline colour must inside quotes
turtle.forward(800)         #top line moves +400 toward positive direction
turtle.right(90)            #turtle drawer turns 90 degree and it is faceing downward now
turtle.forward(500)         #moves downward till +400,-250
turtle.right(90)            #turtle drawer turns 90 degree and it is ready to move left
turtle.forward(800)         #moves till -400,-250
turtle.right(90)            #turtle drawer turns 90 degree and it is ready to move upward
turtle.forward(500)         #moves upward till -400,+250 i.e where we started the border
turtle.penup()              #we finished the border drawing so lifting pen from that point 
turtle.hideturtle()         #hide turtle function hides the turtle drawing arrow,if not called allow will be vissible
'''
#score
score = 0               #INITIAL SCORE
delay = 0.1


#snake
snake = turtle.Turtle() #CREATING SNAKE
snake.speed(0)          #speed of snake
snake.shape('circle')   #sanke shape
snake.color("black")    #sanke colour
snake.penup()           #PICK PEN
snake.goto(0,0)         #SANKE STARTING POSITION
snake.direction = 'stop'


#food
fruit = turtle.Turtle() #CREATING FRUIT
fruit.speed(0)
fruit.shape('square')   #food shape
fruit.color('red')      #food colour
fruit.penup()           #PICK PEN
fruit.goto(0,100)       #FOOD STARTING POSITION

old_fruit=[]

#scoring
scoring = turtle.Turtle()
scoring.speed(0)
#scoring.shape("square")
scoring.color("red")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,260) #0,300
scoring.write("Score :",align="center",font=("ds-digit",24,"normal"))#ds-digital,normal


#######define how to move
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)  

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Keyboard bindings
screen.listen()                             #ASSIGNING KEYBOARD KEYS
screen.onkeypress(snake_go_up, "Up")        #UP
screen.onkeypress(snake_go_down, "Down")    #DOWN
screen.onkeypress(snake_go_left, "Left")    #LEFT
screen.onkeypress(snake_go_right, "Right")  #RIGHT

#main loop

while True:
        screen.update()
            #snake and fruit coliisions
        if snake.distance(fruit)< 20:
                x = random.randint(-290,270) #GENERATING RANDON NO FOR NEXT FRUIT
                y = random.randint(-290,290)#-240,240
                fruit.goto(x,y)             #NXT FRUIT 
                scoring.clear()
                score+=1                   #INC SCORE
                scoring.write("Score:{}".format(score),align="center",font=("ds-digital",24,"normal"))
                delay-=0.001
                
                ## creating new_ball
                new_fruit = turtle.Turtle()
                new_fruit.speed(0)
                new_fruit.shape('square')
                new_fruit.color('black')
                new_fruit.penup()
                old_fruit.append(new_fruit)
                

        #adding ball to snake
        
        for index in range(len(old_fruit)-1,0,-1):
                a = old_fruit[index-1].xcor()
                b = old_fruit[index-1].ycor()

                old_fruit[index].goto(a,b)
                                     
        if len(old_fruit)>0:
                a= snake.xcor()
                b = snake.ycor()
                old_fruit[0].goto(a,b)
        snake_move()

        ##snake and border collision    
        if snake.xcor()>300 or snake.xcor()< -300 or snake.ycor()>300 or snake.ycor()<-300:
                time.sleep(1)
                screen.clear()
                screen.bgcolor('turquoise')
                scoring.goto(0,0)
                scoring.write("   GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))


        ## snake collision
        for food in old_fruit:
                if food.distance(snake) < 20:
                        time.sleep(1)
                        screen.clear()
                        screen.bgcolor('turquoise')
                        scoring.goto(0,0)
                        scoring.write("    GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))


                
        time.sleep(delay)

#turtle.Terminator()

