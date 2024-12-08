#!/bin/python
import sys

def search_by_directional_input(array2d, row, col, dirX, dirY, endX, endY):
    search_chars = ["M", "A", "S"]
    revers_search_chars = ["S", "A", "M"]
    pos = 0
    temp_word = ""
    i = row
    j = col


    while 0 <= i < endX:
        if 0 <= j < endY:

            curr_char = array2d[i][j]

            if pos >= len(search_chars):
                break

            if (curr_char in search_chars or curr_char in revers_search_chars) and (curr_char == search_chars[pos] or curr_char == revers_search_chars[pos]):
                temp_word += array2d[i][j]
                if temp_word == "MAS" or temp_word == "SAM":
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

    input_file = open(input_file_name, "r")

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
    row_number = 0
    for row in array2d:
        print(f"{row_number}: {row}")
        row_number += 1

    xmas_count = 0

    for row in range(0, len(array2d)):
        for col in range(0, len(array2d[row])):
            if array2d[row][col] == "A":
                matches = 0
                # Down right
                xmas = search_by_directional_input(array2d, row-1, col-1, 1, 1, len(array2d[row]), len(array2d))
                if xmas == "MAS" or xmas == "SAM":
                    #xmas_count += 1
                    matches += 1
                    print(f"{xmas_count:02d}: {row}:{col} Down right \\")

                # Upward right
                xmas = search_by_directional_input(array2d, row+1, col-1, -1, 1, len(array2d[row]), len(array2d))
                if xmas == "MAS" or xmas == "SAM":
                    #xmas_count += 1
                    matches += 1
                    print(f"{xmas_count:02d}: {row}:{col} Up right /")

                if matches == 2:
                    xmas_count += 1

    print(xmas_count)