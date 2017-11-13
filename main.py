from graphics import *
from collections import deque
from copy import deepcopy
import colorsys
import math

THRESHOLD = 5
WIDTH = 300
HEIGHT = 600

def quantity(color):
    return math.sqrt((color[0] ** 2) + (color[1] ** 2) + (color[2] ** 2))

def is_duplicate(color, existing_colors):
    return any(map(lambda x : abs(quantity(color) - quantity(x)) > THRESHOLD, existing_colors))

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

DIVERSITY_THRESHOLD = 5

def diversify1(input):
    entries = deepcopy(input)
    count = 0
    index = 0
    diverse_entries = []
    duplicates = set()
    queued_entries = deque()

    while (index < len(entries)):
        if count == DIVERSITY_THRESHOLD:
            duplicates.clear()
            count = 0
        else:
            entry_to_add = None
            for q_entry in queued_entries:
                if not is_duplicate(q_entry, duplicates):
                    entry_to_add = q_entry
                    break
            if entry_to_add != None:
                queued_entries.remove(entry_to_add)
            else:
                while (index < len(entries)):
                    entry = entries[index]
                    index = index + 1
                    if not is_duplicate(entry, duplicates):
                        entry_to_add = entry
                        break
                    else:
                        queued_entries.append(entry)
            if entry_to_add == None:
                entry_to_add = queued_entries.popleft()
            diverse_entries.append(entry_to_add)
            duplicates.add(entry_to_add)
            count = count + 1
        if index >= len(entries) and len(queued_entries) > 0:
            entries.clear()
            for q_entry in queued_entries:
                entries.append(q_entry)
            queued_entries.clear()
            index = 0

    return diverse_entries

def diversify2(input):
    entries = deepcopy(input)
    diverse_entries = []
    duplicates = set()
    index = 0
    dup_penalty = 0.90
    print(entries[1])


    

    while(index < len(entries)):
        current = entries[index]
        if is_duplicate(current, duplicates):
            if current in duplicates:
                diverse_entries.append(current)
                print("already encountered " , current)
                index = index + 1
            else:
                print("penalizing dup ",current)
                entries[index] = (entries[index][0],entries[index][1],entries[index][2],entries[index][3]*dup_penalty)
                duplicates.add(entries[index])
                #TODO sort/insert
                entries.sort(key=lambda tup:tup[3], reverse = True)
        else:
            #add it
            print("adding ", current)
            diverse_entries.append(current)
            index = index + 1
            duplicates.add(current)


    return diverse_entries

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
