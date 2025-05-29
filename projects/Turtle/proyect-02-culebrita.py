import turtle
import time
import random

retraso = .1
marcador = 0
marcador_alto = 0


s = turtle.Screen()
s.setup(650,650)
s.bgcolor('gray')
s.title('Proyecto Serpiente')

snake = turtle.Turtle()
snake.speed()
snake.shape('square')
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'
snake.color('green')

comida = turtle.Turtle()
comida.shape('circle')
comida.color('orange')
comida.penup()
comida.goto(0,100)
comida.speed(0)

cuerpo = []

texto = turtle.Turtle()
texto.speed(0)
texto.color('black')
texto.penup()
texto.hideturtle()
texto.goto(0,-260)
texto.write("Marcador: 0\tMarcador mas alto: 0", align="center", font=("verdana",14,"normal")) 


def up():
    snake.direction = 'up'

def down():
    snake.direction = 'down'
def right():
    snake.direction = 'right'

def left():
    snake.direction = 'left'



def movimiento():
    if snake.direction == 'up':
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == 'down':
        y = snake.ycor()
        snake.sety(y -20)
    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x + 20)
    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x - 20)

s.listen()
s.onkeypress(up, "Up")
s.onkeypress(down, "Down")
s.onkeypress(left, "Left")
s.onkeypress(right, "Right")

while True:
    s.update()

    if snake.xcor() > 300 or snake.xcor() <-300 or snake.ycor() > 300 or snake.ycor() < -300:
        time.sleep(0)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        snake.home()
        snake.direction = 'stop'
        cuerpo.clear()

        marcador = 0 
        texto.clear()
        texto.write("Marcador: {}\tMarcador mas alto: {}".format(marcador,marcador_alto), align="center", font=("verdana",14,"normal"))



    if snake.distance(comida) < 20 :
        x = random.randint(-250,250)
        y = random.randint(-250, 250)
        comida.goto(x,y)

        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape('square')
        nuevo_cuerpo.color('green')
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,0)
        nuevo_cuerpo.speed(0)
        cuerpo.append(nuevo_cuerpo)

        marcador += 10
        if marcador > marcador_alto:
            marcador_alto = marcador
            texto.clear()
            texto.write("Marcador: {}\tMarcador mas alto: {}".format(marcador,marcador_alto), align="center", font=("verdana",14,"normal"))
            print(retraso)

            if marcador == 50:
                retraso/=2
                print(retraso)
            elif marcador == 100:
                retraso/=2
                print(retraso)
            elif marcador == 150:
                retraso/=2
                print(retraso)




    total = len(cuerpo)
    for i in range(total -1, 0, -1):
        x = cuerpo[i-1].xcor()
        y = cuerpo[i-1].ycor()
        cuerpo[i].goto(x,y)
    
    if total > 0:
        x = snake.xcor()
        y = snake.ycor()
        cuerpo[0].goto(x,y)

    movimiento()

    for i in cuerpo:
        if i.distance(snake) < 20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            snake.home()
            cuerpo.clear()
            snake.direction = 'stop'


    time.sleep(retraso)


turtle.done()