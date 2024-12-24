from turtle import *

speed(0)
bgcolor("black")
color("cyan")
pensize(2)

for i in range(600):
    if i%5==0:
        lt(3)
    fd(200)
    lt(360/5)

done()