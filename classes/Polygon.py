from classes.Line import Line


class Polygon(object):
    def __init__(self, points, priority):
        self.count = len(points)
        self.edges = []
        self.priority = priority
        for i in range(self.count - 1):
            self.edges.append(Line(points[i], points[i + 1]))

        self.edges.append(Line(points[-1], points[0]))

    def output(self):
        for i in self.edges:
            print(i)

    def is_convex(self):
        d = []
        for i in range(self.count - 1):
            d.append((self.edges[i].end.x - self.edges[i].begin.x) *
                     (self.edges[i + 1].end.y - self.edges[i + 1].begin.y) -
                     (self.edges[i].end.y - self.edges[i].begin.y) *
                     (self.edges[i + 1].end.x - self.edges[i + 1].begin.x))
        pos_count = 0
        neg_count = 0
        for i in d:
            if i > 0:
                pos_count += 1
            else:
                neg_count += 1

        if pos_count and neg_count:
            return False
        else:
            return True

    @property
    def get_priority(self):
        return self.priority

    def cyruse_beck(self, l):
        t_begin = 0.0
        t_end = 1.0
        dir_l = l.direction

        for edge in self.edges:
            if edge.normal.dot(dir_l) < 0:
                t = l.intersection_parameter(edge)
                if t > t_begin:
                    t_begin = t

            if edge.normal.dot(dir_l) > 0:
                t = l.intersection_parameter(edge)
                if t < t_end:
                    t_end = t

            if edge.normal.dot(dir_l) == 0:
                if not edge.on_left(l.begin):
                    return False, l
        if t_begin > t_end:
            return False, l

        l = l.morph(t_begin, t_end)
        return True, l

    def cyruse_beck_out(self, l):
        t_begin = 0.0
        t_end = 1.0
        dir_l = l.direction

        for edge in self.edges:
            if edge.normal.dot(dir_l) < 0:
                t = l.intersection_parameter(edge)
                if t > t_begin:
                    t_begin = t

            if edge.normal.dot(dir_l) > 0:
                t = l.intersection_parameter(edge)
                if t < t_end:
                    t_end = t

            if edge.normal.dot(dir_l) == 0:
                if not edge.on_left(l.begin):
                    return False, l

        l = l.morph(t_begin, t_end)
        if t_begin > t_end:
            return False, l

        return True, l
