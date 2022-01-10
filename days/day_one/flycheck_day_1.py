import os, click
from pathlib import Path
from itertools import tee, islice, chain


# NOTE: This is just an iteration helper, it helps to iterate through a list with previous and next items
def previous_and_next(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)


def increase_or_decrease(current_depth: int, previous_depth: int = None) -> None:

    """
        Reads the advent of code input, with the before depth and the current depth
    """

    if previous_depth is None:
        print("(N/A - no previous measurement)")

    if previous_depth > current_depth:
        print("increased")

    else:
        print("decreased")


@click.command()
@click.argument("input", type=Path(exists=True))
def main(input):

    """
        Reads an input file from the advent of code
    """

    user_input = open(input).readlines()

    for previous, current, _ in user_input:
        increase_or_decrease(current_depth=int(current), previous_depth=int(previous))


if __name__ == "__main__":
    main()
