from graphics import *
import colorsys

THRESHOLD = 10
WIDTH = 300
HEIGHT = 600

def quantity(color):
    return sqrt((color[0] ** 2) + (color[1] ** 2) + (color[2] ** 2))

def is_duplicate(color_a, color_b):
    return abs(quantity(color_a) - quantity(color_b)) > TRESHOLD

def to_color_rgb(color):
    return color_rgb(color[0], color[1], color[2])

def draw_list(colors, win):
    thickness = HEIGHT / len(colors)
    for i in range(len(colors)):
        line = Line(Point(0, i * thickness), Point(WIDTH, i * thickness))
        line.setFill(to_color_rgb(colors[i]))
        line.setWidth(thickness)
        line.draw(win)

def rainbow(granularity):
    ret = []
    for i in range(granularity):
        rgb = colorsys.hsv_to_rgb(float(i) / granularity, 0.5, 1.0)
        ret.append((int (rgb[0] * 255), int (rgb[1] * 255), int (rgb[2] * 255), 1 - (float(i) / granularity)))
    return ret

def diversify1(entries):
    #TODO: adi
    return entries

def diversify2(entries):
    # TODO: tim
    return entries

if __name__ == '__main__':
    input = rainbow(50)
    win1 = GraphWin("Input Colors", WIDTH, HEIGHT)
    draw_list(input, win1)

    win2 = GraphWin("Diversified #1", WIDTH, HEIGHT)
    draw_list(diversify1(input), win2)

    win3 = GraphWin("Diversified #2", WIDTH, HEIGHT)
    draw_list(diversify2(input), win3)

    win3.getMouse()      # Pause to view result
    win1.close()         # Close windows when done
    win2.close()
    win3.close()
