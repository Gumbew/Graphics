import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
import random

from classes.Polygon import Polygon
from classes.Point import Point
from classes.Line import Line


def main():
    p = Polygon([Point(0, 0), Point(2, 2), Point(1, 0), Point(3, -1)])
    p2 = Polygon([Point(0, 0), Point(2, 0), Point(2, 2), Point(1, 4), Point(0, 2)])
    p.output()
    print("Is convex: ", p.is_convex())
    print("Is convex: ", p2.is_convex())
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

    fig = plt.figure()
    ax = fig.add_subplot(111)
    patch = patches.PathPatch(path, fill=None, lw=2)
    ax.add_patch(patch)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)

    lines = list()
    lines.append(Line(Point(2, 0), Point(0, 4)))
    lines.append(Line(Point(-0.5, -0.5), Point(2.5, -0.5)))
    lines.append(Line(Point(-0.5, -0.5), Point(2.5, 2.5)))
    lines.append(Line(Point(0, -1), Point(3, 2)))
    lines.append(Line(Point(0.3, 0.3), Point(0.5, 1.5)))
    lines.append(Line(Point(-2, -2), Point(20, -2)))

    for i in lines:
        result, b = p2.cyruse_beck_out(i)
        if i.begin.x != b.begin.x and i.begin.y != b.begin.y:
            plt.plot([i.begin.x, b.begin.x], [i.begin.y, b.begin.y], 'k-', lw=2,
                     color=(random.random(), random.random(), random.random()))

        if i.end.x != b.end.x and i.end.y != b.end.y:
            plt.plot([i.end.x, b.end.x], [i.end.y, b.end.y], 'k-', lw=2,
                     color=(random.random(), random.random(), random.random()))

        if not result:
            plt.plot([i.begin.x, i.end.x], [i.begin.y, i.end.y], 'k-', lw=2,
                     color=(random.random(), random.random(), random.random()))

        print("Line: %s %s" % (i, result))

        # result,b = p2.cyruse_beck(i)
        # if (result):
        #     i = b
        #     plt.plot([i.begin.x, i.end.x], [i.begin.y, i.end.y], 'k-', lw=2,
        #               color=(random.random(), random.random(), random.random()))

    plt.show()


main()
