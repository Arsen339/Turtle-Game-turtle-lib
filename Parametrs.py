# Задаем параметры, классы и глобальные переменные
import turtle


# Параметры экрана
screen_length = 700
screen_height = 700

# Скорость игрока
player_speed = 10

# Скорость врагов
enemy_speed = 10

# увеличение скорости игрока
harden = 0

# максимальное количество злаков
max_food = 20

# массив злаков
foods = [turtle.Turtle()] * (max_food + 1)

# максимальное число врагов
max_dangers = 20

# массив врагов
dangers = [turtle.Turtle()] * (max_dangers + 1)

# Перечень цветов
colors = ['green', 'maroon1', 'purple1', 'lime green', 'blue4', 'light coral']


class Cereal:
    """Класс для подсчета съеденных злаков"""
    def __init__(self, count, health_update, health):
        self.count = count
        self.health_update = health_update
        self.health = health


stat = Cereal(0, 0, 10)


# класс для подсчета единиц злаков, которые в игре
class FoodAm:
    def __init__(self, food_now):
        self.food_now = food_now


food_stat = FoodAm(0)

# Установим размер окна
window = turtle.Screen()
window.title("Screen")
window.setup(screen_length, screen_height)

# Объект игрока
player = turtle.Turtle()
player.penup()
player.shape("turtle")
player.color("black", "green")

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