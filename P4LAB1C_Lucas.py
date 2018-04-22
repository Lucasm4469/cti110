import turtle

myPen = turtle.Turtle()
myPen.shape('turtle')
myPen.speed(350)

myPen.color('#3333ff')

myPen.left(90)

for i in range(0,6):
    myPen.forward(100)
    myPen.forward(-40)
    myPen.left(40)
    myPen.forward(30)
    myPen.forward(-30)
    myPen.right(80)
    myPen.forward(30)
    myPen.forward(-30)
    myPen.left(40)
    myPen.forward(-60)

    myPen.right(60)


