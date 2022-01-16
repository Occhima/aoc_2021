from __future__ import annotations
import click, aocd
from dataclasses import dataclass, field
from typing import Final


# Bingo cards are square grids of CARD_SIZE x CARD_SIZE numbers.
CARD_SIZE: Final[int] = 5

# Pre-computed slices for rows and columns
ROWS: Final[list[slice]] = [
    slice(i, i + CARD_SIZE) for i in range(0, CARD_SIZE * CARD_SIZE, CARD_SIZE)
]
COLS: Final[list[slice]] = [
    slice(col, CARD_SIZE * CARD_SIZE, CARD_SIZE) for col in range(CARD_SIZE)
]


@dataclass
class BingoCard:
    numbers: list[int]
    marked: set[int] = field(default_factory=set)
    _lines: frozenset[frozenset[int]] = field(init=False)

    def __post_init__(self) -> None:
        # collect the sets of numbers forming the horizontal and vertical lines
        # across the bingo card
        self._lines = frozenset(
            frozenset(self.numbers[row]) for row in ROWS
        ) | frozenset(frozenset(self.numbers[col]) for col in COLS)

    @classmethod
    def from_text(cls, text: str) -> BingoCard:
        return cls([int(n) for n in text.split()])

    @property
    def unmarked_score(self) -> int:
        return sum(set(self.numbers) - self.marked)

    @property
    def wins(self) -> bool:
        # a bingo card wins if any of its lines is a subset of the marked numbers
        marked = self.marked
        return any(marked >= line for line in self._lines)

    def mark(self, number: int) -> int:
        """Mark a number off on the card, and return a score

        The score is 0 if there are still rows or columns with unmarked numbers.

        """
        self.marked.add(number)
        if self.wins:
            return self.unmarked_score * number
        return 0


@dataclass
class BingoSubsystem:
    random_numbers: list[int]
    cards: list[BingoCard] = field(default_factory=list)
    number_index: dict[int, set[int]] = field(default_factory=dict)

    def add_card(self, card: BingoCard) -> None:
        card_index = len(self.cards)
        self.cards.append(card)
        for number in card.numbers:
            self.number_index.setdefault(number, set()).add(card_index)

    @classmethod
    def from_text(cls, text: str) -> BingoSubsystem:
        blocks = iter(text.split("\n\n"))
        game = cls([int(n) for n in next(blocks).split(",")])
        for block in blocks:
            game.add_card(BingoCard.from_text(block))
        return game

    def find_winning_score(self):
        empty = frozenset()
        for number in self.random_numbers:
            for card_index in self.number_index.get(number, empty):
                if score := self.cards[card_index].mark(number):
                    return score


class LastWinningBingoSubsystem(BingoSubsystem):
    def find_last_winning_score(self) -> int:
        last_score, remaining = 0, set(range(len(self.cards)))
        empty = frozenset()
        for number in self.random_numbers:
            for card_index in self.number_index.get(number, empty) & remaining:
                if score := self.cards[card_index].mark(number):
                    last_score = score
                    remaining.remove(card_index)
                    if not remaining:
                        break
        return last_score


def solve_part_one(data):
    return BingoSubsystem.from_text(data).find_winning_score()


def solve_part_two(data):
    return LastWinningBingoSubsystem.from_text(data).find_last_winning_score()


@click.command()
@click.argument("input")
@click.option(
    "--test",
    default=False,
    is_flag=True,
    help="Runs this solution on test hard-coded inside the code",
)
def main(input, test):

    data = open(input).read()

    part_one_solution = solve_part_one(data)

    click.echo(f"PART ONE: {part_one_solution}")

    part_two_solution = solve_part_two(data)

    click.echo(f"PART ONE: {part_two_solution}")
    # part_two_solution = solve_part_two(data)

    # click.echo(f"PART TWO: {part_two_solution}")


if __name__ == "__main__":
    main()
