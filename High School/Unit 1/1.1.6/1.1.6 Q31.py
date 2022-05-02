#   a116_buggy_image.py
import turtle as trtl


# Create spider body
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)

# Create spider head
spider.penup()
spider.goto(-10,-10)
spider.pendown()
spider.pencolor("red")
spider.pensize(6)
spider.circle(3)

spider.penup()
spider.goto(10,-10)
spider.pendown()
spider.pencolor("red")
spider.pensize(6)
spider.circle(3)


# Configure spider legs
spider.penup()
spider.pencolor("black")
LegNumb = 8
LegLength = 70
LegAngle = 180 / LegNumb
spider.pensize(5)
Counter = 0

# Draw spider legs
while (Counter < LegNumb - 4):
  spider.goto(0,20)
  spider.pendown()
  spider.setheading(LegAngle*Counter - 45)
  spider.forward(LegLength)
  Counter = Counter + 1
spider.hideturtle()

while (Counter < LegNumb):
  spider.goto(0,20)
  spider.setheading(LegAngle*Counter + 60)
  spider.forward(LegLength)
  Counter = Counter + 1
spider.hideturtle()


wn = trtl.Screen()
wn.mainloop()