from classes.Point import Point


class Line(object):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def __str__(self):
        return "{%s - %s}" % (self.begin, self.end)

    @property
    def direction(self):
        return Point(self.end.x - self.begin.x, self.end.y - self.begin.y)

    @property
    def normal(self):
        return Point(self.end.y - self.begin.y, self.begin.x - self.end.x)

    def intersection_parameter(self, that):
        segment_to_edge = that.begin.sub(self.begin)
        segment_dir = self.direction
        edge_dir = that.direction

        if edge_dir.cross(segment_dir) == 0:
            t = 0
        else:
            t = edge_dir.cross(segment_to_edge) / edge_dir.cross(segment_dir)

        return t

    def on_left(self, other):
        ab = Point(self.end.x - self.begin.x, self.end.y - self.begin.y)
        ap = Point(other.x - self.begin.x, other.y - self.begin.y)
        return ab.cross(ap) >= 0

    def morph(self, t_begin, t_end):
        return Line(self.begin.add(self.direction.mul(t_begin)), self.begin.add(self.direction.mul(t_end)))
