# Функции для рисования
import turtle


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


def draw_spiral(multiple_number, multiple_times, angle, line_color, figure_color, first_x, first_y):
    """ Функция для рисования увеличивающийся фигуры(спираль)"""
    spiral = turtle.Turtle()
    spiral.hideturtle()
    spiral.speed(100)
    spiral.penup()
    spiral.goto(first_x, first_y)
    spiral.color(line_color, figure_color)
    spiral.pendown()
    spiral.begin_fill()
    for i in range(multiple_number):
        spiral.forward(i * multiple_times)
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
