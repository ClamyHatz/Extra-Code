#   a113_circle_of_circles.py
#   Modify this code to draw a circle of cirlces
import turtle as trtl

painter = trtl.Turtle()

count = 0

while (count < 18):
    painter.shape("circle")
    painter.forward(20)
    painter.right(20)
    painter.stamp()
    count = count + 1

wn = trtl.Screen()
wn.mainloop()