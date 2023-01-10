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
        # DrawTriangleStrip(strip, 4, color);
        return (x + math.cos(math.radians(degree)) * rx,
                y + math.sin(math.radians(degree)) * ry)


    @classmethod
    def draw_ellipse_line_py(cls, x, y, rx, ry, stroke_width, color):
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
        for i in range(0, len(points) - 1):
            point = points[i]
            next_point = points[i + 1]
            delta = (next_point[0] - point[0], next_point[1] - point[1])
            length = math.dist(point, next_point)
            scale = stroke_width / (2 * length)
            radius = -scale * delta[1], scale * delta[0]
            stripes.append((point[0] - radius[0], point[1] - radius[1]))
            stripes.append((point[0] + radius[0], point[1] + radius[1]))
            stripes.append((next_point[0] - radius[0], next_point[1] - radius[1]))
            stripes.append((next_point[0] + radius[0], next_point[1] + radius[1]))
        rl.DrawTriangleStrip(stripes, len(stripes), color)

if __name__ == '__main__':
    print(ShapeConfig.ellipse_coor_by_degree(50, 50, 40, 30, 0))