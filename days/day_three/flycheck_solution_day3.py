import click


def solve_part_1():
    pass


def solve_part_two():
    pass


@click.command()
@click.argument("input")
def main(input):
    data = open(input).readlines()
    print(data)


if __name__ == "__main__":
    main()
