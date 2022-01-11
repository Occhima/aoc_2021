import os, click


@click.command()
@click.argument("input")
def main(input):

    """
    Reads an input file from the advent of code and proceeds with day 2 solution
    """

    user_input = open(input).readlines()


if __name__ == "__main__":
    main()
