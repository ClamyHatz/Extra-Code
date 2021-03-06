#   a113_flower_alt_color.py
#   This code draws a flower using modulus
#   to alternate every other color
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

# stem
painter.color("green")
painter.pensize(15)
painter.goto(0, -150)
painter.setheading(90)
painter.forward(100)
#  leaf
painter.setheading(270)
painter.circle(20, 120, 20)
painter.setheading(90)
painter.goto(0, -60)
# rest of stem
painter.forward(60)
painter.setheading(0)

# change pen
painter.penup()
painter.shape("circle")
painter.turtlesize(2)

# draw flower
painter.goto(20,180)
petals = 0
while (petals < 18):
  painter.right(20)
  painter.forward(30)
  painter.color("darkorchid")
  rem = petals % 2
  if (rem == 0):
    painter.color("blue")
  rem = petals % 4
  if (rem == 0):
    painter.color("pink")
  painter.stamp()
  petals = petals + 1

#draw flower 2
painter.goto(20,160)
petals = 0
while (petals < 15):
  painter.right(25)
  painter.forward(30)
  painter.color("yellow")
  rem = petals % 2
  if (rem == 0):
    painter.color("red")
  rem = petals % 4
  if (rem == 0):
    painter.color("orange")
  painter.stamp()
  petals = petals + 1

  
wn = trtl.Screen()
wn.mainloop()