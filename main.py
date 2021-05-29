# Импортируем модули
from random import *
import turtle


# Импортируем модули

# Задаем параметры, классы и глобальные переменные
# Параметры экрана
screen_length = 700
screen_height = 700
# Скорость игрока
# global player_speed
player_speed = 10
# Скорость врагов
# global enemy_speed
enemy_speed = 10

# увеличение скорости игрока
# global harden
harden = 0

# максимальное количество злаков
# global max_food
max_food = 20

# массив злаков
# global foods
foods = [turtle.Turtle()] * (max_food + 1)

# максимальное число врагов
# global max_dangers
max_dangers = 20

# массив врагов
# global dangers
dangers = [turtle.Turtle()] * (max_dangers + 1)

# Таблички с надписями
btn1 = turtle.Turtle()
btn2 = turtle.Turtle()
btn2.clear()
btn2.hideturtle()
btn2.penup()
btn2.goto(-120, 290)
btn2.write("Берегись Квадратиков!Ешь желтые злаки!", font=("Arial", 15, "normal"))
btn3 = turtle.Turtle()
btn4 = turtle.Turtle()

# Перечень цветов
colors = ['green', 'maroon1', 'purple1', 'lime green', 'blue4', 'light coral']


class Cereal:
    """Класс для подсчета съеденных злаков"""
    def __init__(self, count, health_update, health):
        self.count = count
        self.health_update = health_update
        self.health = health


stat = Cereal(0, 0, 4)


# класс для подсчета единиц злаков, которые в игре
class FoodAm:
    def __init__(self, food_now):
        self.food_now = food_now


food_stat = FoodAm(0)

# Установим размер окна
# global window
window = turtle.Screen()
window.title("Screen")
window.setup(screen_length, screen_height)

# Объект игрока
player = turtle.Turtle()
player.penup()
player.shape("turtle")
player.color("black", "green")

def draw_square(length, line_color, figure_color, first_x, first_y):
    """Функция для рисования квадрата """
    square = turtle.Turtle()
    square.hideturtle()
    square.penup()
    square.speed(100)
    # Начальная позиция
    square.goto(first_x, first_y)
    # вид абстрактного исполнителя
    square.shape("turtle")
    # задание цвета линии и цвета фигуры
    square.color(line_color, figure_color)
    # начать заливку фигуры
    square.begin_fill()
    # Зададим скорость рисования
    square.speed(1)

    for i in range(4):
        square.forward(length)
        square.right(90)
        # закончить заливку фигуры
    square.end_fill()


def draw_star(angle_am, angle, line_length, line_color, figure_color, first_x, first_y):
    """Рисование звезды """
    star = turtle.Turtle()
    star.hideturtle()
    star.penup()
    star.speed(100)
    star.goto(first_x, first_y)
    star.shape("turtle")
    star.color(line_color, figure_color)
    star.begin_fill()
    for i in range(angle_am):
        star.forward(line_length)
        # поворот на угол
        star.right(angle)
    star.end_fill()


def draw_polygon(num_sides, side_length, line_color, figure_color, first_x, first_y):
    """Функция для рисования многоугольника """
    polygon = turtle.Turtle()
    polygon.penup()
    polygon.hideturtle()
    polygon.speed(100)
    polygon.goto(first_x, first_y)
    angle = 360.0 / num_sides
    polygon.color(line_color, figure_color)
    polygon.begin_fill()
    for i in range(num_sides):
        polygon.forward(side_length)
        polygon.right(angle)
    polygon.end_fill()


def draw_spiral(Multiple_Number, Multiple_Times, angle, line_length, line_color, figure_color, first_x, first_y):
    """ Функция для рисования увеличивающийся фигуры(спираль)"""
    spiral = turtle.Turtle()
    spiral.hideturtle()
    spiral.speed(100)
    spiral.penup()
    spiral.goto(first_x, first_y)
    spiral.color(line_color, figure_color)
    spiral.pendown()
    spiral.begin_fill()
    for i in range(Multiple_Number):
        spiral.forward(i * Multiple_Times)
        spiral.right(angle)

    spiral.end_fill()


def draw_dot(dot_size, color, x_pos, y_pos):
    """Рисует точку """
    # Размер, цвет и вид абстрактного исполнителя
    circle = turtle.Turtle()
    circle.speed(1000)
    # Скрывает черепашку
    circle.hideturtle()
    circle.color('white')
    circle.setpos(x_pos, y_pos)

    circle.pensize(5)
    circle.pencolor(color)
    circle.dot(dot_size)
    circle.penup()
    circle.pendown()


def draw_round(radius, x_pos, y_pos, line_color):
    """Рисует круг """
    rounde = turtle.Turtle()
    rounde.hideturtle()
    rounde.speed(100)
    rounde.color('cyan')
    rounde.setpos(x_pos, y_pos)
    rounde.color(line_color)
    rounde.pensize(5)
    rounde.pencolor(line_color)
    rounde.circle(radius)
    rounde.penup()
    rounde.pendown()

def make_food():
    """Функция для создания еды"""
    if food_stat.food_now == 0:
        for i in range(max_food):
            foods[i] = turtle.Turtle()
            foods[i].penup()
            foods[i].speed(100)
            foods[i].color("cyan", "yellow")
            foods[i].shape("triangle")
            foods[i].goto(randint(-150, 150), randint(-150, 150))
            food_stat.food_now = food_stat.food_now + 1


def eaten():
    """функция для перемещения съеденной еды """
    for i in range(len(foods) - 1):
        # if (len(foods))>2:
        if abs(player.ycor() - foods[i].ycor()) < 16 and abs(player.xcor() - foods[i].xcor()) < 16:

            foods[i].penup()
            foods[i].setx(screen_length)
            foods[i].sety(screen_height)
            stat.health_update = stat.health_update + 1
            stat.count = stat.count + 1
            # надпись о статистике съеденного
            btn1.clear()
            btn1.hideturtle()
            btn1.penup()
            btn1.goto(200, 200)
            write_mes = ('Score: ', stat.count)
            btn1.write(write_mes, font=("Arial", 12, "normal"))
            # увеличение скорости
            harden = stat.count // 10
            if stat.health_update == 10:
                stat.health_update = 0
                stat.health = stat.health + 1
            btn4.clear()
            btn4.hideturtle()
            btn4.penup()
            btn4.goto(-120, 270)
            write_mes_health = ("health: ", stat.health)
            btn4.write(write_mes_health, font=("Arial", 15, "normal"))
            food_stat.food_now = food_stat.food_now - 1
            AddFood()


# функция для добавления еды
def AddFood():
    if food_stat.food_now == 0:
        for i in range(max_food):
            foods[i].penup()
            foods[i].speed(100)
            foods[i].color("cyan", "yellow")
            foods[i].shape("triangle")
            foods[i].goto(randint(-150, 150), randint(-150, 150))


# Создадим врагов
def MakeEnemy():
    for i in range(5):
        dangers[i] = turtle.Turtle()
        dangers[i].penup()
        dangers[i].goto(-200, randint(-180, 180))
        dangers[i].speed(100)
        dangers[i].color("red", "black")
        dangers[i].shape("square")
        dangers[i].pensize(5)
        dangers[i].pencolor('red')
    for i in range(5, 10):
        dangers[i] = turtle.Turtle()
        dangers[i].penup()
        dangers[i].speed(100)
        dangers[i].color("black", "red")
        dangers[i].shape("square")
        dangers[i].goto(200, randint(-180, 180))
    for i in range(10, 15):
        dangers[i] = turtle.Turtle()
        dangers[i].penup()
        dangers[i].speed(100)
        dangers[i].color("green2", "navy")
        dangers[i].shape("square")
        dangers[i].goto(randint(-180, 180), -200)
    for i in range(15, 20):
        dangers[i] = turtle.Turtle()
        dangers[i].penup()
        dangers[i].speed(100)
        dangers[i].color("indian red", "magenta2")
        dangers[i].shape("square")
        dangers[i].goto(randint(-180, 180), 200)


def move_enemy():
    """Передвижение врага """
    for i in range(max_dangers):
        if (i >= 0) and (i < 5):
            x = dangers[i].xcor() + enemy_speed + randint(0, 0) + harden
            dangers[i].setx(x)
        if (i >= 5) and (i < 10):
            x = dangers[i].xcor() - enemy_speed - randint(0, 10) - harden
            dangers[i].setx(x)
        if (i >= 10) and (i < 15):
            y = dangers[i].ycor() + enemy_speed + randint(0, 15) + harden
            dangers[i].sety(y)
        if (i >= 15) and (i < 20):
            y = dangers[i].ycor() - enemy_speed - randint(0, 15) - harden
            dangers[i].sety(y)


def losing():
    """уменьшение жизней и проигрыш """
    for i in range(max_dangers):
        if abs(dangers[i].xcor() - player.xcor()) < 20 and abs(dangers[i].ycor() - player.ycor()) < 20:
            btn4.clear()
            btn4.hideturtle()
            btn4.penup()
            btn4.goto(-120, 270)
            write_mes_health = ("health: ", stat.health)
            btn4.write(write_mes_health, font=("Arial", 15, "normal"))
            stat.health = stat.health - 1
            if stat.health < 1:
                turtle.bye()
        elif (player.xcor() ** 2 + player.ycor() ** 2) > 40000:
            stat.health = stat.health - 1
            btn4.clear()
            btn4.hideturtle()
            btn4.penup()
            btn4.goto(-120, 270)
            write_mes_health = ("health: ", stat.health)
            btn4.write(write_mes_health, font=("Arial", 15, "normal"))
            if stat.health < 1:
                turtle.bye()


# Функция для перезапуска врагов
def respawn_enemy():
    for i in range(max_dangers):
        if dangers[i].xcor() > 600 or dangers[i].xcor() < -600 or dangers[i].ycor() > 600 or dangers[i].ycor() < -600:
            for i in range(5):
                dangers[i].penup()
                dangers[i].goto(-200, randint(-180, 180))
                dangers[i].speed(100)

            for i in range(5, 10):
                dangers[i].penup()
                dangers[i].speed(100)

                dangers[i].goto(200, randint(-180, 180))
            for i in range(10, 15):
                dangers[i].penup()
                dangers[i].speed(100)

                dangers[i].goto(randint(-180, 180), -200)
            for i in range(15, 20):
                dangers[i].penup()
                dangers[i].speed(100)

                dangers[i].goto(randint(-180, 180), 200)


# Функции движения
def up():
    """ Движение вверх"""
    y = player.ycor() + player_speed
    player.sety(y)
    player.setheading(90)
    eaten()
    move_enemy()
    respawn_enemy()
    losing()


def down():
    """ Движение вниз"""
    y = player.ycor() - player_speed
    player.sety(y)
    player.setheading(-90)
    eaten()
    move_enemy()
    respawn_enemy()
    losing()


def left():
    """ Движение вверх"""
    x = player.xcor() - player_speed
    player.setx(x)
    player.setheading(180)
    eaten()
    move_enemy()
    respawn_enemy()
    losing()


def right():
    """ Движение вправо"""
    x = player.xcor() + player_speed
    player.setx(x)
    player.setheading(0)
    eaten()
    move_enemy()
    respawn_enemy()
    losing()


# Нарисуем окружение
draw_dot(400, 'cyan', 0, 0)
draw_round(200, 0, -200, 'red')
draw_dot(30, 'black', 0, 0)

draw_polygon(4, 50, 'brown', 'brown', -25, -200)
draw_polygon(4, 50, 'brown', 'brown', -25, -250)
for i in range(10):
    draw_star(5, 144, 30, 'red', choice(colors), randint(-screen_length / 2, screen_length / 2),
              randint(-screen_length / 2.5, screen_length / 2.5))
for i in range(10):
    draw_star(8, 135, 30, 'red', choice(colors), randint(-screen_length / 2, screen_length / 2),
              randint(-screen_length / 2.5, screen_length / 2.5))
draw_spiral(20, 5, 144, 20, "", "gold", 300, -250)
draw_spiral(20, 5, 144, 20, "", "blue2", -300, 250)
draw_spiral(20, 5, 144, 20, "", "green2", -300, -250)

# Добавим еды
make_food()
MakeEnemy()

# считывание нажатий мыши
turtle.listen()
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

# Завершение
turtle.done()
