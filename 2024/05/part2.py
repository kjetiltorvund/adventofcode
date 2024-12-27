#!/bin/python
import math
import sys
from functools import cmp_to_key


def find_middle_element(arr):
    result = []
    n = len(arr)

    if n % 2 == 0:
        result.append(int(arr[n / 2 - 1]))
        result.append(int(arr[n / 2]))
    else:
        return int(arr[math.floor(n / 2)])

    return result


# Global rules array
rules = []

# Custom sort function
def rule_sort(item1, item2):
    if f"{item1}|{item2}" in rules:
        return -1
    else:
        return 1


def is_valid(page_list, rules):

    for j in range(len(page_list)):
        page_number = page_list[j]
        rule_set_for_page_number = get_rules_for_page(page_number, rules)

        for i in range(j + 1, len(page_list), 1):
            if f"{page_number}|{page_list[i]}" not in rule_set_for_page_number:
                return False

    return True


def get_rules_for_page(page_number, rules):
    return [x for x in rules if
            x.split('|')[0] == page_number]


if __name__ == '__main__':
    input_file_name = sys.argv[1]

    page_order_rules = []
    updates_page_numbers = []

    with open(input_file_name, "r") as f:
        for line in f.readlines():
            if "#" in line:
                continue
            if "|" in line:
                page_order_rules.append(line.strip())
            else:
                updates_page_numbers.append(line.strip())

    rules = page_order_rules
    updates_page_numbers = [x for x in updates_page_numbers if x != '']

    middle_numbers = []
    middle_numbers_on_incorrect = []
    part_two_sum = 0

    correct_count = 0
    incorrect_count = 0
    for update_line in updates_page_numbers:
        line_split = update_line.split(",")
        line_split_copy = update_line.split(",")

        if is_valid(line_split, page_order_rules):
            correct_count += 1
            middle_numbers.append(find_middle_element(line_split))
        else:
            test = sorted(line_split, key=cmp_to_key(rule_sort))
            incorrect_count += 1
            part_two_sum += find_middle_element(test)

    print(f"Correct lines count {correct_count}, sum: {sum(middle_numbers)}")
    print(f"Lines with incorrect count {incorrect_count}, sum: {part_two_sum}")
