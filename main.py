import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
import random
import copy

from classes.Polygon import Polygon
from classes.Point import Point
from classes.Line import Line

fig = plt.figure()
ax = fig.add_subplot(111)


def draw_windows(p2):
    verticals = [
        (0., 0.),
        (2., 0.),
        (2., 2.),
        (1., 4.),
        (0., 2.),
        (0., 0.),
    ]

    codes = [Path.MOVETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.CLOSEPOLY,
             ]

    path = Path(verticals, codes)
    patch = patches.PathPatch(path, fill=None, lw=2, zorder=5, color=p2.color)
    ax.add_patch(patch)

    # verticals = [
    #     (0., 0.),
    #     (1., 0.),
    #     (1.5, 0.5),
    #     (1, 1),
    #     (0., 1.),
    #     (0., 0.),
    # ]
    #
    # codes = [Path.MOVETO,
    #          Path.LINETO,
    #          Path.LINETO,
    #          Path.LINETO,
    #          Path.LINETO,
    #          Path.CLOSEPOLY,
    #          ]
    #
    # path = Path(verticals, codes)
    #
    # patch = patches.PathPatch(path, fill=None, lw=2, zorder=10)
    # ax.add_patch(patch)
    #
    # verticals = [
    #     (3., 0.),
    #     (6., 0.),
    #     (7., 2.),
    #     (4.5, 3.),
    #     (2., 2.),
    #     (3., 0.),
    # ]
    #
    # codes = [Path.MOVETO,
    #          Path.LINETO,
    #          Path.LINETO,
    #          Path.LINETO,
    #          Path.LINETO,
    #          Path.CLOSEPOLY,
    #          ]
    #
    # path = Path(verticals, codes)
    #
    # patch = patches.PathPatch(path, fill=None, lw=2, zorder=10)
    # ax.add_patch(patch)

    ax.set_xlim(-5, 8)
    ax.set_ylim(-5, 8)


def out_print(lines, p):
    lines_copy = copy.copy(lines)
    for i in lines:
        result, b = p.cyruse_beck_out(i)
        if result:
            lines_copy.remove(i)
            lines_copy.extend(b)

    for i in lines_copy:
        plt.plot([i.begin.x, i.end.x], [i.begin.y, i.end.y], 'k-', lw=1,
                 color=i.color)


def in_print(lines, p):
    for line in lines:
        result, b = p.cyruse_beck(line)
        if result:
            line = b
            plt.plot([line.begin.x, line.end.x], [line.begin.y, line.end.y], 'k-', lw=2,
                     color=line.color)


def main():
    # p = Polygon([Point(0, 0), Point(1, 0), Point(1.5, 0.5), Point(1, 1), Point(0, 1)], 1)
    p2 = Polygon([Point(0, 0), Point(2, 0), Point(2, 2), Point(1, 4), Point(0, 2)], 2, "black")
    # p3 = Polygon([Point(3, 0), Point(6, 0), Point(7, 2), Point(4.5, 3), Point(2, 2)], 1)

    # print("Is convex: ", p.is_convex())
    print("Is convex: ", p2.is_convex())
    # print("Is convex: ", p3.is_convex())

    lines = list()

    lines.append(Line(Point(3.5, 0), Point(3.6, 3), "red"))
    lines.append(Line(Point(2, 0), Point(0, 4), "green"))
    lines.append(Line(Point(-0.5, -0.5), Point(2.5, -0.5), "magenta"))
    lines.append(Line(Point(-0.5, -0.5), Point(2.5, 2.5), "grey"))
    lines.append(Line(Point(0, -1), Point(3, 2), "blue"))
    lines.append(Line(Point(0.3, 0.3), Point(0.5, 1.5), "purple"))
    lines.append(Line(Point(-2, -2), Point(20, -2), "aqua"))
    lines.append(Line(Point(-2, 0.5), Point(20, 3), "pink"))

    out_print(lines, p2)
    # in_print(lines,p2)

    draw_windows(p2)
    plt.show()


main()
