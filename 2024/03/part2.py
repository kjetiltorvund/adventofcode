#!/bin/python
import re
import sys


if __name__ == '__main__':
    input_file_name = sys.argv[1]

    input_file = open(input_file_name, "r")

    list_of_mulls = []

    pattern = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")

    start_of_word = ['m', 'd']

    include = True

    for line in input_file.readlines():
        muls = re.findall(pattern, line)

        for item in muls:
            if item == "don't()":
                include = False
                continue

            if item == "do()":
                include = True
                continue

            if include:
                list_of_mulls.append(item)


    numbers_to_add = []
    number_pattern = re.compile(r"(\d+),(\d+)")
    for mul in list_of_mulls:
        mul_numbers = re.search(number_pattern, mul)

        numbers_to_add.append(int(mul_numbers.groups()[0]) * int(mul_numbers.groups()[1]))

    print(sum(numbers_to_add))