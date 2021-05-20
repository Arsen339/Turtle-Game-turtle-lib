import turtle

wndow = turtle.Screen()
wndow.title("Screen & Button")
wndow.setup(500, 500)

btn1 = turtle.Turtle()
btn1.hideturtle()
for i in range(2):
    btn1.fd(80)
    btn1.left(90)
    btn1.fd(30)
    btn1.left(90)
btn1.penup()
btn1.goto(11,7)
btn1.write("Push me", font=("Arial", 12, "normal"))

def btnclick(x, y):
    if 0<x<80 and 0<y<30:
        print("Кнопка нажата!")
        btn1.clear()
        ball = turtle.Turtle()
        turtle.fillcolor("orange")
        turtle.pencolor("purple")
        turtle.shape("circle")

turtle.listen()
turtle.onscreenclick(btnclick, 1)
turtle.done()