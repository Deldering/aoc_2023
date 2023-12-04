import os
import re
from dataclasses import dataclass

SCRIPT_DIR = os.path.dirname(__file__)


@dataclass
class NumberMatch:
    value: int
    start_index: int
    end_index: int


@dataclass
class LineMatches:
    numbers: list[NumberMatch]
    symbols: list[int]


def ranges_overlap(x: range, y: range):
    overlap = range(max(x[0], y[0]), min(x[-1], y[-1]) + 1)
    return len(overlap) > 0


def find_adjacent_numbers(line_matches: list[LineMatches], line_range: range, index_range: range):
    adjacent_numbers: list[int] = []
    for j in line_range:
        for number in line_matches[j].numbers:
            if ranges_overlap(range(number.start_index, number.end_index + 1), index_range):
                adjacent_numbers.append(number.value)
    return adjacent_numbers


def has_symbol(line_matches: list[LineMatches], line_range: range, index_range: range):
    for j in line_range:
        for i in index_range:
            if i in line_matches[j].symbols:
                return True
    return False


def problem_1():
    result = 0
    with open(os.path.join(SCRIPT_DIR, "engine_schematic.txt")) as f:
        line_matches: list[LineMatches] = []
        for line in f.readlines():
            numbers_with_position = [
                NumberMatch(int(match.group()), match.start(), match.end() - 1)
                for match in re.finditer(r"(\d+)", line)
            ]
            symbol_positions = [match.start() for match in re.finditer(r"(?!\d|\.).", line)]
            line_matches.append(LineMatches(numbers_with_position, symbol_positions))
    number_of_lines = len(line_matches)
    for index, line in enumerate(line_matches):
        for number in line.numbers:
            start_search_index = number.start_index - 1
            end_search_index = number.end_index + 1
            start_search_line = index - 1 if index > 0 else 0
            end_search_line = index + 1 if index < (number_of_lines - 1) else (number_of_lines - 1)
            if has_symbol(
                line_matches,
                range(start_search_line, end_search_line + 1),
                range(start_search_index, end_search_index + 1),
            ):
                result += number.value
    return result


def problem_2():
    result = 0
    with open(os.path.join(SCRIPT_DIR, "engine_schematic.txt")) as f:
        line_matches: list[LineMatches] = []
        for line in f.readlines():
            numbers_with_position = [
                NumberMatch(int(match.group()), match.start(), match.end() - 1)
                for match in re.finditer(r"(\d+)", line)
            ]
            symbol_positions = [match.start() for match in re.finditer(r"\*", line)]
            line_matches.append(LineMatches(numbers_with_position, symbol_positions))
    number_of_lines = len(line_matches)
    for index, line in enumerate(line_matches):
        for symbol in line.symbols:
            start_search_index = symbol - 1
            end_search_index = symbol + 1
            start_search_line = index - 1 if index > 0 else 0
            end_search_line = index + 1 if index < (number_of_lines - 1) else (number_of_lines - 1)
            adjacent_numbers = find_adjacent_numbers(
                line_matches,
                range(start_search_line, end_search_line + 1),
                range(start_search_index, end_search_index + 1),
            )
            if len(adjacent_numbers) == 2:
                result += adjacent_numbers[0] * adjacent_numbers[1]
    return result


print(f"Problem 1: {problem_1()}")
print(f"Problem 2: {problem_2()}")
