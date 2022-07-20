import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# mod for triangle
mod = 3

# number of rows for the triangle
num_rows = 64

# the first row of numbers
starting_values = []

#
# creating the values
#

# list that will hold all of the values
values = []
values.append(starting_values)



# number of times to run this code (each run is a row in the triangle)
for num in range(num_rows):
    # the new row has to start with 0 so create a new
    row_values = [0]

    # use the length of the previous row to determine amount of times to do addition
    for value in range(len(values[num])):
        try:
            # take the value number and add the number to the right of it
            new_num = values[num][value] + values[num][value + 1]
            row_values.append(new_num)
        except:
            # this happens when it reaches the 0 at the end of the list
            pass

    # the new row has to end with 0 so append 0
    row_values.append(0)
    # add the entire new row to the values row
    values.append(row_values)


#
# creating the graph
#

figure = plt.figure()

# starting square corner
square_start_x = -0.3
square_start_y = -0.3

# square size
square_size = 0.2

for row in range(num_rows):
    for value_index in range(len(values[row])):
        # if it is the first ever square change nothing
        if value_index == 0 and row == 0:
            square_start_cords = (square_start_x, square_start_y)
        # if it is the first square of a row change the y value down a row and move the x value over half a square
        elif value_index == 0 and row != 0:
            square_start_x = square_start_x - square_size / 2
            square_start_y = square_start_y - square_size

            square_start_cords = (square_start_x, square_start_y)
        else:
            # if it is the second square in a row then change the start based on the first square
            if value_index == 1:
                square_start_x_row = square_start_x + square_size
            # if it is any other square change based on square to the left
            else:
                square_start_x_row = square_start_x_row + square_size

            square_start_cords = (square_start_x_row, square_start_y)

        # picking the color
        remain = values[row][value_index] % mod
        if remain == 0:
            color = "blue"
        else:
            color = "green"

        if values[row][value_index] != 0:
            square = plt.Rectangle(square_start_cords, square_size, square_size, fc=color)
            plt.gca().add_patch(square)
        else:
            pass

# static things
plt.axis("scaled")
# get the bottom row (the biggest) then get the amount of squares in that row and divide by 2 to get half the length of the row
# multiply by the square size then add a buffer, this will be half of the axis width
x_size = (len(values[-1]) / 2) * square_size + 0.5
# get the amount of rows and then add an extra row worth of buffer
y_size = (len(values) + 1) * 0.2
plt.xlim(-x_size, x_size + (len(values[0]) - 2) * square_size)
plt.ylim(-y_size, 0.5)

plt.show()