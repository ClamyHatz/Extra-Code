#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:

  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)

  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions

steps = 0
while steps < 30:

  for ht in horiz_turtles:
    for vt in vert_turtles:
      ht.forward(4)
      vt.forward(4)

      if (abs(ht.xcor() - vt.xcor()) < 30):
        if (abs(ht.ycor() - vt.ycor()) < 30):
         cv_color = vt.fillcolor()
         cv_shape = vt.shape()
         ch_color = ht.fillcolor()
         ch_shape = ht.shape()
         vt.fillcolor("white")
         ht.fillcolor("white")
         vt.shape("circle")
         ht.shape("circle")
         ht.backward(4)
         vt.backward(4)
         ht.forward(1)
         vt.forward(1)
         vt.fillcolor(cv_color)
         ht.fillcolor(ch_color)
         vt.shape(cv_shape)
         ht.shape(ch_shape)
  steps = steps + 1


wn = trtl.Screen()
wn.mainloop()