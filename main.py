# Импортируем модули
from random import *
import turtle
from DrawingFuns import *
from Parametrs import *
from GamePlayFuns import *


# Нарисуем окружение
draw_dot(400, 'cyan', 0, 0)
draw_round(200, 0, -200, 'red')
draw_dot(30, 'black', 0, 0)
draw_polygon(4, 50, 'brown', 'brown', -25, -200)
draw_polygon(4, 50, 'brown', 'brown', -25, -250)

# нарисуем звездочки
for i in range(10):
    draw_star(5, 144, 30, 'red', choice(colors), randint(-screen_length / 2, screen_length / 2),
              randint(-screen_length / 2.5, screen_length / 2.5))
for i in range(10):
    draw_star(8, 135, 30, 'red', choice(colors), randint(-screen_length / 2, screen_length / 2),
              randint(-screen_length / 2.5, screen_length / 2.5))
# Нарисуем спирали
draw_spiral(20, 5, 144,  "", "gold", 300, -250)
draw_spiral(20, 5, 144,  "", "blue2", -300, 250)
draw_spiral(20, 5, 144,  "", "green2", -300, -250)

# Добавим еды
make_food()
make_enemy()

# считывание нажатий мыши
turtle.listen()
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

# Завершение
turtle.done()
