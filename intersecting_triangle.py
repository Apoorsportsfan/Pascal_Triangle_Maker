from math import factorial
import copy
import matplotlib.pyplot as plt

rows_before_intersection = 20
mod = 2

triangle_values = []

for row in range(rows_before_intersection):
    triangle_values.append([])

    for number in range(row + 1):
        # nCr = n!/((n-r)!*r!)
        value = factorial(row) // (factorial(number) * factorial(row - number))
        # append the newest value to the newest list
        triangle_values[-1].append(value)

upside_down_triangle_values = copy.deepcopy(triangle_values)

upside_down_triangle_values.pop(-1)
upside_down_triangle_values.reverse()
# print(triangle_values)
# print(upside_down_triangle_values)

# each row is 1 more then the row above it so we need to make the bottom rows bigger to do math latter
for num in range(rows_before_intersection + 1, rows_before_intersection * 2):
    # the number of zeros you need to add to each side of the number to get the correct numbers in each row
    zeros_to_add = int((num - len(upside_down_triangle_values[num-rows_before_intersection-1]))/2)
    for zero in range(zeros_to_add):
        upside_down_triangle_values[num-rows_before_intersection-1].insert(zero, 0)
        upside_down_triangle_values[num-rows_before_intersection-1].append(0)

# we need to do the formula for pascels triangle for each of the upside down rows
for row in range(len(upside_down_triangle_values)):
    # each number is going to become the sum of the 2 numbers above it and the number currently holding that spot
    for number in range(len(upside_down_triangle_values[row])):
        # if it is the first row then refer to the last row in triangle values
        if row == 0:
            # the first number just moves down to the first spot on the next row
            if number == 0:
                upside_down_triangle_values[row][number] = triangle_values[-1][number]
            else:
                try:
                    # add the number before the current index and the number of the current index together from the previous row,
                    # then once that is down add the number currently ocuppying the spot
                    upside_down_triangle_values[row][number] = triangle_values[-1][number-1] + triangle_values[-1][number] + upside_down_triangle_values[row][number]
                except:
                    # there will be an "out of range" exception, this signifies the end of the row and just carry down the last number
                    upside_down_triangle_values[row][number] = triangle_values[-1][-1]

        # if it is not the first row then refer to the row above in the upside down triangle
        elif row > 0:
            if number == 0:
                # the first number of the previous row just carries down
                upside_down_triangle_values[row][number] = upside_down_triangle_values[row-1][number]

            else:
                try:
                    # add the number before the current index and the number of the current index together from the previous row,
                    # then once that is down add the number currently ocuppying the spot
                    upside_down_triangle_values[row][number] = upside_down_triangle_values[row-1][number-1] + upside_down_triangle_values[row-1][number] + upside_down_triangle_values[row][number]
                except:
                    # the "out of range" except means you reached the end of the first row
                    upside_down_triangle_values[row][number] = upside_down_triangle_values[row-1][-1]

for row in range(len(upside_down_triangle_values)):
    triangle_values.append(upside_down_triangle_values[row])
print(triangle_values)


# starting square corner
square_start_x = -0.1
square_start_y = -0.1

# square size
square_size = 0.2

for row in range(len(triangle_values)):
    # square in row
    for square in range(len(triangle_values[row])):
        # if it is the first ever square change nothing
        if square == 0 and row == 0:
            square_start_cords = (square_start_x, square_start_y)
        # if it is the first square of a row change the y value
        elif square == 0 and row != 0:
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
        remain = triangle_values[row][square] % mod
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

plt.show()
