# Функции, отвечающие за игровой процесс
import turtle
from Parametrs import *
from random import randint

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
            add_food()


def add_food():
    """Функция для добавления еды """
    if food_stat.food_now == 0:
        for i in range(max_food):
            foods[i].penup()
            foods[i].speed(100)
            foods[i].color("cyan", "yellow")
            foods[i].shape("triangle")
            foods[i].goto(randint(-150, 150), randint(-150, 150))


def make_enemy():
    """ Функция для создания врагов"""
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
