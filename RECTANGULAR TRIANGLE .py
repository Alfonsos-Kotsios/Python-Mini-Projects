from turtle import * 
import math
import turtle

screen = turtle.Screen()
def right_triangle(x,y):
  z=math.sqrt(pow(x,2) + pow(y,2))
  tangent_value = x/y
  angle_in_radians = math.atan(tangent_value)
  angle_in_degrees = math.degrees(angle_in_radians)
  degreess = 180 -angle_in_degrees

  forward(x)
  left(90)
  forward(y)
  left(degreess)
  forward(z)

right_triangle(400,500)
screen.exitonclick()

