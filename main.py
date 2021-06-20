# the beginning of training for drawing

import graphics as gr

window = gr.GraphWin("Черчу черчу", 1200, 800)


def circle_drw(coord_x, cord_y, radius, line_width, outline_colour, fill_colour):
    circle = gr.Circle(gr.Point(coord_x, cord_y), radius)
    circle.setOutline(outline_colour)
    circle.setWidth(line_width)
    circle.setFill(fill_colour)
    circle.draw(window)
    return ()


def rectangle_drw(start_point_x, start_point_y, end_point_x, end_point_y, line_width, outline_color, fill_color):
    rectangle = gr.Rectangle(gr.Point(start_point_x, start_point_y), (gr.Point(end_point_x, end_point_y)))
    rectangle.setOutline(outline_color)
    rectangle.setWidth(line_width)
    rectangle.setFill(fill_color)
    rectangle.draw(window)
    return ()


rectangle_drw(0, 0, 1200, 400, 2, "blue", "blue")

window.getMouse()
