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
        result.append(int(arr[math.floor(n / 2)]))

    return result

if __name__ == '__main__':
    input_file_name = sys.argv[1]

    page_order_rules = []
    updates_page_numbers = []

    with open(input_file_name, "r") as f:
        for line in f.readlines():
            if "|" in line:
                page_order_rules.append(line.strip())
            else:
                updates_page_numbers.append(line.strip())

    #print(page_order_rules)
    updates_page_numbers = [x for x in updates_page_numbers if x != '']
    #print(updates_page_numbers)

    middle_numbers = []
    total_count = 0
    incorrect_count = 0

    for update_line in updates_page_numbers:
        total_count += 1
        line_split = update_line.split(",")
        line_upheld_the_rules = True
        for page_number in line_split:

            index = line_split.index(page_number)

            rule_set_for_page = [x for x in page_order_rules if x.split('|')[0] == page_number]
            #print(rule_set_for_page)

            for i in range(index+1, len(line_split), 1):
                #print(f"{page_number}: {line_split[i]}")
                if f"{page_number}|{line_split[i]}" not in rule_set_for_page:
                    line_upheld_the_rules = False
                    break

        print(f"{line_split} upheld the rule: {line_upheld_the_rules}")
        if line_upheld_the_rules:
            middle_numbers += find_middle_element(line_split)
        else:
            incorrect_count += 1

    print(f"Total count {total_count - incorrect_count}, sum: {sum(middle_numbers)}")
            