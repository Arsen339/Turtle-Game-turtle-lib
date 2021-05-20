import turtle
#Импортируем модуль turtle

screen_length=500
screen_height=500

#Установим размер окна 
wndow = turtle.Screen()
wndow.title("Screen")
wndow.setup(screen_length,screen_height)



def MakeCell():
    lines=['rr']*12
    for i in range (12):
        lines[i]=turtle.Turtle()
    #line=turtle.Turtle()
    i=-100
    for j in range(0, 12, 1):
        lines[j].hideturtle()
        lines[j].color('white')
        lines[j].setpos(-100+i,100)
        lines[j].speed(1000)
        lines[j].color("black")
        lines[j].right(90)
        lines[j].forward(100)
        
        i=i+20

    #for i in range(-100,100,10):
     #   line.setpos(-100+i,100)
      #  turtle.right(90)
       # turtle.forward(100)



#Функция для рисования квадрата
def DrawSquare(length,line_color,figure_color,first_x,first_y):
    square = turtle.Turtle()
    #Начальная позиция
    turtle.goto(first_x,first_y)
    #вид абстрактного исполнителя
    square.shape("turtle")
    #задание цвета линии и цвета фигуры
    square.color(line_color, figure_color)
    #начать заливку фигуры
    square.begin_fill()
    #Зададим скорость рисования
    square.speed(1)

    for i in range(4):
      square.forward(length)
      square.right(90)
      #закончить заливку фигуры
    square.end_fill()
    

#Рисование звезды
def DrawStar(angle_am,angle,line_length,line_color,figure_color,first_x,first_y):
    star=turtle.Turtle()
    turtle.goto(first_x,first_y)
    star.shape("turtle")
    star.color(line_color, figure_color)
    star.begin_fill()
    for i in range(angle_am):
        star.forward(line_length)
        star.right(angle)
    star.end_fill()

#Функция для рисования многоугольника
def DrawPolygon(num_sides,side_length,line_color,figure_color,first_x,first_y):
    polygon = turtle.Turtle()
    polygon.goto(first_x,first_y)
    angle = 360.0 / num_sides
    polygon.color(line_color, figure_color)
    polygon.begin_fill()
    for i in range(num_sides):
        polygon.forward(side_length)
        polygon.right(angle)
    polygon.end_fill()
    
#Функция для рисования увеличивающийся фигуры(спираль)
def DrawSpiral(Multiple_Number,Multiple_Times,angle,line_length,line_color,figure_color,first_x,first_y):
    spiral = turtle.Turtle()
    spiral.goto(first_x,first_y)
    spiral.color(line_color, figure_color)
    spiral.begin_fill()
    for i in range(Multiple_Number):
        spiral.forward(i * Multiple_Times)
        spiral.right(angle)
    turtle.exitonclick()
    spiral.end_fill()


#Рисуем круг
def DrawCircle(circle,dot_size,radius):
    
    #Размер, цвет и вид абстрактного исполнителя
    circle = turtle.Turtle()
    #Скрывает черепашку
    circle.hideturtle()
    circle.setpos(0, -200)
    #отчищает экран
    turtle.tracer(0, 0) 
    circle.shape("turtle")
    circle.pensize(5)
    circle.pencolor("cyan")

    #Радиус точки. из которой чертится круг
    
    circle.dot(dot_size)
    circle.penup()
    
    circle.pendown()

    circle.circle(radius)
    return circle













MakeCell()




#turtle.done()

#Выход по клику
turtle.exitonclick()