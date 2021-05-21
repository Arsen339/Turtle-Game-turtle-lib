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
#Скорость врагов
global enemy_speed
enemy_speed=10



#максимальное количество злаков
global max_food
max_food=20

#массив злаков
global foods
foods=[turtle.Turtle()]*(max_food+1)

global max_dangers
max_dangers=20

global dangers
dangers=[turtle.Turtle()]*(max_dangers+1)


#Таблички с надписями
btn1 = turtle.Turtle()
btn2= turtle.Turtle()
btn2.clear()
btn2.hideturtle()
btn2.penup()
btn2.goto(-30,270)
btn2.write("Берегись Квадратиков!Ешь желтые злаки!", font=("Arial", 12, "normal"))
btn3 = turtle.Turtle()




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
global window
window = turtle.Screen()
window.title("Screen")
window.setup(screen_length,screen_height)

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

#Создадим врагов
def MakeEnemy():
    for i in range(5):
        dangers[i]=turtle.Turtle()
        dangers[i].penup()
        dangers[i].goto(-200,randint(-180,180))
        dangers[i].speed(100)
        dangers[i].color("red","black")
        dangers[i].shape("square")
        dangers[i].pensize(5)
        dangers[i].pencolor('red')
    for i in range(5,10):
        dangers[i]=turtle.Turtle()
        dangers[i].penup()
        dangers[i].speed(100)
        dangers[i].color("black","red")
        dangers[i].shape("square")
        dangers[i].goto(200,randint(-180,180))
    for i in range(10,15):
        dangers[i]=turtle.Turtle()
        dangers[i].penup()
        dangers[i].speed(100)
        dangers[i].color("black","red2")
        dangers[i].shape("square")
        dangers[i].goto(randint(-180,180),-200)
    for i in range(15,20):
        dangers[i]=turtle.Turtle()
        dangers[i].penup()
        dangers[i].speed(100)
        dangers[i].color("black","grey26")
        dangers[i].shape("square")
        dangers[i].goto(randint(-180,180),200)

#Передвижение врага
def MoveEnemy():
    for i in range(max_dangers):
        if (i>=0) and (i<5):
            x=dangers[i].xcor()+enemy_speed+randint(0,0)
            dangers[i].setx(x)
        if (i>=5) and (i<10):
            x=dangers[i].xcor()-enemy_speed+randint(0,10)
            dangers[i].setx(x)
        if (i>=10) and(i<15):
            y=dangers[i].ycor()+enemy_speed+randint(0,15)
            dangers[i].sety(y)
        if (i>=15) and(i<20):
            y=dangers[i].ycor()-enemy_speed+randint(0,15)
            dangers[i].sety(y)

def Losing():
    for i in range(max_dangers):
        if abs(dangers[i].xcor()-player.xcor())<10 and abs(dangers[i].ycor()-player.ycor())<10:
        
            btn3.clear()
            btn3.hideturtle()
            btn3.penup()
            btn3.goto(0,0)
            turtle.bye()
            
            btn3.write("Game Over", font=("Arial", 22, "normal"))
            turtle.exitonclick()



#Функции движения
def up():
    y = player.ycor() + player_speed
    player.sety(y)
    player.setheading(90)
    Eaten()
    Losing()

def down():
    y = player.ycor() - player_speed
    player.sety(y)
    player.setheading(-90)
    Eaten()
    Losing()
    
def left():
    x = player.xcor() - player_speed
    player.setx(x)
    player.setheading(180)
    Eaten()
    Losing()

def right():
    x = player.xcor() + player_speed
    player.setx(x)
    player.setheading(0)
    Eaten()
    Losing()









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






#Добавим еды
MakeFood()
MakeEnemy()

#считывание нажатий мыши
turtle.listen()
turtle.onkeypress(up, 'Up')
turtle.onkeypress(down, 'Down')
turtle.onkeypress(left, 'Left')
turtle.onkeypress(right, 'Right')
turtle.onkey(MoveEnemy, 'Up')
turtle.onkey(MoveEnemy, 'Down')
turtle.onkey(MoveEnemy, 'Left')
turtle.onkey(MoveEnemy, 'Right')

#Завершение
turtle.done()
