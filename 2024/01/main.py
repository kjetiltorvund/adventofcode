#!/bin/python

import sys
import re

if __name__ == "__main__":
    input_file_name = sys.argv[1]

    input_file = open(input_file_name, "r")

    left_list = []
    right_list = []

    for line in input_file.readlines():
        res = re.findall("(\d+)\s+(\d+)", line)
        
        left_list.append(int(res[0][0]))
        right_list.append(int(res[0][1]))

    left_list.sort()
    right_list.sort()     

    sum_array = []

    for i in range(0, len(left_list), 1):
        distance = abs(left_list[i] - right_list[i])
        sum_array.append(distance)

    print(sum(sum_array))