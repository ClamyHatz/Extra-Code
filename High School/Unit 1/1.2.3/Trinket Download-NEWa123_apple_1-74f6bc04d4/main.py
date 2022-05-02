#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "D:/CSP/Unit 1/1.2.3/Trinket Download-NEWa123_apple_1-74f6bc04d4/apple.gif" # Store the file name of your shape

Continue = "D:/CSP/Unit 1/1.2.3/Trinket Download-NEWa123_apple_1-74f6bc04d4/Continue.gif"

Dio_image = "D:/CSP/Unit 1/1.2.3/Trinket Download-NEWa123_apple_1-74f6bc04d4/Dio.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(Continue)
wn.addshape(Dio_image)
wn.bgpic("D:/CSP/Unit 1/1.2.3/Trinket Download-NEWa123_apple_1-74f6bc04d4/background.gif")

drawer = trtl.Turtle()
drawer.penup()
drawer.hideturtle()

new_letter = "."

letter_list = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

apple_list = []
cletter_list = []

#-----functions-----
#Sets up ending
def Ending(x, y):
  Dio = trtl.Turtle()
  Dio.shape(Dio_image)
  

# Gives the Apple a location and adds it to apple_list
def apple_reset(active_apple):
  global new_xpos
  global new_ypos
  new_xpos = rand.randint(-150, 150)
  new_ypos = rand.randint(0, 150)
  active_apple.goto(new_xpos, new_ypos)
  apple_list.append(active_apple)
  wn.update()

# Draws a letter on the turtle and takes a random letter from letter_list and adds it to cletter_list
def letter(drawlen):
  global new_letter
  global lt_list_length
  lt_list_length = len(letter_list)
  if(lt_list_length != 0):
    run_numb = rand.randint(0, lt_list_length - 1)
    new_letter = letter_list.pop(run_numb)
    cletter_list.append(new_letter)
    drawlen.penup()
    drawlen.hideturtle()
    drawlen.goto(new_xpos-22, new_ypos-50)
    drawlen.color("blue")
    drawlen.write(new_letter, font=("Arial", 55, "bold"))
    wn.update()

# Creates new turtle and calls functions to set up turtle and draws letter
def spawn(active_apple):
  wn.tracer(False)
  active_apple = trtl.Turtle(shape = apple_image)
  active_apple.penup()
  apple_reset(active_apple)
  letter(drawlen)
  wn.tracer(True)

# Spawns first turtle
for i in range(0, 1):
  wn.tracer(False)
  active_apple = trtl.Turtle(shape = apple_image)
  active_apple.penup()
  drawlen = trtl.Turtle()
  apple_reset(active_apple)
  letter(drawlen)
  wn.tracer(True)

# Drops the apple and spawns a new one until letter_list is empty
def apple_drop():
  drawlen.clear()
  capple = apple_list.pop()
  yco = capple.ycor()
  fallH = yco + 150
  capple.setheading(270)
  capple.forward(fallH)
  capple.hideturtle()
  if(lt_list_length != 1):
    spawn(active_apple)
  else:
    drawer.goto(-250, 0)
    drawer.write("Game Finished!", font=("Arial", 55, "bold"))
    ebutton = trtl.Turtle()
    ebutton.shape(Continue)
    ebutton.penup()
    wn.tracer(False)
    ebutton.goto(0, -80)
    wn.tracer(True)
    ebutton.onclick(Ending)
  wn.update()

# ------ Defines many variables that check the current letter for dropping.
def check_apple_a():
  if ("A" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_b():
  if ("B" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_c():
  if ("C" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_d():
  if ("D" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_e():
  if ("E" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_f():
  if ("F" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_g():
  if ("G" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_h():
  if ("H" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_i():
  if ("I" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_j():
  if ("J" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_k():
  if ("K" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_l():
  if ("L" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_m():
  if ("M" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_n():
  if ("N" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_o():
  if ("O" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_p():
  if ("P" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_q():
  if ("Q" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_r():
  if ("R" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_s():
  if ("S" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_t():
  if ("T" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_u():
  if ("U" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_v():
  if ("V" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_w():
  if ("W" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_x():
  if ("X" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_y():
  if ("Y" in cletter_list):
    apple_drop()
    cletter_list.pop(0)

def check_apple_z():
  if ("Z" in cletter_list):
    apple_drop()
    cletter_list.pop(0)


#-----function calls-----
# --- Keypress commands
wn.onkeypress(check_apple_a, "a")
wn.onkeypress(check_apple_b, "b")
wn.onkeypress(check_apple_c, "c")
wn.onkeypress(check_apple_d, "d")
wn.onkeypress(check_apple_e, "e")
wn.onkeypress(check_apple_f, "f")
wn.onkeypress(check_apple_g, "g")
wn.onkeypress(check_apple_h, "h")
wn.onkeypress(check_apple_i, "i")
wn.onkeypress(check_apple_j, "j")
wn.onkeypress(check_apple_k, "k")
wn.onkeypress(check_apple_l, "l")
wn.onkeypress(check_apple_m, "m")
wn.onkeypress(check_apple_n, "n")
wn.onkeypress(check_apple_o, "o")
wn.onkeypress(check_apple_p, "p")
wn.onkeypress(check_apple_q, "q")
wn.onkeypress(check_apple_r, "r")
wn.onkeypress(check_apple_s, "s")
wn.onkeypress(check_apple_t, "t")
wn.onkeypress(check_apple_u, "u")
wn.onkeypress(check_apple_v, "v")
wn.onkeypress(check_apple_w, "w")
wn.onkeypress(check_apple_x, "x")
wn.onkeypress(check_apple_y, "y")
wn.onkeypress(check_apple_z, "z")

wn.listen()
wn.mainloop()