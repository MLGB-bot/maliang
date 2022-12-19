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
    stroke_width = 1
    stroke_color = pr.BLACK
    filled_color = pr.WHITE


    def __init__(self):
        pass

    @classmethod
    def format_color(self, color):
        obj_color = MColor(*color)
        return tuple(obj_color)

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
            self.filled_color = self.format_color(color)

    @classmethod
    def stroke(self, color: tuple = None, width: float = None):
        self._stroke = True
        if color is not None:
            self.stroke_color = self.format_color(color)
        if width is not None:
            self.stroke_width = width

    @classmethod
    def init_stroke_width(self, stroke_width):
        if stroke_width is not None:
            return stroke_width
        elif self._stroke:
            return self.stroke_width
        return None

    @classmethod
    def init_stroke_color(self, stroke_color):
        if stroke_color:
            return self.format_color(stroke_color)
        elif self._stroke:
            return self.stroke_color
        return None

    @classmethod
    def init_filled_color(self, filled_color: tuple):
        if filled_color:
            return self.format_color(filled_color)
        elif self._fill:
            return self.filled_color
        return None
