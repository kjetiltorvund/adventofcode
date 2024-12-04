#!/bin/python

import sys
import re

def get_distance(a : int, b: int):
    if a > b:
        return a - b
    
    return b - a

def is_report_safe(report_line):
    increasing = None
    previous_number = None
    for report in report_line:
        if previous_number is None:
            previous_number = int(report)
            continue

        distance = get_distance(previous_number, int(report))
        print(f"Got distance {distance} for {report} and {previous_number}")

        if distance < 1 and distance > 3:
            return False
        
        if increasing is None:
            if int(report) > previous_number:
                increasing = True
            
            increasing = False

        if increasing is True:
            if int(report) < previous_number:
                return False
            
        if increasing is False:
            if int(report) > previous_number:
                return False
            
        previous_number = int(report)

        
    return True


if __name__ == "__main__":
    input_file_name = sys.argv[1]

    input_file = open(input_file_name, "r")

    safe_reports_count = 0

    for line in input_file.readlines():
        if is_report_safe(line.strip().split(" ")) is True:
            print("Safe")
            safe_reports_count += 1
        else:
            print("Unsafe")

    print(f"Amount of safe reports {safe_reports_count}")