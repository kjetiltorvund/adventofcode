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
            previous_number = report
            continue

        distance = get_distance(previous_number, report)
        print(f"For {previous_number} and {report}, distance {distance}")

        if 1 > distance or distance > 3:
            if distance > 0:
                print(f"{previous_number} {report} is { 'an' if increasing else 'a'} {'increase' if increasing else 'decrease'} of {distance}")
            else:
                print(f"{previous_number} {report} is neither increasing or decreasing")
            return False
        
        if increasing is None:
            increasing = report > previous_number

        if increasing is True:
            if report < previous_number:
                return False
            
        if increasing is False:
            if report > previous_number:
                return False
            
        previous_number = report

        
    return True


if __name__ == "__main__":
    input_file_name = sys.argv[1]

    input_file = open(input_file_name, "r")

    safe_reports_count = 0

    for line in input_file.readlines():
        if is_report_safe([ int(x) for x in line.strip().split(" ")]) is True:
            print("Safe")
            safe_reports_count += 1
        else:
            print("Unsafe")

    print(f"Amount of safe reports {safe_reports_count}")