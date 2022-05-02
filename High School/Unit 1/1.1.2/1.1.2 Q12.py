# import the turtle module
import turtle as trtl

# create the turtle object
painter = trtl.Turtle()

print("making a circle...")

# ask user for a color (such as red, green, blue, pink, purple)
cColor = input("What color should the circle be?")

# ask user for the radius of a circle
cRadius = int(input("What should the radius be?"))

# draw a circle with the radius and line color entered by the user
painter.pencolor(cColor)
painter.circle(cRadius)

# get the screen object and make it persist
wn = trtl.Screen()
wn.mainloop()
