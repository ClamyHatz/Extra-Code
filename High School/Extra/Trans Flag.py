import turtle as trtl

painter = trtl.Turtle()

painter.penup()
painter.goto(-500,350)
painter.pendown()
painter.turtlesize(3)
painter.pensize(50)

painter.pencolor("skyblue")
painter.setheading(0)
painter.forward(1000)
painter.setheading(270)
painter.forward(50)
painter.setheading(180)
painter.forward(1000)
painter.setheading(90)
painter.forward(50)
painter.backward(100)
painter.setheading(0)
painter.forward(1000)
painter.setheading(90)
painter.forward(50)
painter.penup()
painter.backward(100)
painter.pendown()

painter.pencolor("pink")
painter.setheading(180)
painter.forward(1000)
painter.setheading(270)
painter.forward(50)
painter.setheading(0)
painter.forward(1000)
painter.setheading(90)
painter.forward(50)
painter.backward(100)
painter.setheading(180)
painter.forward(1000)
painter.setheading(90)
painter.forward(50)
painter.penup()
painter.backward(100)
painter.pendown()

painter.pencolor("white")
painter.setheading(0)
painter.forward(1000)
painter.setheading(270)
painter.forward(50)
painter.setheading(180)
painter.forward(1000)
painter.setheading(90)
painter.forward(50)
painter.backward(100)
painter.setheading(0)
painter.forward(1000)
painter.setheading(90)
painter.forward(50)
painter.penup()
painter.backward(100)
painter.pendown()

painter.pencolor("pink")
painter.setheading(180)
painter.forward(1000)
painter.setheading(270)
painter.forward(50)
painter.setheading(0)
painter.forward(1000)
painter.setheading(90)
painter.forward(50)
painter.backward(100)
painter.setheading(180)
painter.forward(1000)
painter.setheading(90)
painter.forward(50)
painter.penup()
painter.backward(100)
painter.pendown()

painter.pencolor("skyblue")
painter.setheading(0)
painter.forward(1000)
painter.setheading(270)
painter.forward(50)
painter.setheading(180)
painter.forward(1000)
painter.setheading(90)
painter.forward(50)
painter.backward(100)
painter.setheading(0)
painter.forward(1000)
painter.setheading(90)
painter.forward(50)
painter.penup()
painter.backward(100)
painter.pendown()

wn = trtl.Screen()
wn.mainloop()