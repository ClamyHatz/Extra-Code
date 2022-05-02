# ------ Import items
import turtle as trtl
import keyboard
import time
from turtle import Screen, Turtle

#------ Set Algorithms
walls = []

run_speed = 30

def go_left():
  slime.speed(0)
  slime.setheading(180)
  slime.speed(2)
  slime.forward(run_speed)
  slime.shape(runl_image)
  time.sleep(.05)
  slime.shape(idlel_image)

def go_right():
  slime.speed(0)
  slime.setheading(0)
  slime.speed(2)
  slime.forward(run_speed)
  slime.shape(runr_image)
  time.sleep(.05)
  slime.shape(idler_image)

def go_up():
  slime.speed(0)
  slime.setheading(90)
  slime.speed(2)
  slime.forward(run_speed)
  slime.shape(runu_image)
  time.sleep(.05)
  slime.shape(idleu_image)

def go_down():
  slime.speed(0)
  slime.setheading(270)
  slime.speed(2)
  slime.forward(run_speed)
  slime.shape(rund_image)
  time.sleep(.05)
  slime.shape(idled_image)

columnVal = []
rowVal = []

Colum = -301
while (Colum < 365.5):
  columnVal.append(Colum)
  Colum = Colum + 66.65

Col10 = columnVal.pop()
Col9 = columnVal.pop()
Col8 = columnVal.pop()
Col7 = columnVal.pop()
Col6 = columnVal.pop()
Col5 = columnVal.pop()
Col4 = columnVal.pop()
Col3 = columnVal.pop()
Col2 = columnVal.pop()
Col1 = columnVal.pop()

Row = 293
while (Row > -357):
  rowVal.append(Row)
  Row = Row - 65

Row10 = rowVal.pop()
Row9 = rowVal.pop()
Row8 = rowVal.pop()
Row7 = rowVal.pop()
Row6 = rowVal.pop()
Row5 = rowVal.pop()
Row4 = rowVal.pop()
Row3 = rowVal.pop()
Row2 = rowVal.pop()
Row1 = rowVal.pop()
  
#----- Define Starting Location
startx = -300
starty = 280

#----- Set Screen Size
screen = trtl.Screen()
screen.setup(width=732, height=712)

#----- Pull Image Items

# - Background
#screen.bgpic("D:/CSP/Unit 1/1.1.9/im/ColorMaze.png")

# Loaging ...
Load = "D:/CSP/Unit 1/1.1.9/im/Untitled-1.gif"
screen.addshape(Load)

# - Right
idler_image = "D:/CSP/Unit 1/1.1.9/im/right_idle.gif"
runr_image = "D:/CSP/Unit 1/1.1.9/im/right_run.gif"
screen.addshape(idler_image)
screen.addshape(runr_image)
# - Left
idlel_image = "D:/CSP/Unit 1/1.1.9/im/left_idle.gif"
runl_image = "D:/CSP/Unit 1/1.1.9/im/left_run.gif"
screen.addshape(idlel_image)
screen.addshape(runl_image)
# - Down
idled_image = "D:/CSP/Unit 1/1.1.9/im/down_idle.gif"
rund_image = "D:/CSP/Unit 1/1.1.9/im/down_run.gif"
screen.addshape(idled_image)
screen.addshape(rund_image)
# - Up
idleu_image = "D:/CSP/Unit 1/1.1.9/im/up_idle.gif"
runu_image = "D:/CSP/Unit 1/1.1.9/im/up_run.gif"
screen.addshape(idleu_image)
screen.addshape(runu_image)

# loaiding screen

Lder = trtl.Turtle()
Lder.shape("square")
Lder.turtlesize(2)
Lder.pensize(50)
Lder.color("teal")
Lder.pencolor("teal")
Lder.penup()
Lder.goto(Col3, Row9)
Lder.pendown()
Lder.hideturtle()
LScree = trtl.Turtle(shape=Load)

# ------ Create Turtle
slime = trtl.Turtle(shape=idler_image)
slime.hideturtle()
slime.penup()
slime.setheading(0)
slime.goto(startx, starty)
slime.speed(2)

# ----------------------------- Create Walls

# -------- Row 1
screen.tracer(False)
wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col5, Row1)
wall.turtlesize(3.3)
wall.color("white")
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col7, Row1)
wall.turtlesize(3.3)
wall.color("white")
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col8, Row1)
wall.turtlesize(3.3)
wall.color("white")
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col9, Row1)
wall.turtlesize(3.3)
wall.color("white")
walls.append(wall)

Lder.forward(20)

# -------- Row 2

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col1,Row2)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col2,Row2)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col3,Row2)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col7,Row3)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col8,Row3)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col9,Row3)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col10,Row3)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

Lder.forward(50)

# ----------- Row 4

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col1,Row4)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col2,Row4)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col4,Row4)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col5,Row4)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col10,Row4)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

Lder.forward(50)

# ------------ Row 5

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col2,Row5)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col4,Row5)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col6,Row5)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col7,Row5)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col8,Row5)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

Lder.forward(70)

# ------------ Row 6

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col4,Row6)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col9,Row6)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

Lder.forward(30)

# ------------ Row 7

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col3,Row7)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col5,Row7)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col7,Row7)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col9,Row7)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

Lder.forward(20)

# ------------ Row 8

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col1,Row8)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col3,Row8)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col7,Row8)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

Lder.forward(30)

# ------------- Row 9

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col9,Row9)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

# ---------------- Row 10

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col2,Row10)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col5,Row10)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col7,Row10)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

wall = trtl.Turtle()
wall.shape("square")
wall.hideturtle()
wall.penup()
wall.goto(Col10,Row10)
wall.color("white")
wall.turtlesize(3.3)
walls.append(wall)

Lder.forward(100)

screen.tracer(True)
# --- bringss back images
screen.bgpic("D:/CSP/Unit 1/1.1.9/im/ColorMaze.png")
Lder.clear()
LScree.hideturtle()
slime.showturtle()

#--- Player Key Inputsd
while keyboard.is_pressed('p') == False:
  while (1 == 1):
    
      if keyboard.is_pressed('w') == True:
          go_up()
          time.sleep(.08)

      if keyboard.is_pressed('a') == True:
          go_left()
          time.sleep(.08)


      if keyboard.is_pressed('s') == True:
          go_down()
          time.sleep(.08)


      if keyboard.is_pressed('d') == True:
          go_right()
          time.sleep(.08)

# - wall hits
      for t in walls:
        if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
          CD = slime.heading()
          slime.setheading(CD-180)
          slime.forward(30)