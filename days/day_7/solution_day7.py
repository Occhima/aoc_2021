import click
from typing import List
from statistics import mean


def solve_part_one(data: List[int]) -> int:

    fuels = [sum(abs(init_pos - pos) for init_pos in data) for pos in data]
    return min(fuels)


def solve_part_two(data: List[int]) -> int:
    target = mean(data)
    triangle = lambda n: n * (n + 1) // 2
    summed_cost = lambda t: sum(triangle(abs(pos - t)) for pos in data)
    return min(summed_cost(int(target + bias)) for bias in (-0.5, 0, 0.5))


@click.command()
@click.argument("input_data")
def main(input_data):

    data = open(input_data).read().split(",")
    data = [int(d) for d in data]

    part_one_solution = solve_part_one(data)

    click.echo(f" PART ONE: {part_one_solution}")

    part_two_solution = solve_part_two(data)

    click.echo(f" PART  TWO: {part_two_solution}")


if __name__ == "__main__":
    main()
