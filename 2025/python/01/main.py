

import copy
import math

def part1(data: list[str], start:int = 50, clicks: int = 100) -> int:
    zero_counter = 0
    curr_pos = start

    for instruction in data:
        direction = instruction[0]
        steps = int(instruction[1:])
        
        # Convert LEFT to equivalent RIGHT rotation
        if direction == "L":
            steps = clicks - steps
        
        curr_pos = (curr_pos + steps) % clicks
        if curr_pos == 0:
            zero_counter += 1

    return zero_counter


def part2(data: list[str], start:int = 50, clicks: int = 100) -> int:
    dail_position = start
    zero_counter = 0

    print(f"Amount of lines: {len(data)}")
    for line in data:
        print("Line: ", line)

        direction = line[0]
        value = int(line[1:])

        print(f"CLine: {direction}{value}")

        for _ in range(value):
            if direction == 'R':
                dail_position = (dail_position + 1) % clicks
            else:
                dail_position = (dail_position - 1) % clicks

            if dail_position == 0:
                zero_counter += 1

        #print("Position: ", dail_position)

    
    print(f"Code is: {zero_counter}")

    return zero_counter

if __name__ == "__main__":
    data_file = open("input.txt", "r")
    lines = list(map(lambda x: x.strip(), data_file.readlines()))
    part2(lines)
