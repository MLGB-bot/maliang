import pyray as pr
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
