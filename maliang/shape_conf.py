import math

import pyray as pr
import raylib as rl
from maliang.structs import MColor


class ShapeConfig(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    # def __call__(self, *args, **kwargs):
    #     print("call ...")

    _stroke = True
    _fill = True
    _stroke_width = 1
    _stroke_color = MColor(*pr.BLACK)
    _filled_color = MColor(*pr.WHITE)


    def __init__(self):
        pass

    @property
    def filled_color(self):
        return self._filled_color

    @property
    def stroke_color(self):
        return self._stroke_color

    @property
    def stroke_width(self):
        return self._stroke_width

    @classmethod
    def format_color(self, color):
        if isinstance(color, MColor):
            return color
        return MColor(*color)

    @classmethod
    def no_fill(self):
        self._fill = False

    @classmethod
    def no_stroke(self):
        self._stroke = False

    @classmethod
    def fill(self, *color):
        self._fill = True
        if color:
            self._filled_color = self.format_color(color)

    @classmethod
    def stroke(self, color: tuple = None, width: float = None):
        self._stroke = True
        if color is not None:
            self._stroke_color = self.format_color(color)
        if width is not None:
            self._stroke_width = width

    @classmethod
    def init_stroke_width(self, kwargs):
        if kwargs and "stroke_width" in kwargs:
            return kwargs['stroke_width']
        elif self._stroke:
            return self._stroke_width
        return None

    @classmethod
    def init_stroke_color(self, kwargs):
        if kwargs and "stroke_color" in kwargs:
            return self.format_color(kwargs['stroke_color']) if kwargs['stroke_color'] else None
        elif self._stroke:
            return self._stroke_color
        return None

    @classmethod
    def init_filled_color(self, kwargs):
        if kwargs and "filled_color" in kwargs:
            return self.format_color(kwargs['filled_color']) if kwargs['filled_color'] else None
        elif self._fill:
            return self._filled_color
        return None

    @classmethod
    def calc_polygon_area(cls, points):
        area = 0
        for index, point in enumerate(points):
            neighboor_index = (index + 1) % len(points)
            area += point[0] * points[neighboor_index][1] - point[1] * points[neighboor_index][0]
        return area * 0.5

    @classmethod
    def ellipse_coor_by_degree(cls, x, y, rx, ry, degree):
        return (x + math.cos(math.radians(degree)) * rx,
                y + math.sin(math.radians(degree)) * ry)

    @classmethod
    def circle_coor_by_degree(cls, x, y, r, degree):
        return (x + math.cos(math.radians(degree)) * r,
                y + math.sin(math.radians(degree)) * r)


    @classmethod
    def draw_ellipse_lines_py(cls, x, y, rx, ry, stroke_width, color):
        points0 = []  # 0~90
        points1 = []  # 90~180
        points2 = []  # 180~270
        points3 = []  # 270~360

        for degree in range(0, 90, 10):
            _x, _y = cls.ellipse_coor_by_degree(x, y, rx, ry, degree)
            points0.append((_x, _y))
            points1.append((2 * x - _x, _y))
            if degree > 0:
                points2.append((2 * x - _x, 2 * y - _y))
            points3.append((_x, 2 * y - _y))

        _x, _y = cls.ellipse_coor_by_degree(x, y, rx, ry, 90)
        points0.append((_x, _y))
        points2.append((2 * x - _x, 2 * y - _y))

        points1.reverse()
        points3.reverse()

        points = [
            *points0,
            *points1,
            *points2,
            *points3
        ]

        stripes = []
        for i in range(0, len(points) - 2):
            point = points[i]
            next_point = points[i + 1]
            delta = (next_point[0] - point[0], next_point[1] - point[1])
            length = math.dist(point, next_point)
            scale = stroke_width / (2 * length)
            radius = -scale * delta[1], scale * delta[0]
            if not stripes:
                # 第一个点
                stripes.append((point[0] - radius[0], point[1] - radius[1]))
                stripes.append((point[0] + radius[0], point[1] + radius[1]))
            # 中间点
            stripes.append((next_point[0] - radius[0], next_point[1] - radius[1]))
            stripes.append((next_point[0] + radius[0], next_point[1] + radius[1]))
        # 最后一个点 直接合并到起点
        stripes.append(stripes[0])
        stripes.append(stripes[1])
        rl.DrawTriangleStrip(stripes, len(stripes), color)

    @classmethod
    def draw_triangles(cls, triangles, color):
        rl.rlBegin(0x0004)
        rl.rlColor4ub(*color)
        for point in triangles:
            rl.rlVertex2f(*point)
        rl.rlEnd()

    @classmethod
    def draw_lines(cls, lines, color):
        rl.rlBegin(0x0001)
        rl.rlColor4ub(*color)
        for point in lines:
            rl.rlVertex2f(*point)
        rl.rlEnd()

    @classmethod
    def draw_quads(cls, quads, color):
        rl.rlBegin(0x0007)
        rl.rlColor4ub(*color)
        for point in quads:
            rl.rlVertex2f(*point)
        rl.rlEnd()


    @classmethod
    def draw_arc_py(cls, x, y, rx, ry, start_angle, end_angle, segments=30, shape=1,
                            stroke_width=1, stroke_color=None, filled_color=None):
        # DrawEllipse
        """
        :param x:
        :param y:
        :param rx:
        :param ry:
        :param start_angle:
        :param end_angle:
        :param stroke_width:
        :param stroke_color:
        :param filled_color:
        :param segments:
        :param shape:
            PIE: 1
            OPEN_PIE: 2
            CHORD: 3
            OPEN_CHORD: 4
        :return:
        """
        points = []
        steper = (end_angle - start_angle) // segments or 1
        degree = start_angle
        for degree in range(start_angle, end_angle, steper):
            _x, _y = cls.circle_coor_by_degree(x, y, rx, degree) if rx==ry \
                else cls.ellipse_coor_by_degree(x, y, rx, ry, degree)
            points.append((_x, _y))
        if degree < end_angle:
            _x, _y = cls.circle_coor_by_degree(x, y, rx, end_angle) if rx==ry \
                else cls.ellipse_coor_by_degree(x, y, rx, ry, end_angle)
            points.append((_x, _y))

        triangles = []
        stripes = []
        lines = []
        for i in range(0, len(points) - 1):
            point = points[i]
            next_point = points[i + 1]
            if filled_color:
                if shape in (1, 2):
                    triangles.append((x, y))
                elif shape in (3, 4):
                    triangles.append(points[-1])
                triangles.append(next_point)
                triangles.append(point)
            if stroke_width and stroke_color:
                if stroke_width == 1:
                    lines.append(point)
                    lines.append(next_point)
                else:
                    delta = (next_point[0] - point[0], next_point[1] - point[1])
                    length = math.dist(point, next_point)
                    scale = stroke_width / (2 * length)
                    radius = -scale * delta[1], scale * delta[0]
                    if not stripes:
                        # 第一个点
                        stripes.append((point[0] - radius[0], point[1] - radius[1]))
                        stripes.append((point[0] + radius[0], point[1] + radius[1]))
                    # 中间点
                    stripes.append((next_point[0] - radius[0], next_point[1] - radius[1]))
                    stripes.append((next_point[0] + radius[0], next_point[1] + radius[1]))

        if triangles:
            cls.draw_triangles(triangles, filled_color)

        if stripes:
            if shape == 1:
                # PIE
                rl.DrawLineEx(pr.Vector2(*points[0]), pr.Vector2(x, y), stroke_width, stroke_color)
                rl.DrawLineEx(pr.Vector2(*points[-1]), pr.Vector2(x, y), stroke_width, stroke_color)
            elif shape == 3:
                # CHORD
                rl.DrawLineEx(pr.Vector2(*points[0]), pr.Vector2(*points[-1]), stroke_width, stroke_color)
            rl.DrawTriangleStrip(stripes, len(stripes), stroke_color)
        elif lines:
            if shape == 1:
                # PIE
                lines.append(points[0])
                lines.append((x, y))
                lines.append(points[-1])
                lines.append((x, y))
            elif shape == 3:
                # CHORD
                lines.append(points[0])
                lines.append(points[-1])
            cls.draw_lines(lines, stroke_color)

