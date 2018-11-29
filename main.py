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


def draw_windows():
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
    patch = patches.PathPatch(path, fill=None, lw=2, zorder=5)
    ax.add_patch(patch)

    verticals = [
        (0., 0.),
        (1., 0.),
        (1.5, 0.5),
        (1, 1),
        (0., 1.),
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

    patch = patches.PathPatch(path, fill=None, lw=2, zorder=10)
    ax.add_patch(patch)

    verticals = [
        (3., 0.),
        (6., 0.),
        (7., 2.),
        (4.5, 3.),
        (2., 2.),
        (3., 0.),
    ]

    codes = [Path.MOVETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.CLOSEPOLY,
             ]

    path = Path(verticals, codes)

    patch = patches.PathPatch(path, fill=None, lw=2, zorder=10)
    ax.add_patch(patch)

    ax.set_xlim(-5, 8)
    ax.set_ylim(-5, 8)


def out_print(i, p, count, colors):
    result, b = p.cyruse_beck_out(i)
    if i.begin.x != b.begin.x and i.begin.y != b.begin.y:
        plt.plot([i.begin.x, b.begin.x], [i.begin.y, b.begin.y], 'k-', lw=1,
                 color=(random.random(), random.random(), random.random()))

    if i.end.x != b.end.x and i.end.y != b.end.y:
        plt.plot([i.end.x, b.end.x], [i.end.y, b.end.y], 'k-', lw=1,
                 color=(random.random(), random.random(), random.random()))

    if not result:
        plt.plot([i.begin.x, i.end.x], [i.begin.y, i.end.y], 'k-', lw=1,
                 color=(random.random(), random.random(), random.random()))

    print("Line: %s %s" % (i, result))


def in_print(i, p, count, colors):
    result, b = p.cyruse_beck(i)
    if result:
        i = b
        plt.plot([i.begin.x, i.end.x], [i.begin.y, i.end.y], 'k-', lw=1,
                 color=(colors[count], colors[count + 1], colors[count + 2]))
    count += 3


def main():
    p = Polygon([Point(0, 0), Point(1, 0), Point(1.5, 0.5), Point(1, 1), Point(0, 1)], 1)
    p2 = Polygon([Point(0, 0), Point(2, 0), Point(2, 2), Point(1, 4), Point(0, 2)], 2)
    p3 = Polygon([Point(3, 0), Point(6, 0), Point(7, 2), Point(4.5, 3), Point(2, 2)], 1)

    print("Is convex: ", p.is_convex())
    print("Is convex: ", p2.is_convex())
    print("Is convex: ", p3.is_convex())

    lines = list()

    lines.append(Line(Point(3.5, 0), Point(3.6, 3)))
    lines.append(Line(Point(2, 0), Point(0, 4)))
    lines.append(Line(Point(-0.5, -0.5), Point(2.5, -0.5)))
    lines.append(Line(Point(-0.5, -0.5), Point(2.5, 2.5)))
    lines.append(Line(Point(0, -1), Point(3, 2)))
    lines.append(Line(Point(0.3, 0.3), Point(0.5, 1.5)))
    lines.append(Line(Point(-2, -2), Point(20, -2)))
    lines.append(Line(Point(-2, 0.5), Point(20, 3)))

    lines1 = copy.copy(lines)
    lines2 = copy.copy(lines)
    lines3 = copy.copy(lines)

    colors = list()
    for i in range(len(lines) * 3):
        colors.append(random.random())
    count = 0

    for i in lines1:
        in_print(i, p, count, colors)
        count += 3

    count = 0
    for i in lines2:
        #in_print(i, p2, count, colors)
        out_print(i, p2, count, colors)
        count += 3

    count = 0

    for i in lines3:
        in_print(i, p3, count, colors)
        count += 3

    draw_windows()
    plt.show()


main()
