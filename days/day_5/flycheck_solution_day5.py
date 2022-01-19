from __future__ import annotations
import click, typing as t
from dataclasses import dataclass
from heapq import heappush, heappop
from itertools import repeat
from math import copysign
from typing import Iterable, NamedTuple


class Point(NamedTuple):
    x: int
    y: int

    def __str__(self) -> str:
        return f"{self.x},{self.y}"

    @classmethod
    def from_str(cls, s: str) -> Point:
        return cls(*map(int, s.split(",")))


@dataclass(order=True)
class Line:
    start: Point
    end: Point

    @classmethod
    def from_string(cls, line: str) -> Line:
        # start should always be to the left / above from end, so all our
        # lines run from left to right or top to bottom (not counting diagonal
        # slopes going up)
        return cls(*sorted(map(Point.from_str, line.split("->"))))

    @property
    def straight(self) -> bool:
        return self.start.x == self.end.x or self.start.y == self.end.y

    def __str__(self) -> str:
        return f"{self.start} -> {self.end}"

    def __mul__(self, p: Point) -> int:
        """Calculate the cross-product of this line and point p"""
        dx, dy = self.end.x - self.start.x, self.end.y - self.start.y
        return dx * (p.y - self.start.y) - (p.x - self.start.x) * dy

    def __and__(self, other: Line) -> Iterable[Point]:
        """Yield all points at which this line intersects with other"""
        sstart, send, ostart, oend = self.start, self.end, other.start, other.end

        # check for the cross-product of the two lines to check if they intersect
        cross_sos, cross_soe = self * ostart, self * oend
        cpother = (other * sstart) * (other * send)
        if not ((cross_sos * cross_soe <= 0 and cpother <= 0) or not cross_sos):
            return

        # find if two line segments intersect, and where, adapted from
        # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
        sdx, sdy = send.x - sstart.x, send.y - sstart.y
        odx, ody = oend.x - ostart.x, oend.y - ostart.y

        # With integer coordinates we need to account for diagonal lines
        # passing one another and not actually intersecting, which happens
        # when they run along 'odd' and 'even' diagonals
        if not (self.straight or other.straight):
            # intercepts of the diagonals must both be odd or even
            sparity = (sstart.y + (sdy // sdx) * sstart.x) % 2
            oparity = (ostart.y + (ody // odx) * ostart.x) % 2
            if sparity != oparity:
                return

        denom = sdx * ody - odx * sdy
        if denom:
            # there is a single intersection point
            num = odx * (sstart.y - ostart.y) - ody * (sstart.x - ostart.x)
            yield Point(sstart.x + sdx * num // denom, sstart.y + sdy * num // denom)
        else:
            # lines overlap along a segment
            xs = range(ostart.x, min(send.x, oend.x) + 1) if sdx else repeat(ostart.x)
            # match sdy:
            #     case 0:
            #         ys = repeat(ostart.y)
            #     case _ if sdy < 0:
            #         ys = range(ostart.y, max(send.y, oend.y) - 1, -1)
            #     case _:  # > 0
            #         ys = range(ostart.y, min(send.y, oend.y) + 1)
            # match sdy:
            ys = repeat(ostart.y)

            if sdy < 0:
                ys = range(ostart.y, max(send.y, oend.y) - 1, -1)
            else:  # > 0
                ys = range(ostart.y, min(send.y, oend.y) + 1)
            yield from (Point(x, y) for x, y in zip(xs, ys))


@dataclass
class HydrothermalVents:
    lines: list[Line]

    @classmethod
    def from_lines(
        cls, lines: list[str], ignore_diagonals: bool = True
    ) -> HydrothermalVents:
        vents = map(Line.from_string, lines)
        if ignore_diagonals:
            vents = (line for line in vents if line.straight)
        return cls(sorted(vents))

    def count_most_dangerous(self) -> int:
        # heap with (end, line), endpoints per still-active lines
        queue: list[tuple[Point, Line]] = []
        # all points touched by 2 or more lines.
        overlaps: set[Point] = set()
        for line in self.lines:
            # clear queued lines no longer active (.end to left or above this line)
            while queue and queue[0][0] < line.start:
                heappop(queue)
            overlaps |= {p for _, other in queue for p in other & line}
            heappush(queue, (line.end, line))
        return len(overlaps)


@click.command()
@click.argument("input_data")
@click.option(
    "--test",
    default=False,
    is_flag=True,
    help="Runs this solution on test hard-coded inside the code",
)
def main(input_data, test):

    data = open(input_data).read().splitlines()

    click.echo(f"Part One: {HydrothermalVents.from_lines(data).count_most_dangerous()}")
    click.echo(
        f"Part Two: {HydrothermalVents.from_lines(data, False).count_most_dangerous()}"
    )


if __name__ == "__main__":
    main()
