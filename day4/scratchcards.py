import re
import os

SCRIPT_DIR = os.path.dirname(__file__)


def get_my_winning_numbers(line: str):
    _, numbers = line.split(":")
    winning_number_string, my_number_string = numbers.split("|")
    winning_numbers = re.findall(r"\d+", winning_number_string)
    my_numbers = re.findall(r"\d+", my_number_string)
    my_winning_numbers = [number for number in my_numbers if number in winning_numbers]
    return my_winning_numbers


def problem_1():
    result = 0
    with open(os.path.join(SCRIPT_DIR, "scratchcards.txt")) as f:
        for line in f.readlines():
            my_winning_numbers = get_my_winning_numbers(line)
            if len(my_winning_numbers) > 0:
                result += 2 ** (len(my_winning_numbers) - 1)
    return result


def problem_2():
    with open(os.path.join(SCRIPT_DIR, "scratchcards.txt")) as f:
        lines = f.readlines()
    card_count = {x: 1 for x in range(len(lines))}
    for index, line in enumerate(lines):
        my_winning_numbers = get_my_winning_numbers(line)
        for x in range(1, len(my_winning_numbers) + 1):
            if index + x > len(lines) - 1:
                break
            card_count[index + x] += card_count[index]
    return sum(card_count.values())


print(f"Problem 1: {problem_1()}")
print(f"Problem 2: {problem_2()}")
