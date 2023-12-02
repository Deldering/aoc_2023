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


def problem_1():
    sum = 0
    with open(os.path.join(SCRIPT_DIR, "calibration_values.txt")) as f:
        for line in f.readlines():
            values = re.findall(r"\d", line)
            sum += int(values[0] + values[-1])
    return sum


def problem_2():
    sum = 0
    with open(os.path.join(SCRIPT_DIR, "calibration_values.txt")) as f:
        for line in f.readlines():
            first = re.search(f"(\d|{'|'.join(NUMBERS)})", line).group()
            try:
                first = int(first)
            except:
                first = NUMBERS.index(first)

            second = re.search(f"(\d|{'|'.join(REVERSE_NUMBERS)})", line[::-1]).group()
            try:
                second = int(second)
            except:
                second = REVERSE_NUMBERS.index(second)

            sum += first * 10 + second
    return sum

print(f"Problem 1: {problem_1()}")
print(f"Problem 2: {problem_2()}")
