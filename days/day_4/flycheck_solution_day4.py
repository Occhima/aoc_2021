import click
from typing import List


class Board:
    def __init__(self, data):
        self.data = data


class BoardCollection:
    def __init__(self, board_collection: List[Board]):

        self.__chosen_numbers = None
        self.board_collection = board_collection

    def load_board_from_input(self):
        pass

    def mark_boards_by_number(self, number: int) -> None:
        pass

    def count_unmarked_numbers(self):
        pass


def solve_part_one():
    pass


@click.command()
@click.argument("input")
@click.option(
    "--test",
    default=False,
    is_flag=True,
    help="Runs this solution on test hard-coded inside the code",
)
def main(input, test):

    data = open(input).read().splitlines()

    part_one_solution = solve_part_one(data)

    click.echo(f"PART ONE: {part_one_solution}")

    # part_two_solution = solve_part_two(data)

    # click.echo(f"PART TWO: {part_two_solution}")


if __name__ == "__main__":
    main()
