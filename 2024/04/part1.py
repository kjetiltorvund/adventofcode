#!/bin/python
import sys

def search_by_directional_input(array2d, row, col, dirX, dirY, endX, endY):
    search_chars = ["X", "M", "A", "S"]
    pos = 0
    temp_word = ""
    i = row
    j = col

    while 0 <= i < endX:
        if 0 <= j < endY:

            curr_char = array2d[i][j]

            if curr_char in search_chars and curr_char == search_chars[pos]:
                temp_word += array2d[i][j]
                if temp_word == "XMAS":
                    return temp_word
                pos += 1
            else:
                break
        else:
            return None
        j += dirY
        i += dirX
    return None


if __name__ == '__main__':
    input_file_name = sys.argv[1]

    array2d = []

    with open(input_file_name, "r") as f:

        for line in f.readlines():
            temp_array = []
            line = line.strip()
            for char in line:
                temp_array.append(char)

            array2d.append(temp_array)

        temp_array = []

    # Debug print matrix
    # row_number = 0
    # for row in array2d:
    #     print(f"{row_number}: {row}")
    #     row_number += 1

    xmas_count = 0

    for row in range(0, len(array2d)):
        for col in range(0, len(array2d[row])):
            if array2d[row][col] == "X":

                # Left to right
                xmas = search_by_directional_input(array2d, row, col, 0, 1, len(array2d[row]), len(array2d))
                if xmas is not None:
                    xmas_count += 1
                    print(f"{xmas_count:02d}: {row}:{col} Left to right ->")
                # Down right
                xmas = search_by_directional_input(array2d, row, col, 1, 1, len(array2d[row]), len(array2d))
                if xmas is not None:
                    xmas_count += 1
                    print(f"{xmas_count:02d}: {row}:{col} Down right \\")

                # Straight down
                xmas = search_by_directional_input(array2d, row, col, 1, 0, len(array2d[row]), len(array2d))
                if xmas is not None:
                    xmas_count += 1
                    print(f"{xmas_count:02d}: {row}:{col} Down |")

                # Down left
                xmas = search_by_directional_input(array2d, row, col, 1, -1, len(array2d[row]), len(array2d))
                if xmas is not None:
                    xmas_count += 1
                    print(f"{xmas_count:02d}: {row}:{col} Down left /")

                # Right to left
                xmas = search_by_directional_input(array2d, row, col, 0, -1, len(array2d[row]), len(array2d))
                if xmas is not None:
                    xmas_count += 1
                    print(f"{xmas_count:02d}: {row}:{col} Right to left <-")

                # Upward left
                xmas = search_by_directional_input(array2d, row, col, -1, -1, len(array2d[row]), len(array2d))
                if xmas is not None:
                    xmas_count += 1
                    print(f"{xmas_count:02d}: {row}:{col} Up left \\")

                # Straight up
                xmas = search_by_directional_input(array2d, row, col, -1, 0, len(array2d[row]), len(array2d))
                if xmas is not None:
                    xmas_count += 1
                    print(f"{xmas_count:02d}: {row}:{col} Up |")

                # Upward right
                xmas = search_by_directional_input(array2d, row, col, -1, 1, len(array2d[row]), len(array2d))
                if xmas is not None:
                    xmas_count += 1
                    print(f"{xmas_count:02d}: {row}:{col} Up right /")


    print(xmas_count)