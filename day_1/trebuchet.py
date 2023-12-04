from enum import Enum
import re
import os

SCRIPT_DIR = os.path.dirname(__file__)

NUMBERS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
REVERSE_NUMBERS = [number[::-1] for number in NUMBERS]

FORWARD_PATTERN = rf"(\d|{'|'.join(NUMBERS)})"
REVERSE_PATTERN = rf"(\d|{'|'.join(REVERSE_NUMBERS)})"


class Direction(Enum):
    FORWARD = "FORWARD"
    REVERSE = "REVERSE"


def find_digit(line: str, direction: Direction):
    if direction == Direction.FORWARD:
        pattern = FORWARD_PATTERN
        number_list = NUMBERS
    elif direction == Direction.REVERSE:
        pattern = REVERSE_PATTERN
        number_list = REVERSE_NUMBERS
        line = line[::-1]
    else:
        raise ValueError("Invalid Direction parameter")
    result = re.search(pattern, line)
    if result is None:
        raise ValueError("Line doesn't contain a digit")
    try:
        return int(result.group())
    except ValueError:
        return number_list.index(result.group())


def problem_1():
    result = 0
    with open(os.path.join(SCRIPT_DIR, "calibration_values.txt")) as f:
        for line in f.readlines():
            values = re.findall(r"\d", line)
            if len(values) == 0:
                raise ValueError("Line doesn't contain a digit")
            result += int(values[0] + values[-1])
    return result


def problem_2():
    result = 0
    with open(os.path.join(SCRIPT_DIR, "calibration_values.txt")) as f:
        for line in f.readlines():
            first = find_digit(line, Direction.FORWARD)
            last = find_digit(line, Direction.REVERSE)
            result += first * 10 + last
    return result


print(f"Problem 1: {problem_1()}")
print(f"Problem 2: {problem_2()}")
