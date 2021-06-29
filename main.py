# the beginning of training for drawing

import graphics as gr

x = int(input("Введите желаемую ширину окошка рисунка:"))
y = x / 2
window = gr.GraphWin("Черчу верчу", x, y)


def circle_drw(cord_x, cord_y, radius, line_width, outline_colour, fill_colour):
    circle = gr.Circle(gr.Point(cord_x, cord_y), radius)
    circle.setOutline(outline_colour)
    circle.setWidth(line_width)
    circle.setFill(fill_colour)
    circle.draw(window)
    return ()


def rectangle_drw(center_point_x, center_point_y, width, height, line_width, outline_color, fill_color):
    start_point_x = center_point_x - width / 2
    start_point_y = center_point_y - height / 2
    end_point_x = center_point_x + width / 2
    end_point_y = center_point_y + height / 2
    rectangle = gr.Rectangle(gr.Point(start_point_x, start_point_y), (gr.Point(end_point_x, end_point_y)))
    rectangle.setOutline(outline_color)
    rectangle.setWidth(line_width)
    rectangle.setFill(fill_color)
    rectangle.draw(window)
    return ()


def line_drw(start_point_x, start_point_y, end_point_x, end_point_y, line_width, outline_color):
    line = gr.Line(gr.Point(start_point_x, start_point_y), gr.Point(end_point_x, end_point_y))
    line.setOutline(outline_color)
    line.setWidth(line_width)
    line.draw(window)
    return ()


def triangle_drw(center_point_x, center_point_y, base_length, height, line_width, outline_color,
                 fill_color):  # center_point_y = start_point_y
    start_point_x = center_point_x - base_length / 2
    end_point_x = center_point_x + base_length / 2
    end_point_y = center_point_y - height
    triangle = gr.Polygon(gr.Point(start_point_x, center_point_y), gr.Point(center_point_x, end_point_y),
                          gr.Point(end_point_x, center_point_y))
    triangle.setOutline(outline_color)
    triangle.setWidth(line_width)
    triangle.setFill(fill_color)
    triangle.draw(window)
    return ()


def background_set_up():
    rectangle_drw(x / 2, y * 0.25, x, y / 2, 2, "blue", "blue")  # background top
    rectangle_drw(x / 2, y * 0.75, x, y / 2, 2, "Lightgray", "Lightgray")  # background bottom
    return ()


def window_drw():
    rectangle_drw(x * 0.25, y * 0.5, x / 14, x / 14, x * 0.003, "black", "yellow")
    line_drw((x * 0.25 + x / 28), y * 0.5, (x * 0.25 - x / 28), y * 0.5, x // 310, "black")
    line_drw(x * 0.25, (y * 0.5 + x / 28), x * 0.25, (y * 0.5 - x / 28), x // 310, "black")
    return ()


def house_drw():
    rectangle_drw(x * 0.25, y * 0.5, x / 6, y / 3, x // 300, "black", "gray")  # the box depends on screen size
    triangle_drw(x * 0.25, (y * 0.5 - y / 6), x / 6, y / 5, x // 250, "black", "red")  # the roof depends on screen size
    window_drw()
    return ()


def clouds_drw():
    for i in range(5):
        if i == 0:
            step_x = 0.625
            step_y = 1
        elif i == 1:
            step_x = 0.875
            step_y = 1
        else:
            step_x = i * 0.25
            step_y = 1.5
        circle_drw(x * 0.1 * step_x, y * 0.1 * step_y, x // 40, x // 550, "black", "white")
    return ()


def spruce_drw():
    for i in range(0, 3, 1):
        if i == 0:
            step = 1.5
        elif i == 1:
            step = 1.25
        else:
            step = 1
        triangle_drw(x * 0.65, (y * 0.5 * step), x / 6, y / 5, x // 250, "black", "green")
        if i == 3:
            break
    rectangle_drw(x * 0.65, y * 0.5 * 1.5 + y // 20, x // 60, y // 10, x // 250, "black", "brown")
    return ()


def sun_drw():
    circle_drw(x * 0.85, y * 0.15, x // 20, x // 300, "black", "yellow")
    return ()


def picture_creation():
    background_set_up()
    house_drw()
    clouds_drw()
    spruce_drw()
    sun_drw()
    return ()


picture_creation()
window.getMouse()
