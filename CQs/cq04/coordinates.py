"""coordinates"""

__author__: str = "730812663"


def get_coords(xs: str, ys: str) -> None:
    index_xs = 0
    while index_xs < len(xs):
        index_ys = 0
        while index_ys < len(ys):
            print("(" + xs[index_xs] + "," + ys[index_ys] + ")")
            index_ys = index_ys + 1
        index_xs = index_xs + 1
