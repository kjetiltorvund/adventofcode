#!/bin/python
import math
import sys


def find_middle_element(arr):
    result = []
    n = len(arr)

    if n % 2 == 0:
        result.append(int(arr[n / 2 - 1]))
        result.append(int(arr[n / 2]))
    else:
        return int(arr[math.floor(n / 2)])

    return result


def shift_number_to_pass_rule(page_list, rules):
    j = 0
    while j < len(page_list):
        page_number = page_list[j]
        filtered_rule_set = get_rules_for_page(page_number, rules)
        page_pos = j
        for i in range(j+1, len(page_list), 1):
            if f"{page_number}|{page_list[i]}" not in filtered_rule_set:
                print(f"Page {page_number}, Rule {page_list[i]}|{page_number}")
                temp = page_list[i]
                page_list[page_pos] = temp
                page_list[i] = page_number
                page_pos = i
        j += 1


def is_valid(page_list, rules):

    for j in range(len(page_list)):
        page_number = page_list[j]
        rule_set_for_page_number = get_rules_for_page(page_number, rules)

        for i in range(j + 1, len(page_list), 1):
            # print(f"{page_number}: {line_split[i]}")
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

    #print(page_order_rules)
    updates_page_numbers = [x for x in updates_page_numbers if x != '']
    #print(updates_page_numbers)

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
            shift_number_to_pass_rule(page_list=line_split, rules=page_order_rules)
            incorrect_count += 1
            middle_numbers_on_incorrect.append(find_middle_element(line_split))
            part_two_sum += find_middle_element(line_split)

    print(f"Correct lines count {correct_count}, sum: {sum(middle_numbers)}")
    print(f"Lines with incorrect count {incorrect_count}, sum: {sum(middle_numbers_on_incorrect)}")
    print(f"Lines with incorrect count {incorrect_count}, sum: {part_two_sum}")
