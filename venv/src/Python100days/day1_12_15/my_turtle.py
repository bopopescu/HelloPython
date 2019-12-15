import turtle
import random
# left() right() is angle, only forward() can move the turtle
turtle.pensize(4)
turtle.pencolor('red')
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
for i in range(30):
    ran=random.randint(10,100)
    turtle.forward(ran)
    turtle.left(ran)
turtle.mainloop()