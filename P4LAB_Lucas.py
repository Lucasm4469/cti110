import turtle

turtle.speed(0)
turtle.bgcolor('grey')
turtle.color('white')
turtle.width(6)

for i in range(10):
    for j in range(2):
        turtle.forward(100)
        turtle.right(60)
        turtle.forward(100)
        turtle.right(120)
    turtle.right(36)
