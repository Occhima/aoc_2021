from __future__ import annotations
from collections import Counter, deque
from itertools import islice
from collections import Counter
from dataclasses import dataclass, replace
from functools import cached_property
from itertools import islice
from dataclasses import dataclass
from typing import Iterator, NamedTuple, Dict


Rules: Dict[str, tuple[str, str]]


class Extremes(NamedTuple):
    min: int
    max: int


@dataclass(frozen=True)
class Polymerization:
    chain: Counter[str]
    last: str
    rules: Rules

    @classmethod
    def from_instructions(cls, instructions: str) -> Polymerization:
        templ, rulelines = instructions.split("\n\n")
        template = Counter(f"{l1}{l2}" for l1, l2 in zip(templ, templ[1:]))
        rule_pairs = (line.split(" -> ") for line in rulelines.splitlines())
        rules = {
            pair: (f"{pair[0]}{target}", f"{target}{pair[1]}")
            for pair, target in rule_pairs
        }
        return cls(template, templ[-1], rules)

    def __len__(self) -> int:
        return self.chain.total() + 1

    def __iter__(self) -> Iterator[Polymerization]:
        step, rules = self, self.rules
        while True:
            chain = Counter()
            for pair, count in step.chain.items():
                for new in rules[pair]:
                    chain[new] += count
            yield (step := replace(step, chain=chain))

    @cached_property
    def extremes(self) -> Extremes:
        elems = Counter(self.last)
        for (elem, _), count in self.chain.items():
            elems[elem] += count
        return Extremes(min(elems.values()), max(elems.values()))


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def solve_p1(polymer: str, polymers_map: dict, n_steps: int = 10) -> str:

    final_polymer = polymer

    print(f"Template: {final_polymer}")

    for i in range(n_steps):

        for index, pair in enumerate(sliding_window(polymer, 2)):
            final_polymer = (
                final_polymer[:index]
                + polymers_map["".join(pair)]
                + final_polymer[index:]
            )

        print(f"After step {i}: {final_polymer}")

    return final_polymer


def main():

    data = open("input").read()

    reaction = Polymerization.from_instructions(data)

    step10 = next(islice(reaction, 9, None))  # skip 9 steps to get to step 10

    print("Part 1:", step10.extremes.max - step10.extremes.min)

    step40 = next(islice(step10, 29, None))  # 30 steps onwards from step10
    print("Part 2:", step40.extremes.max - step40.extremes.min)


if __name__ == "__main__":
    main()
