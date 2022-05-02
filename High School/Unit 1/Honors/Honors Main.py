# ------ Import items
import turtle as trtl
import keyboard
import time

#------ Set Algorithms
walls = []
swall = []
trapslist = []
traper = []
buttons = []

bt1 = []
bt2 = []
bt3 = []
wbt1 = []
wbt2 = []
wbt3 = []
tbw = []

run_speed = 33.25

def go_left():
  screen.tracer(False)
  maze.speed(0)
  maze.setheading(0)
  maze.speed(2)
  maze.forward(run_speed)
  for t in walls:
    t.speed(0)
    t.setheading(0)
    t.speed(2)
    t.forward(run_speed)
  for t in traper:
    t.speed(0)
    t.setheading(0)
    t.speed(2)
    t.forward(run_speed)
  for t in buttons:
    t.speed(0)
    t.setheading(0)
    t.speed(2)
    t.forward(run_speed)
  for t in tbw:
    t.speed(0)
    t.setheading(0)
    t.speed(2)
    t.forward(run_speed)
  Lader.speed(0)
  Lader.setheading(0)
  Lader.speed(2)
  Lader.forward(run_speed)
  slime.setheading(180)
  screen.tracer(True)
  slime.shape(runl_image)
  time.sleep(.05)
  slime.shape(idlel_image)

def go_right():
  screen.tracer(False)
  maze.speed(0)
  maze.setheading(180)
  maze.speed(2)
  maze.forward(run_speed)
  for t in walls:
    t.speed(0)
    t.setheading(180)
    t.speed(2)
    t.forward(run_speed)
  for t in traper:
    t.speed(0)
    t.setheading(180)
    t.speed(2)
    t.forward(run_speed)
  for t in buttons:
    t.speed(0)
    t.setheading(180)
    t.speed(2)
    t.forward(run_speed)
  for t in tbw:
    t.speed(0)
    t.setheading(180)
    t.speed(2)
    t.forward(run_speed)
  Lader.speed(0)
  Lader.setheading(180)
  Lader.speed(2)
  Lader.forward(run_speed)
  slime.setheading(0)
  screen.tracer(True)
  slime.shape(runr_image)
  time.sleep(.05)
  slime.shape(idler_image)

def go_up():
  screen.tracer(False)
  maze.speed(0)
  maze.setheading(270)
  maze.speed(2)
  maze.forward(run_speed)
  for t in walls:
    t.speed(0)
    t.setheading(270)
    t.speed(2)
    t.forward(run_speed)
  for t in traper:
    t.speed(0)
    t.setheading(270)
    t.speed(2)
    t.forward(run_speed)
  for t in buttons:
    t.speed(0)
    t.setheading(270)
    t.speed(2)
    t.forward(run_speed)
  for t in tbw:
    t.speed(0)
    t.setheading(270)
    t.speed(2)
    t.forward(run_speed)
  Lader.speed(0)
  Lader.setheading(270)
  Lader.speed(2)
  Lader.forward(run_speed)
  slime.setheading(90)
  screen.tracer(True)
  slime.shape(runu_image)
  time.sleep(.05)
  slime.shape(idleu_image)

def go_down():
  screen.tracer(False)
  maze.speed(0)
  maze.setheading(90)
  maze.speed(2)
  maze.forward(run_speed)
  for t in walls:
    t.speed(0)
    t.setheading(90)
    t.speed(2)
    t.forward(run_speed)
  for t in traper:
    t.speed(0)
    t.setheading(90)
    t.speed(2)
    t.forward(run_speed)
  for t in buttons:
    t.speed(0)
    t.setheading(90)
    t.speed(2)
    t.forward(run_speed)
  for t in tbw:
    t.speed(0)
    t.setheading(90)
    t.speed(2)
    t.forward(run_speed)
  Lader.speed(0)
  Lader.setheading(90)
  Lader.speed(2)
  Lader.forward(run_speed)
  slime.setheading(270)
  screen.tracer(True)
  slime.shape(rund_image)
  time.sleep(.05)
  slime.shape(idled_image)


columnVal = []
rowVal = []

Colum = 0
while (Colum < 599.9):
  columnVal.append(Colum)
  Colum = Colum + 66.6525

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

Row = -2.5
while (Row > -652.5):
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

#----- Set Screen Size
screen = trtl.Screen()
screen.setup(width=1031, height=675)

#----- Pull Image Items
# - Cut Sceen Stuff

spikes = "D:/CSP/Unit 1/Honors/Spike.gif"
screen.addshape(spikes)

level1 = "D:/CSP/Unit 1/Honors/level1.gif"
screen.addshape(level1)
level2 = "D:/CSP/Unit 1/Honors/level2.gif"
screen.addshape(level2)
level3 = "D:/CSP/Unit 1/Honors/level3.gif"
screen.addshape(level3)
level4 = "D:/CSP/Unit 1/Honors/level4.gif"
screen.addshape(level4)
level5 = "D:/CSP/Unit 1/Honors/level5.gif"
screen.addshape(level5)

# - Level Elements
Ladder = "D:/CSP/Unit 1/Honors/Ladder.gif"
screen.addshape(Ladder)
Dark = "D:/CSP/Unit 1/Honors/Darness.gif"
screen.addshape(Dark)

# - Background
Map1 = "D:/CSP/Unit 1/Honors/Map 1.gif"
Map2 = "D:/CSP/Unit 1/Honors/Map 2.gif"
Map3 = "D:/CSP/Unit 1/Honors/Map3.gif"
Map4 = "D:/CSP/Unit 1/Honors/Map4.gif"
Map5 = "D:/CSP/Unit 1/Honors/Map5.gif"
screen.addshape(Map1)
screen.addshape(Map2)
screen.addshape(Map3)
screen.addshape(Map4)
screen.addshape(Map5)

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

# ----------------------------- Create Walls
def wallsLevel1():
    screen.tracer(False)

    for i in range(0, 35):
        wall = trtl.Turtle()
        wall.shape("square")
        wall.penup()
        wall.turtlesize(3.3)
        wall.color("black")
        swall.append(wall)

    # -------- Row 1
    cwall = swall.pop()
    cwall.goto(Col5, Row1)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col7, Row1)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col8, Row1)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col9, Row1)
    walls.append(cwall)

    # -------- Row 2
    cwall = swall.pop()
    cwall.goto(Col1,Row2)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col2,Row2)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col3,Row2)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col7,Row3)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col8,Row3)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col9,Row3)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col10,Row3)
    walls.append(cwall)

    # ----------- Row 4

    cwall = swall.pop()
    cwall.goto(Col1,Row4)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col2,Row4)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col4,Row4)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col5,Row4)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col10,Row4)
    walls.append(cwall)

    # ------------ Row 5

    cwall = swall.pop()
    cwall.goto(Col2,Row5)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col4,Row5)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col6,Row5)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col7,Row5)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col8,Row5)
    walls.append(cwall)

    # ------------ Row 6
    cwall = swall.pop()
    cwall.goto(Col4,Row6)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col9,Row6)
    walls.append(cwall)

    # ------------ Row 7
    cwall = swall.pop()
    cwall.goto(Col3,Row7)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col5,Row7)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col7,Row7)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col9,Row7)
    walls.append(cwall)

    # ------------ Row 8
    cwall = swall.pop()
    cwall.goto(Col1,Row8)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col3,Row8)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col7,Row8)
    walls.append(cwall)

    # ------------- Row 9
    cwall = swall.pop()
    cwall.goto(Col9,Row9)
    walls.append(cwall)

    # ---------------- Row 10
    cwall = swall.pop()
    cwall.goto(Col2,Row10)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col5,Row10)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col7,Row10)
    walls.append(cwall)

    cwall = swall.pop()
    cwall.goto(Col10,Row10)
    walls.append(cwall)

    screen.tracer(True)

def wallsLevel2():

  screen.tracer(False)

  for i in range(0, 42):
    wall = trtl.Turtle()
    wall.shape("square")
    wall.penup()
    wall.turtlesize(3.3)
    wall.color("black")
    swall.append(wall)

  cwall = swall.pop()
  cwall.goto(Col3, Row1)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col10, Row1)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col1, Row2)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col3, Row2)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col5, Row2)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col6, Row2)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col7, Row2)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col8, Row2)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col1, Row3)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col1, Row3)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col3, Row3)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col9, Row3)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col1, Row4)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col4, Row4)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col5, Row4)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col6, Row4)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col8, Row4)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col9, Row4)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col9, Row5)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col2, Row6)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col3, Row6)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col5, Row6)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col5, Row6)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col6, Row6)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col7, Row6)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col9, Row6)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col5, Row7)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col1, Row8)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col2, Row8)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col3, Row8)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col5, Row8)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col6, Row8)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col7, Row8)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col8, Row8)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col10, Row8)
  walls.append(cwall)
    
  cwall = swall.pop()
  cwall.goto(Col3, Row9)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col5, Row9)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col10, Row9)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col1, Row10)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col7, Row10)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col8, Row10)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col10, Row10)
  walls.append(cwall)
def trapsLevel2():

  screen.tracer(False)

  for i in range(0, 4):
    trap = trtl.Turtle()
    trap.shape(spikes)
    trap.penup()
    trap.hideturtle()
    trapslist.append(trap)
  
  ctrap = trapslist.pop()
  ctrap.goto(Col2, Row5)
  traper.append(ctrap)

  ctrap = trapslist.pop()
  ctrap.goto(Col8, Row6)
  traper.append(ctrap)

  ctrap = trapslist.pop()
  ctrap.goto(Col4, Row9)
  traper.append(ctrap)

  ctrap = trapslist.pop()
  ctrap.goto(Col9, Row10)
  traper.append(ctrap)

def wallsLevel3():
  screen.tracer(False)

  for i in range(0, 37):
    wall = trtl.Turtle()
    wall.shape("square")
    wall.penup()
    wall.turtlesize(3.3)
    wall.color("black")
    swall.append(wall)
  
  cwall = swall.pop()
  cwall.goto(Col6, Row1)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col2, Row2)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col3, Row2)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col6, Row2)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col8, Row2)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col9, Row2)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col10, Row2)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col4, Row3)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col6, Row3)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col2, Row4)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col2, Row4)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col4, Row4)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col6, Row4)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col7, Row4)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col8, Row4)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col2, Row5)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col4, Row5)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col6, Row5)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col2, Row6)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col4, Row6)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col8, Row6)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col9, Row6)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col10, Row6)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col2, Row7)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col4, Row7)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col6, Row7)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col3, Row8)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col6, Row8)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col8, Row8)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col9, Row8)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col2, Row9)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col6, Row9)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col8, Row9)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col2, Row10)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col4, Row10)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col8, Row10)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col10, Row10)
  walls.append(cwall)
def trapsLevel3():
  screen.tracer(False)

  for i in range(0, 7):
    trap = trtl.Turtle()
    trap.shape(spikes)
    trap.penup()
    trap.hideturtle()
    trapslist.append(trap)

  ctrap = trapslist.pop()
  ctrap.goto(Col10, Row4)
  traper.append(ctrap)

  ctrap = trapslist.pop()
  ctrap.goto(Col3, Row6)
  traper.append(ctrap)

  ctrap = trapslist.pop()
  ctrap.goto(Col6, Row6)
  traper.append(ctrap)

  ctrap = trapslist.pop()
  ctrap.goto(Col2, Row8)
  traper.append(ctrap)

  ctrap = trapslist.pop()
  ctrap.goto(Col10, Row8)
  traper.append(ctrap)

  ctrap = trapslist.pop()
  ctrap.goto(Col1, Row9)
  traper.append(ctrap)

  ctrap = trapslist.pop()
  ctrap.goto(Col3, Row9)
  traper.append(ctrap)

def trapsLevel4():
    screen.tracer(False)

    for i in range(0, 35):
      trap = trtl.Turtle()
      trap.shape(spikes)
      trap.penup()
      trap.hideturtle()
      trapslist.append(trap)

    # -------- Row 1
    ctrap = trapslist.pop()
    ctrap.goto(Col5, Row1)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col7, Row1)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col8, Row1)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col9, Row1)
    traper.append(ctrap)

    # -------- Row 2
    ctrap = trapslist.pop()
    ctrap.goto(Col1,Row2)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col2,Row2)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col3,Row2)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col7,Row3)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col8,Row3)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col9,Row3)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col10,Row3)
    traper.append(ctrap)

    # ----------- Row 4

    ctrap = trapslist.pop()
    ctrap.goto(Col1,Row4)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col2,Row4)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col4,Row4)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col5,Row4)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col10,Row4)
    traper.append(ctrap)

    # ------------ Row 5

    ctrap = trapslist.pop()
    ctrap.goto(Col2,Row5)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col4,Row5)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col6,Row5)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col7,Row5)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col8,Row5)
    traper.append(ctrap)

    # ------------ Row 6
    ctrap = trapslist.pop()
    ctrap.goto(Col4,Row6)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col9,Row6)
    traper.append(ctrap)

    # ------------ Row 7
    ctrap = trapslist.pop()
    ctrap.goto(Col3,Row7)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col5,Row7)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col7,Row7)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col9,Row7)
    traper.append(ctrap)

    # ------------ Row 8
    ctrap = trapslist.pop()
    ctrap.goto(Col1,Row8)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col3,Row8)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col7,Row8)
    traper.append(ctrap)

    # ------------- Row 9
    ctrap = trapslist.pop()
    ctrap.goto(Col9,Row9)
    traper.append(ctrap)

    # ---------------- Row 10
    ctrap = trapslist.pop()
    ctrap.goto(Col2,Row10)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col5,Row10)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col7,Row10)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col10,Row10)
    traper.append(ctrap)

    screen.tracer(True)

def wallsLevel5():
  screen.tracer(False)

  for i in range(0, 38):
    wall = trtl.Turtle()
    wall.shape("square")
    wall.penup()
    wall.turtlesize(3.3)
    wall.color("black")
    swall.append(wall)
  
  cwall = swall.pop()
  cwall.goto(Col6, Row1)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col8, Row1)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col1, Row2)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col2, Row2)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col4, Row2)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col6, Row2)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col8, Row2)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col10, Row2)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col4, Row3)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col6, Row3)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col1, Row4)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col2, Row4)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col4, Row4)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col6, Row4)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col8, Row4)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col9, Row4)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col10, Row4)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col6, Row5)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col10, Row5)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col2, Row6)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col3, Row6)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col4, Row6)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col5, Row6)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col6, Row6)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col7, Row6)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col8, Row6)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col10, Row6)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col3, Row7)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col10, Row7)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col3, Row8)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col6, Row8)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col7, Row8)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col8, Row8)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col10, Row8)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col5, Row9)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col7, Row10)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col8, Row10)
  walls.append(cwall)

  cwall = swall.pop()
  cwall.goto(Col9, Row10)
  walls.append(cwall)
def trapsLevel5():
    screen.tracer(False)

    for i in range(0, 35):
      trap = trtl.Turtle()
      trap.shape(spikes)
      trap.penup()
      trap.hideturtle()
      trapslist.append(trap)
    '''
    ctrap = trapslist.pop()
    ctrap.goto(Col7, Row1)
    traper.append(ctrap)
    '''
    ctrap = trapslist.pop()
    ctrap.goto(Col5, Row3)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col10, Row3)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col4, Row7)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col2, Row8)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col2, Row10)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col6, Row10)
    traper.append(ctrap)

    ctrap = trapslist.pop()
    ctrap.goto(Col10, Row10)
    traper.append(ctrap)
def buttonsLevel5():
  b1 = trtl.Turtle()
  b1.shape("square")
  b1.penup()
  b1.turtlesize(3.3)
  b1.color("blue")
  b1.hideturtle()
  b1.goto(Col10, Row1)
  bt1.append(b1)
  buttons.append(b1)
  wb1 = trtl.Turtle()
  wb1.shape("square")
  wb1.penup()
  wb1.turtlesize(3.3)
  wb1.color("black")
  wb1.goto(Col2, Row3)
  wbt1.append(wb1)
  walls.append(wb1)

  b2 = trtl.Turtle()
  b2.shape("square")
  b2.penup()
  b2.turtlesize(3.3)
  b2.color("blue")
  b2.hideturtle()
  b2.goto(Col7, Row2)
  bt2.append(b2)
  buttons.append(b2)
  wb2 = trtl.Turtle()
  wb2.shape("square")
  wb2.penup()
  wb2.turtlesize(3.3)
  wb2.color("black")
  wb2.goto(Col7, Row3)
  wb2.hideturtle()
  wbt2.append(wb2)
  tbw.append(wb2)

  b3 = trtl.Turtle()
  b3.shape("square")
  b3.penup()
  b3.turtlesize(3.3)
  b3.color("blue")
  b3.hideturtle()
  b3.goto(Col8, Row9)
  bt3.append(b3)
  buttons.append(b3)
  wb3 = trtl.Turtle()
  wb3.shape("square")
  wb3.penup()
  wb3.turtlesize(3.3)
  wb3.color("black")
  wb3.goto(Col9, Row9)
  wb3.hideturtle()
  wbt3.append(wb3)
  tbw.append(wb3)

# -- Switch to out side
wallsLevel1()

screen.tracer(False)
lev1 = trtl.Turtle(shape = level1)
lev1.penup()
lev1.setposition(0, 200)

LevS = 2

screen.bgcolor("black")

maze = trtl.Turtle(shape = Map1)
maze.penup()
maze.goto(300, -295)

Lader = trtl.Turtle(shape=Ladder)
Lader.penup()
Lader.goto(Col6, Row10)

slime = trtl.Turtle(shape=idler_image)
slime.penup()
slime.setheading(0)
slime.speed(2)

dark = trtl.Turtle(shape = Dark)
dark.hideturtle()

lev2 = trtl.Turtle(shape = level3)
lev2.penup()
lev2.goto(0, 200)
lev2.hideturtle()
screen.tracer(True)

# - Player Key Inputsd
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

    for t in walls:
        if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
            screen.tracer(False)
            CD = maze.heading()
            maze.setheading(CD-180)
            maze.forward(run_speed)
            for t in walls:
              t.speed(0)
              t.setheading(CD-180)
              t.speed(2)
              t.forward(run_speed)
            for t in traper:
              t.speed(0)
              t.setheading(CD-180)
              t.speed(2)
              t.forward(run_speed)
            for t in buttons:
              t.speed(0)
              t.setheading(CD-180)
              t.speed(2)
              t.forward(run_speed)
            for t in tbw:
              t.speed(0)
              t.setheading(CD-180)
              t.speed(2)
              t.forward(run_speed)
            Lader.speed(0)
            Lader.setheading(CD-180)
            Lader.speed(2)
            Lader.forward(run_speed)
            screen.tracer(True)

    if (0 < (abs(Lader.ycor() - slime.ycor())) < 50) and (0 < (abs(Lader.xcor() - slime.xcor())) < 50):
        screen.tracer(False)
        for i in walls:
            i.reset()
            i.hideturtle()
        for r in traper:
            r.reset()
            r.hideturtle()
        for r in buttons:
            r.reset()
            r.hideturtle()
        for r in tbw:
            r.reset()
            r.hideturtle()
        if (LevS < 3):
          walls.clear()
          traper.clear()
          lev1.shape(level2)
          maze.goto(300, -295)
          maze.shape(Map2)
          Lader.goto(Col1, Row9)
          slime.shape(idler_image)
          slime.goto(Col1, Row1)
          wallsLevel2()
          trapsLevel2()
          LevS = 3
          screen.tracer(True)
        elif (LevS < 4):
          walls.clear()
          traper.clear()
          wallsLevel3()
          trapsLevel3()
          maze.goto(300, -295)
          maze.shape(Map3)
          Lader.goto(Col10, Row1)
          slime.shape(idler_image)
          slime.goto(Col1, Row1)
          dark.showturtle()
          lev2.showturtle()
          lev1.hideturtle()
          LevS = 4
          screen.tracer(True)
        elif (LevS < 5):
          screen.tracer(False)
          walls.clear()
          traper.clear()
          maze.goto(300, -295)
          maze.shape(Map4)
          Lader.goto(Col6, Row10)
          slime.shape(idler_image)
          slime.goto(Col1, Row1)
          lev2.shape(level4)
          trapsLevel4()
          LevS = 5
          screen.tracer(True)
        elif (LevS < 6):
          screen.tracer(False)
          walls.clear()
          traper.clear()
          tbw.clear()
          buttons.clear()
          maze.goto(300, -295)
          maze.shape(Map5)
          Lader.goto(Col1, Row3)
          slime.shape(idler_image)
          slime.goto(Col1, Row1)
          lev2.shape(level5)
          wallsLevel5()
          trapsLevel5()
          buttonsLevel5()
          LevS = 6
          screen.tracer(True)

    for t in traper:
        if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
          t.showturtle()
          time.sleep(.5)
          screen.tracer(False)
          for i in walls:
              i.reset()
              i.hideturtle()
          for r in traper:
              r.reset()
              r.hideturtle()
          for r in buttons:
              r.reset()
              r.hideturtle()
          if (LevS < 4):
            walls.clear()
            traper.clear()
            lev1.shape(level2)
            maze.goto(300, -295)
            maze.shape(Map2)
            Lader.goto(Col1, Row9)
            slime.shape(idler_image)
            slime.goto(Col1, Row1)
            wallsLevel2()
            trapsLevel2()
            print(LevS)
            screen.tracer(True)
          elif (LevS < 5):
            walls.clear()
            traper.clear()
            lev1.shape(level3)
            maze.goto(300, -295)
            wallsLevel3()
            trapsLevel3()
            maze.shape(Map3)
            Lader.goto(Col10, Row1)
            slime.shape(idler_image)
            slime.goto(Col1, Row1)
            dark.showturtle()
            lev2.showturtle()
            lev1.hideturtle()
            screen.tracer(True)
          elif (LevS < 6):
            screen.tracer(False)
            walls.clear()
            traper.clear()
            maze.goto(300, -295)
            maze.shape(Map4)
            Lader.goto(Col6, Row10)
            slime.shape(idler_image)
            slime.goto(Col1, Row1)
            lev2.shape(level4)
            LevS = 5
            trapsLevel4()
            screen.tracer(True)
          elif (LevS < 7):
            screen.tracer(False)
            tbw.clear()
            buttons.clear()
            walls.clear()
            traper.clear()
            maze.goto(300, -295)
            maze.shape(Map5)
            Lader.goto(Col1, Row3)
            slime.shape(idler_image)
            slime.goto(Col1, Row1)
            lev2.shape(level5)
            wallsLevel5()
            trapsLevel5()
            buttonsLevel5()
            LevS = 6
            screen.tracer(True)

    for t in bt1:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        screen.tracer(False)
        bt1.clear()
        for t in wbt1:
          t.reset()
          t.hideturtle()
          wee = walls.index(t)
          walls.pop(wee)
        screen.tracer(True)
    for t in bt2:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        screen.tracer(False)
        bt2.clear()
        go_up()
        go_up()
        for t in wbt2:
          t.showturtle()
          wa = tbw.index(t)
          tbw.pop(wa)
          walls.append(t)
        screen.tracer(True)
    for t in bt3:
      if (0 < (abs(t.ycor() - slime.ycor())) < 50) and (0 < (abs(t.xcor() - slime.xcor())) < 50):
        screen.tracer(False)
        bt3.clear()
        go_left()
        go_left()
        for t in wbt3:
          t.showturtle()
          wa = tbw.index(t)
          tbw.pop(wa)
          walls.append(t)
        screen .tracer(True)

screen.listen()
screen.mainloop()
