# /Library/Frameworks/Python.framework/Versions/3.12/bin/python3 draw_turtle.py
# draw turtle

from turtle import *

# square
shape("turtle")
for i in range(4):
  forward(100)
  left(90)

penup()
goto(200, 200)
pendown()


# star
star_color = ["orange", "green", "gold", "blue", "red"]
for i in range(5):
  color(star_color[i])
  forward(200)
  left(144)

penup()
goto(-200, 0)
pendown()



# flower
flower_color = ["red", "orange", "pink", "yellow", "gold"]
for i in range(5):
  color(flower_color[i])
  circle(50)
  left(360/5)
color("green")
right(90)
forward(200)
right(135)
forward(150)
penup()
back(150)
right(90)
pendown()
forward(150)



done()
