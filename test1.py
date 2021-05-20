import turtle

circ = turtle.Turtle()
circ.shape("circle")
circ.color("orange")
circ.penup()


def up():
    y = circ.ycor() + 10
    circ.sety(y)
#Лямбда-функция, записанная в одну строчку
down = lambda: circ.sety(circ.ycor() - 10)


#Считывание клавиш
turtle.listen()
turtle.onkeypress(up, 'Up')
turtle.onkeypress(down, 'Down')
turtle.done()