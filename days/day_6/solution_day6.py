import click
import typing as t
from collections import deque


def solve_part_one(starting_ages: t.List[int], steps: int) -> int:
    counts = [0] * 7
    for age in starting_ages:
        counts[age] += 1
    fishes = deque(counts)
    offspring = deque([0, 0])
    for _ in range(steps):
        fishes.rotate(-1)
        offspring.append(fishes[0])
        fishes[0] += offspring.popleft()
    return sum(fishes) + offspring.popleft()


@click.command()
@click.argument("input_data")
@click.option(
    "--test",
    default=False,
    is_flag=True,
    help="Runs this solution on test hard-coded inside the code",
)
def main(input_data, test):

    data = open(input_data).read().split(",")
    data = [int(d) for d in data]

    solve_p1 = solve_part_one(data, 256)

    click.echo(f"PART ONE: {solve_p1}")


if __name__ == "__main__":
    main()
