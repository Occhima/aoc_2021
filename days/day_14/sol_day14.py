from collections import deque
from itertools import islice


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def solve_p1(n_steps: int, initial_string: str, polymers: str = None) -> int:

    final_str = initial_string

    for _ in range(n_steps):
        for index, pair in enumerate(sliding_window(final_str, 2)):
            print(index, pair)


def main():

    data = open("input").read().splitlines()
    solve_p1(10, data[0])


if __name__ == "__main__":
    main()
