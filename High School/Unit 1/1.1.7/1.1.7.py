#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []
startx = 0
starty = 0
direction = 45
length = 70
tn = 0
trtl.speed(0)

while(tn < 4):
  # use interesting shapes and colors
  turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
  turtle_colors = ["red", "blue", "green", "orange", "purple", "gold",]

  for s in turtle_shapes:
    t = trtl.Turtle(shape=s)
    item = turtle_colors.pop()
    t.color(item)
    my_turtles.append(t)


  # Gives the starting points


  # Makes the turtles move
  for t in my_turtles:
    t.penup()
    t.goto(startx, starty)
    t.pendown()
    t.setheading(direction)   
    t.forward(length)
    startx = t.xcor()
    starty = t.ycor()
    direction = t.heading() - 65
    length = length + 10

  tn = tn + 1


wn = trtl.Screen()
wn.mainloop()