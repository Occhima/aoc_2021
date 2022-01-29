import click
from collections import Counter


def solve_part_one(lines) -> int:
    lengths = Counter()
    for line in lines:
        output = line.partition("|")[-1]
        lengths += Counter(len(num) for num in output.split())
    return lengths[2] + lengths[3] + lengths[4] + lengths[7]


@click.command()
@click.argument("input_data")
def main(input_data):

    data = open(input_data).read().splitlines()
    # data = [int(d) for d in data]

    part_one_solution = solve_part_one(data)
    click.echo(f" PART ONE: {part_one_solution}")

    # part_two_solution = solve_part_two(data)

    # click.echo(f" PART  TWO: {part_two_solution}")


if __name__ == "__main__":
    main()
