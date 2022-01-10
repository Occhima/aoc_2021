import os, click
from pathlib import Path
from collections import deque
from itertools import islice


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


@click.command()
@click.argument("input")
def main(input):

    """
        Reads an input file from the advent of code
    """

    user_input = open(input).readlines()
    user_input = [int(value) for value in user_input]

    click.secho("Part one...", bold=True, blink=False)

    part_one_result = sum(b > a for a, b in sliding_window(user_input, 2))

    click.secho(
        f"Total number of increases {part_one_result}", bold=True,
    )

    click.secho("Part two...", bold=True, blink=False)

    # creates an array with all the sums
    aux_arr = [sum(tup) for tup in sliding_window(user_input, 3)]

    part_two_result = sum(curr > prev for prev, curr in sliding_window(aux_arr, 2))

    click.secho(
        f"Total number of increases for part two {part_two_result}", bold=True,
    )


if __name__ == "__main__":
    main()
