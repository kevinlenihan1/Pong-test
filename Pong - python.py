import turtle
import time

# this creates the screen
sc = turtle.Screen()
sc.title("Pong Game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)

#left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400,0)

#right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400,0)

#ball to be bounced
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0,0)
hit_ball.dx = 5
hit_ball.dy = 5

#intialize score
left_player = 0
right_player = 0

#display for score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0,260)
sketch.write("Left player : 0   Right player : 0", align="center", font=("Arial", 25, "normal"))

#paddle movements
#left paddle move up
def paddleaup():
    y = left_pad.ycor()
    if y < 250:     #limits paddle movement
        y += 20
        left_pad.sety(y)

#left paddle move down
def paddleadown():
    y = left_pad.ycor()
    if y > -240:    #limits paddle movement
        y -= 20
        left_pad.sety(y)

#right paddle move up
def paddlebup():
    y = right_pad.ycor()
    if y < 250:     #limits paddle movement
        y += 20
        right_pad.sety(y)

#right paddle move down
def paddlebdown():
    y = right_pad.ycor()
    if y > -240:    #limits paddle movement
        y -= 20
        right_pad.sety(y)

#control binds
sc.listen()
sc.onkeypress(paddleaup, "w")       #move left paddle up with w
sc.onkeypress(paddleadown, "s")     #move left paddle down with s
sc.onkeypress(paddlebup, "Up")      #move right paddle up with up arrow
sc.onkeypress(paddlebdown, "Down")  #move right paddle down with down arrow

#main game loop
while True:
    sc.update()
    time.sleep(0.01)

    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    #check borders
    #checks top border
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1

    #checks bottom border
    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1

    #checks right border
    if hit_ball.xcor() > 500:
        hit_ball.goto(0,0)
        hit_ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Left player : {}  Right player : {}".format(left_player, right_player), align="center",
                     font=("Arial", 25, "normal"))
        
    #checks left border
    if hit_ball.xcor() < -500:
        hit_ball.goto(0,0)
        hit_ball.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write("Left player : {}  Right player : {}".format(left_player, right_player), align="center",
                     font=("Arial", 25, "normal"))
        
    #ball collision
    if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor() + 50 and hit_ball.ycor() > right_pad.ycor() - 50):
        hit_ball.setx(360)
        hit_ball.dx *= -1
        hit_ball.dx *= 1.1
        hit_ball.dy *= 1.1


    if (hit_ball.xcor() < -360 and hit_ball.xcor() > -370) and (hit_ball.ycor() < left_pad.ycor() + 50 and hit_ball.ycor() > left_pad.ycor() - 50):
        hit_ball.setx(-360)
        hit_ball.dx *= -1
        hit_ball.dx *= 1.1
        hit_ball.dy *= 1.1

    #set max speed for ball
    MAX_SPEED = 5

    if abs(hit_ball.dx) > MAX_SPEED:
        hit_ball.dx = MAX_SPEED if hit_ball.dx > 0 else -MAX_SPEED
    if abs(hit_ball.dy) > MAX_SPEED:
        hit_ball.dy = MAX_SPEED if hit_ball.dy > 0 else -MAX_SPEED
