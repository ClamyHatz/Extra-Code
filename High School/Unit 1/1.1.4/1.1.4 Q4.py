#   a114_zero_iteration_and_infinite.py
#   Make a zero-iteration condition and follow it with an infinite loop.
#   Include some visual evidence that the second loop is infinite.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

 # What does this do?


# Add a loop with a zero-iteration condition
cat = 0

while (cat > 1):
  painter.goto(0,0)
  painter.right(20)
  painter.forward(80)
  painter.pendown()
  painter.circle(10)
  painter.penup()
  cat = cat + 1

# Add an infinite loop
cat = 1

while (cat > 0):
  painter.goto(0,0)
  painter.right(20)
  painter.forward(80)
  painter.pendown()
  painter.circle(10)
  painter.penup()
  cat = cat + 1

wn = trtl.Screen()
wn.mainloop()
