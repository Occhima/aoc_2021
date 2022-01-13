import click
from typing import List, Literal, Union
from collections import Counter


def calculate_proportion_in_array(data: List[int]) -> Union[Literal[1], Literal[0]]:
    """
    For an alternate solution

    """

    prop = sum(data) / len(data)

    return 1 if prop > 0.5 else 0


def solve_part_one(data: List[str]) -> int:

    aux_data = [[d[i] for d in data] for i in range(len(data[0]))]

    gamma_rate = int("".join(max(a, key=Counter(a).get) for a in aux_data), 2)
    epsilon_rate = int("".join(min(a, key=Counter(a).get) for a in aux_data), 2)

    power_consumption = gamma_rate * epsilon_rate

    return power_consumption


def solve_part_two_rec(data: List[str]) -> int:
    def recursive_solution(
        data,
        i: int = None,
        rate_type: Union[Literal["oxygen"], Literal["co2"]] = "oxygen",
    ) -> str:

        if i is None:
            i = 0

        if i == len(data[0]):
            return ""

        caller = max if rate_type == "oxygen" else min

        aux_data_1 = [d[i] for d in data]
        max_item = caller(aux_data_1, key=Counter(aux_data_1).get)
        aux_data = [d for d in data if d[i] == max_item]
        i += 1

        return "".join(max_item + recursive_solution(aux_data, i=i))

    oxygen = int(recursive_solution(data), 2)
    co2 = int(recursive_solution(data, rate_type="co2"), 2)

    return oxygen * co2


def solve_part_two(report: List[str]) -> int:
    width = len(report[0])

    def reduce(lines: List[str], filter_on="01") -> int:
        for k in range(width):
            threshold = (len(lines) + 1) // 2
            one_most_common = sum(line[k] == "1" for line in lines) >= threshold
            lines = [line for line in lines if line[k] == filter_on[one_most_common]]
            if len(lines) == 1:
                return int(lines[0], 2)

    oxygen_generator_rating = reduce(report)
    co2_scrubber_rating = reduce(report, filter_on="10")
    return oxygen_generator_rating * co2_scrubber_rating


@click.command()
@click.argument("input")
@click.option(
    "--test",
    default=False,
    is_flag=True,
    help="Runs this solution on test hard-coded inside the code",
)
def main(input, test):

    if test:
        data = """
        00100
        11110
        10110
        10111
        10101
        01111
        00111
        11100
        10000
        11001
        00010
        01010
        """.splitlines()
        print("used test data")

    else:
        data = open(input).read().splitlines()

    part_one_solution = solve_part_one(data)

    click.echo(f"PART ONE: {part_one_solution}")

    part_two_solution = solve_part_two(data)

    click.echo(f"PART TWO: {part_two_solution}")


if __name__ == "__main__":
    main()
