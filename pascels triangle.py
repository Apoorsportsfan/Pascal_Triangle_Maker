import numpy as np
from math import factorial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Functions_of_cool_designs import save_as_gif_2d

triangle_values = []

# mod of triangle
mod = 2
# number of rows of triangle
n = 64
for i in range(n):
    # if it is the start of a new row append a new list inside the list
    triangle_values.append([])
    for j in range(i + 1):
        # nCr = n!/((n-r)!*r!)
        value = factorial(i) // (factorial(j) * factorial(i - j))
        # append the newest value to the newest list
        triangle_values[-1].append(value)

figure = plt.figure()

# starting square corner
square_start_x = -0.1
square_start_y = -0.1

# square size
square_size = 0.2
# number of rows is equal to the length of the triangle list
rows_num = len(triangle_values)
# row number
for num in range(rows_num):
    # square in row
    for square in range(len(triangle_values[num])):
        # if it is the first ever square change nothing
        if square == 0 and num == 0:
            square_start_cords = (square_start_x, square_start_y)
        # if it is the first square of a row change the y value
        elif square == 0 and num != 0:
            square_start_x = square_start_x - square_size / 2
            square_start_y = square_start_y - square_size

            square_start_cords = (square_start_x, square_start_y)
        else:
            # if it is the second square in a row then change the start based on the first square
            if square == 1:
                square_start_x_row = square_start_x + square_size
            # if it is any other square change based on square to the left
            else:
                square_start_x_row = square_start_x_row + square_size

            square_start_cords = (square_start_x_row, square_start_y)

        # picking the color
        remain = triangle_values[num][square] % mod
        if remain == 0:
            color = "blue"
        else:
            color = "green"
        # elif remain == 1:
        #     color = "green"
        # elif remain == 2:
        #     color = "orange"
        # elif remain == 3:
        #     color = "yellow"
        # elif remain == 4:
        #     color = "black"
        square = plt.Rectangle(square_start_cords, square_size, square_size, fc=color)
        plt.gca().add_patch(square)


# static things
plt.axis("scaled")
x_size = (len(triangle_values[-1])/2) * 0.2 + 0.5
y_size = (len(triangle_values) + 1) * 0.2
plt.xlim(-x_size, x_size)
plt.ylim(-y_size, 0.5)

def animate(frame):
    pass

anim = FuncAnimation(figure, animate, frames=200, interval=10)
# save_as_gif_2d(anim, "baseball")
plt.show()
