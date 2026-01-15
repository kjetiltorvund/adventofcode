
def part1(data:list) -> int:
    added_invalid_ids = 0

    for id in data:
        sub_ids = id.split("-")

        if(str(sub_ids[0]).startswith("0")):
            continue

        for sub_id in range(int(sub_ids[0]), int(sub_ids[1])+1):
            num_str = str(sub_id)

            string_length = int(len(num_str) / 2)

            first_part = num_str[:string_length]
            last_part = num_str[string_length:]

            if first_part == last_part:
                #print(f"Value to add: {sub_id}")
                added_invalid_ids += sub_id
                continue        

    return added_invalid_ids


def test_string(num_string:str, test:str) -> bool:
    return test in num_string


def part2(data:list) -> int:
    # ID is invalid if
    # - only made of som sequence of digits repeated at least twice. 12341234 (1234 two times)

    import re

    added_invalid_ids = 0
    invalid_ids_list = []

    for id_range in data:
        sub_ids = id_range.split("-")

        if(str(sub_ids[0]).startswith("0")):
            continue

        for sub_id in range(int(sub_ids[0]), int(sub_ids[1])+1):
            num_string = str(sub_id)

            comparator = ""
            previous_char = ""
            current_string = ""
            length = 0
            match_counter = 0
            
            for i, char in enumerate(num_string):
                current_string += char
                
                if len(previous_char) == 0:
                    previous_char = char
                    continue

                if len(num_string) == 2 and char == previous_char:
                    invalid_ids_list.append(sub_id)
                    added_invalid_ids += sub_id
                    previous_char = char
                    continue

                if len(num_string)-1 == i:
                    all_similar = True

                    for i, c in enumerate(current_string):
                        if c != char:
                            all_similar = False
                            break

                    if all_similar:
                        invalid_ids_list.append(sub_id)
                        added_invalid_ids += sub_id

                matches = re.findall(current_string, num_string)

                if len(matches) >= 2:
                    added_invalid_ids += sub_id
                    invalid_ids_list.append(sub_id)
                    break




    return added_invalid_ids


if __name__ == '__main__':
    with open("input.txt", "r") as data_file:

        data:list = []
    
        for line in data_file.readlines():
            data += line.split(",")

    answer_part1 = part1(data)

    print(f"Answer part1: {answer_part1}")

    answer_part2 = part2(data)

    print(f"Answer part2: {answer_part2}")