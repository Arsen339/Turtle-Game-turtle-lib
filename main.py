from random import *
import turtle
import math
#Импортируем модули

#Задаем параметры, классы и глобальные переменные
#Параметры экрана
screen_length=700
screen_height=700
#Скорость игрока
global player_speed
player_speed=10
#максимальное количество злаков
global max_food
max_food=20

#массив злаков
global foods
foods=[turtle.Turtle()]*(max_food+1)


#Таблички с надписями
btn1 = turtle.Turtle()
btn2= turtle.Turtle()
btn2.clear()
btn2.hideturtle()
btn2.penup()
btn2.goto(0,230)
btn2.write("Красный-опасная зона", font=("Arial", 12, "normal"))

#Перечень цветов
colors=['green','maroon1','purple1','lime green','blue4','light coral']

#класс для подсчета съеденных злаков
class cereal():
    def __init__(self,count):
        self.count=count
stat=cereal(0)
#класс для подсчета единиц злаков, которые в игре
class FoodAm():
    def __init__(self,food_now):
        self.food_now=food_now
food_stat=FoodAm(0)

#Установим размер окна 
wndow = turtle.Screen()
wndow.title("Screen")
wndow.setup(screen_length,screen_height)

#Объект игрока
player=turtle.Turtle()
player.shape("turtle")
player.color("black","green")




'''def MakeCell():
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
        
        i=i+20'''

    #for i in range(-100,100,10):
     #   line.setpos(-100+i,100)
      #  turtle.right(90)
       # turtle.forward(100)



#Функция для рисования квадрата
def DrawSquare(length,line_color,figure_color,first_x,first_y):
    square = turtle.Turtle()
    square.hideturtle()
    square.penup()
    square.speed(100)
    #Начальная позиция
    square.goto(first_x,first_y)
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
    star.hideturtle()
    star.penup()
    star.speed(100)
    star.goto(first_x,first_y)
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
    polygon.penup()
    polygon.hideturtle()
    polygon.speed(100)
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
    
    spiral.end_fill()


#Рисуем точку
def DrawDot(dot_size,color,x_pos,y_pos):
    
    #Размер, цвет и вид абстрактного исполнителя
    circle = turtle.Turtle()
    circle.speed(1000)
    #Скрывает черепашку
    circle.hideturtle()
    circle.color('white')
    circle.setpos(x_pos, y_pos)
    
    circle.pensize(5)
    circle.pencolor(color)
    circle.dot(dot_size)
    circle.penup()
    circle.pendown()
    
    
   
#Рисуем круг   
def DrawRound(radius,x_pos,y_pos,line_color):
    round=turtle.Turtle() 
    round.hideturtle()
    round.speed(100)
    round.color('cyan')
    round.setpos(x_pos, y_pos)
    round.color(line_color)
    round.pensize(5)
    round.pencolor(line_color)
    round.circle(radius)
    round.penup()
    round.pendown()
    
    








#Функция для создания еды
def MakeFood():
    if food_stat.food_now==0:
        for i in range(max_food):
            foods[i]=turtle.Turtle()
            foods[i].penup()
            foods[i].speed(100)
            foods[i].color("cyan","yellow")
            foods[i].shape("triangle")
            foods[i].goto(randint(-150,150),randint(-150,150))
            food_stat.food_now=food_stat.food_now+1
#функция для перемещения съеденной еды      
def Eaten():
    for i in range(len(foods)-1):
        #if (len(foods))>2:
        if (abs(player.ycor()-foods[i].ycor())<16 and abs(player.xcor()-foods[i].xcor())<16):
            #foods[i].hideturtle
            #foods[i].setx(300)
            #foods[i].sety(300)
            
            foods[i].penup()
            foods[i].setx(screen_length)
            foods[i].sety(screen_height)
            stat.count=stat.count+1
            
            btn1.clear()
            btn1.hideturtle()
            btn1.penup()
            btn1.goto(200,200)
            write_mes=('Score: ',stat.count)
            btn1.write(write_mes, font=("Arial", 12, "normal"))
            food_stat.food_now=food_stat.food_now-1
            
            

            AddFood()
            



#функция для добавления еды
def AddFood():
    if food_stat.food_now==0:
        for i in range(max_food):
            foods[i].penup()
            foods[i].speed(100)
            foods[i].color("cyan","yellow")
            foods[i].shape("triangle")
            foods[i].goto(randint(-150,150),randint(-150,150))

def MakeEnemy():





#Функции движения
def up():
    y = player.ycor() + player_speed
    player.sety(y)
    player.setheading(90)
    Eaten()
def down():
    y = player.ycor() - player_speed
    player.sety(y)
    player.setheading(-90)
    Eaten()
    
def left():
    x = player.xcor() - player_speed
    player.setx(x)
    player.setheading(180)
    Eaten()

def right():
    x = player.xcor() + player_speed
    player.setx(x)
    player.setheading(0)
    Eaten()









#Нарисуем окружение
DrawDot(400,'cyan',0,0)
DrawRound(200,0,-200,'red')
DrawDot(30,'black',0,0)

DrawPolygon(4,50,'brown','brown',-25,-200)
DrawPolygon(4,50,'brown','brown',-25,-250)
for i in range(10):
    DrawStar(5,144,30,'red',choice(colors),randint(-screen_length/2, screen_length/2),randint(-screen_length/2.5, screen_length/2.5))
for i in range(10):
    DrawStar(8,135,30,'red',choice(colors),randint(-screen_length/2, screen_length/2),randint(-screen_length/2.5, screen_length/2.5))
DrawSquare(80,"red",'red',-40,-120)




#Добавим еды
MakeFood()

#считывание нажатий мыши
turtle.listen()
turtle.onkeypress(up, 'Up')
turtle.onkeypress(down, 'Down')
turtle.onkeypress(left, 'Left')
turtle.onkeypress(right, 'Right')



#Завершение
turtle.done()
