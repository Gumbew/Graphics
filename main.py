import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
import copy

from classes.Polygon import Polygon
from classes.Point import Point
from classes.Line import Line

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(-5, 8)
ax.set_ylim(-5, 8)


def draw_window(figure, lines):
    verticals = list()
    for edge in figure.edges:
        verticals.append((edge.begin.x, edge.begin.y))
    verticals.append((figure.edges[0].begin.x, figure.edges[0].begin.y))

    codes = [Path.MOVETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.CLOSEPOLY,
             ]

    path = Path(verticals, codes)
    patch = patches.PathPatch(path, fill=None, lw=2, zorder=5, color=figure.color)
    ax.add_patch(patch)
    in_print(lines,figure)
    # out_print(lines,figure)


def draw_windows(figures):
    for figure in figures:
        verticals = list()
        for edge in figure.edges:
            verticals.append((edge.begin.x, edge.begin.y))
        verticals.append((figure.edges[0].begin.x, figure.edges[0].begin.y))

        codes = [Path.MOVETO,
                 Path.LINETO,
                 Path.LINETO,
                 Path.LINETO,
                 Path.LINETO,
                 Path.CLOSEPOLY,
                 ]

        path = Path(verticals, codes)
        patch = patches.PathPatch(path, fill=None, lw=3, zorder=figure.priority, color=figure.color)
        ax.add_patch(patch)


def print_curus(figures, lines):
    c = 0
    figures.sort(key=lambda x: x.priority, reverse=True)
    lines_copy = copy.copy(lines)
    for figure in figures:
        lines = lines_copy

        in_print(lines, figure)
        for i in lines:
            result, b = figure.cyruse_beck_out(i)
            if result:
                lines_copy.remove(i)
                lines_copy.extend(b)
        print('\n', c)
        c += 1
        for i in lines:
            print(i)


def out_print(lines, p):
    lines_copy = copy.copy(lines)
    for i in lines:
        result, b = p.cyruse_beck_out(i)
        if result:
            lines_copy.remove(i)
            lines_copy.extend(b)

    for i in lines_copy:
        plt.plot([i.begin.x, i.end.x], [i.begin.y, i.end.y], 'k-', lw=1,
                 color=i.color, zorder=p.priority - 1)
    return lines_copy


def in_print(lines, p):
    for line in lines:
        result, b = p.cyruse_beck(line)
        if result:
            line = b
            plt.plot([line.begin.x, line.end.x], [line.begin.y, line.end.y], 'k-', lw=2,
                     color=line.color, zorder=p.priority - 1)
    return lines


def main():
    figures = list()
    figures.append(Polygon([Point(0, 0), Point(1, 0), Point(1.5, 0.5), Point(1, 1), Point(0, 1)], 1, "blue"))
    figures.append(Polygon([Point(0, 0), Point(2, 0), Point(2, 2), Point(1, 4), Point(0, 2)], 5, "black"))
    figures.append(Polygon([Point(3, 0), Point(6, 0), Point(7, 2), Point(4.5, 3), Point(2, 2)], 0, "grey"))

    for i in figures:
        print("Is convex: ", i.is_convex())

    lines = list()

    lines.append(Line(Point(3.5, 0), Point(3.6, 3), "red"))
    lines.append(Line(Point(2, 0), Point(0, 4), "green"))
    lines.append(Line(Point(-0.5, -0.5), Point(2.5, -0.5), "magenta"))
    lines.append(Line(Point(-0.5, -0.5), Point(2.5, 2.5), "grey"))
    lines.append(Line(Point(0, -1), Point(3, 2), "blue"))
    lines.append(Line(Point(0.3, 0.3), Point(0.5, 1.5), "purple"))
    lines.append(Line(Point(-2, -2), Point(20, -2), "aqua"))
    lines.append(Line(Point(-2, 0.5), Point(20, 3), "pink"))

    draw_window(figures[1], lines)

    # print_curus(figures, lines)
    # draw_windows(figures)

    plt.show()


main()
