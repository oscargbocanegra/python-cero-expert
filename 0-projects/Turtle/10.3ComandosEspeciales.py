import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.speed(10)
t.circle(60)
t.dot(60, "red")
t.hideturtle()
t.circle(70)
t.dot(30, "green")
t.showturtle()
t.circle(100)
t.setx(-200)
t.sety(150)

turtle.done()