from collections import deque


#solve day 10 problem of the advent of code 2021
def solve_p1(data):

    """
        Solves the AoC 2021 day 10 problem for part 1
    """

    open_char = "(<{["
    close_char = "

    for string in data:

        stack =  deque()

        for c in string:

            if c in open_char:
                stack.append(c)

            else:






def main():

    data = open('input', 'r').read().splitlines()
    solve_p1(data)

if __name__ == "__main__":
    main()

