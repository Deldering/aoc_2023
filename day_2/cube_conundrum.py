import os

SCRIPT_DIR = os.path.dirname(__file__)


def game_valid(information: list[str]):
    colors_available = {"r": 12, "g": 13, "b": 14}
    for info in information.split(";"):
        for color_values in info.split(","):
            _, count, color_text = color_values.split(" ")
            if colors_available[color_text[0]] < int(count):
                return False
    return True


def determine_colors_required(information: list[str]):
    colors_required = {"r": 0, "g": 0, "b": 0}
    for info in information.split(";"):
        for color_values in info.split(","):
            _, count, color_text = color_values.split(" ")
            if colors_required[color_text[0]] < int(count):
                colors_required[color_text[0]] = int(count)
    return colors_required


def problem_1():
    sum = 0
    with open(os.path.join(SCRIPT_DIR, "game_information.txt")) as f:
        for line in f.readlines():
            game, information = line.split(":")
            if game_valid(information):
                sum += int(game.split(" ")[-1])
    return sum


def problem_2():
    sum = 0
    with open(os.path.join(SCRIPT_DIR, "game_information.txt")) as f:
        for line in f.readlines():
            game, information = line.split(":")
            colors_required = determine_colors_required(information)
            sum += colors_required["r"] * colors_required["g"] * colors_required["b"]
            pass
    return sum


print(f"Problem 1: {problem_1()}")
print(f"Problem 2: {problem_2()}")
