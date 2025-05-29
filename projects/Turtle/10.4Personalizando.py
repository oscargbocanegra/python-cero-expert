import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor("red")
s.title("Mi primer programa")

t.shapesize(1,5,10)
t.shapesize(10,5,1)
t.shapesize(1,10,5)
t.shapesize(10,1,5)

t.pensize(20)
t.forward(100)

t.shapesize(3,3,3)
t.fillcolor("orange")
t.pencolor("white")
t.goto(200,-200)

t.color("green", "black")
t.forward(50)

turtle.done()