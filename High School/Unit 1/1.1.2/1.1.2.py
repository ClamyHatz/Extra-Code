import turtle as trtl

p = trtl.Turtle()

p.turtlesize(3)
p.pensize(5)

p.pencolor("blue")
p.fillcolor("blue")
p.begin_fill()
p.circle(100, 360, 24)
p.end_fill()
p.penup()
p.forward(100)
p.pendown()
p.pencolor("pink")
p.fillcolor("pink")
p.begin_fill()
p.circle(40, 360, 20)
p.end_fill()


wn = trtl.Screen()
wn.mainloop()