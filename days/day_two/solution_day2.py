import os, click
from typing import List


def solve_part_two(data):
    x = 0
    y = 0
    aim = 0

    for line in data:

        instr, val = line.split(" ")
        val = int(val)
        if instr == "forward":
            x += val
            y += aim * val
        elif instr == "down":
            aim += val
        elif instr == "up":
            aim -= val

    print(x * y)


def solve_part_one(data):

    x = 0
    y = 0

    for line in data:

        instr, val = line.split(" ")

        val = int(val)

        if instr == "forward":
            x += val
        elif instr == "down":
            y += val
        elif instr == "up":
            y -= val

    print(x * y)


@click.command()
@click.argument("input")
def main(input):

    """
    Reads an input file from the advent of code and proceeds with day 2 solution
    """

    user_input = open(input).read().splitlines()
    solve_part_one(user_input)
    solve_part_two(user_input)


if __name__ == "__main__":
    main()
