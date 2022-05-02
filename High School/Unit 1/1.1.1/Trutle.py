import turtle as trtl

painter = trtl.Turtle()

painter.pencolor("pink")
painter.turtlesize(3)
painter.pensize(5)
painter.forward(100)
painter.right(90)
painter.forward(100)
painter.right(90)
painter.forward(100)
painter.right(90)
painter.forward(100)
painter.right(90)

wn = trtl.Screen()
wn.mainloop()