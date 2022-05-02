import turtle as trtl
import random as rand
import keyboard
import time


run_speed = 10

run = trtl.Turtle()
run.speed("fastest")

def go_left():
  run.speed(0)
  run.setheading(180)
  run.speed(2)
  run.forward(run_speed)

def go_right():
  run.speed(0)
  run.setheading(0)
  run.speed(2)
  run.forward(run_speed)

def go_up():
  run.speed(0)
  run.setheading(90)
  run.speed(2)
  run.forward(run_speed)

def go_down():
  run.speed(0)
  run.setheading(270)
  run.speed(2)
  run.forward(run_speed)


wn = trtl.Screen()

wal_numb = 35
walllength = 5

mazemaker = trtl.Turtle()
mazemaker.pencolor("white")
mazemaker.hideturtle()
mazemaker.pensize(5)

wn.tracer(False)

for i in range (wal_numb):
    mazemaker.forward(walllength)
    mazemaker.right(90)
    if (i > 4):
        mazemaker.pencolor("black")
    walllength += 15

mazemaker.penup()
mazemaker.goto(-30.000000000000075, 29.999999999999932)
walllength = 5
mazemaker.pencolor("white")
mazemaker.pensize(7)
mazemaker.setheading(0)

walllength = 65

for i in range (wal_numb):
    gapP = rand.randint(40, walllength - 20)
    mazemaker.penup()
    mazemaker.forward(walllength - gapP + 40)
    mazemaker.pendown()
    mazemaker.backward(40)
    mazemaker.penup()
    mazemaker.forward(gapP)
    mazemaker.pendown()
    walllength += 15
    mazemaker.right(90)

mazemaker.penup()
mazemaker.goto(-30.000000000000075, 29.999999999999932)
walllength = 5
mazemaker.pencolor("black")
mazemaker.pensize(5)
mazemaker.setheading(0)

walllength = 65

for i in range (27):
    gapP = rand.randint(40, walllength - 20)
    mazemaker.penup()
    mazemaker.forward(walllength - gapP)
    mazemaker.right(90)
    mazemaker.pendown()
    mazemaker.backward(30)
    mazemaker.forward(30)
    mazemaker.left(90)
    mazemaker.penup()
    mazemaker.forward(gapP)
    mazemaker.pendown()
    walllength += 15
    mazemaker.right(90)


wn.tracer(True)

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




wn.mainloop()