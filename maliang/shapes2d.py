import pyray as pr
from maliang.units import RectMode, EllipseMode, CircleMode
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


class Shapes2d(ShapeConfig):
    def __init__(self):
        ShapeConfig().__init__()
        self._rect_mode = RectMode.CORNER
        self._ellipse_mode = EllipseMode.CENTER
        self._circle_mode = CircleMode.CENTER


    def rect_mode(self, mode):
        assert isinstance(mode, (str, int))
        if isinstance(mode, str):
            assert hasattr(RectMode, mode)
            self._rect_mode = getattr(RectMode, mode)
        elif isinstance(mode, int):
            assert mode in RectMode.__values__
            self._rect_mode = mode

    def ellipse_mode(self, mode):
        assert isinstance(mode, (str, int))
        if isinstance(mode, str):
            assert hasattr(EllipseMode, mode)
            self._ellipse_mode = getattr(EllipseMode, mode)
        elif isinstance(mode, int):
            assert mode in EllipseMode.__values__
            self._ellipse_mode = mode

    def circle_mode(self, mode):
        assert isinstance(mode, (str, int))
        if isinstance(mode, str):
            assert hasattr(CircleMode, mode)
            self._circle_mode = getattr(CircleMode, mode)
        elif isinstance(mode, int):
            assert mode in CircleMode.__values__
            self._circle_mode = mode


    def point(self, x, y, stroke_width=None, stroke_color: tuple = None, shape="circle"):
        stroke_width = self.init_stroke_width(stroke_width)
        stroke_color = self.init_stroke_color(stroke_color)
        if stroke_width and stroke_color:
            if stroke_width > 1:
                # 画一个圆
                if shape == "circle":
                    pr.draw_circle(x, y, stroke_width * 0.5, pr.Color(*stroke_color))
                elif shape == 'rect':
                    pr.draw_rectangle(x, y, stroke_width, stroke_width, pr.Color(*stroke_color))
            elif stroke_width == 1:
                # 画一个像素
                pr.draw_pixel(x, y, stroke_color)

    def line(self, x1, y1, x2, y2, stroke_width=None, stroke_color: tuple = None):
        stroke_width = self.init_stroke_width(stroke_width)
        stroke_color = self.init_stroke_color(stroke_color)
        if stroke_width and stroke_color:
            pr.draw_line_ex(
                pr.Vector2(int(x1), int(y1)),
                pr.Vector2(int(x2), int(y2)),
                stroke_width,
                pr.Color(*stroke_color),
            )
        elif stroke_color:
            pr.draw_line(int(x1), int(y1), int(x2), int(y2), pr.Color(*stroke_color), )

    def rect(self, x, y, w, h, stroke_width=None, stroke_color: tuple = None, filled_color: tuple = None, mode=None):
        stroke_width = self.init_stroke_width(stroke_width)
        stroke_color = self.init_stroke_color(stroke_color)
        filled_color = self.init_filled_color(filled_color)

        mode = mode or self._rect_mode

        def init_mode(rect_mode):
            if rect_mode == RectMode.CORNER:
                return x, y, w, h
            elif rect_mode == RectMode.CENTER:
                return int(x - w * 0.5), int(y - h * 0.5), w, h
            elif rect_mode == RectMode.RADIUS:
                return x - w, y - h, 2 * w, 2 * h
            elif rect_mode == RectMode.CORNERS:
                return min(x, w), min(y, h), abs(x - w), abs(y - h)
            else:
                return x, y, w, h

        _x, _y, _w, _h = init_mode(mode)
        # draw
        if filled_color:
            pr.draw_rectangle(_x, _y, _w, _h, pr.Color(*filled_color))
        if stroke_width and stroke_color:
            if stroke_width == 1:
                pr.draw_rectangle_lines(_x, _y, _w, _h, pr.Color(*stroke_color))
            else:
                pr.draw_rectangle_lines_ex(pr.Rectangle(_x, _y, _w, _h), stroke_width, pr.Color(*stroke_color))

    def circle(self, x, y, d, stroke_width=None, stroke_color: tuple = None, filled_color: tuple = None, segments=30,
               mode=None):
        stroke_width = self.init_stroke_width(stroke_width)
        stroke_color = self.init_stroke_color(stroke_color)
        filled_color = self.init_filled_color(filled_color)
        mode = mode or self._circle_mode
        # draw
        def init_mode(rect_mode):
            if rect_mode == CircleMode.CORNER:
                return int(x + d * 0.5), int(y + d * 0.5), d * 0.5
            elif rect_mode == CircleMode.CENTER:
                return x, y, d*0.5
            elif rect_mode == CircleMode.RADIUS:
                return x, y, d
            else:
                return x, y, d*0.5

        _x, _y, _r = init_mode(mode)

        if filled_color:
            pr.draw_circle(_x, _y, _r, pr.Color(*filled_color))
        if stroke_width and stroke_color:
            if stroke_width == 1:
                pr.draw_circle_lines(_x, _y, _r, pr.Color(*stroke_color))
            elif stroke_width > 1:
                pr.draw_ring(pr.Vector2(_x, _y), _r - stroke_width * 0.5, _r + stroke_width * 0.5, 0, 360, segments,
                             pr.Color(*stroke_color))

    def ellipse(self, x, y, w, h, stroke_width=None, stroke_color: tuple = None, filled_color: tuple = None, mode=None):
        stroke_width = self.init_stroke_width(stroke_width)
        stroke_color = self.init_stroke_color(stroke_color)
        filled_color = self.init_filled_color(filled_color)
        mode = mode or self._ellipse_mode

        def init_mode(rect_mode):
            if rect_mode == EllipseMode.CORNER:
                return int(x + w * 0.5), int(y + h * 0.5), w * 0.5, h * 0.5
            elif rect_mode == EllipseMode.CENTER:
                return x, y, w * 0.5, h * 0.5
            elif rect_mode == EllipseMode.RADIUS:
                return x, y, w, h
            elif rect_mode == EllipseMode.CORNERS:
                return int(0.5 * (x + w)), int(0.5 * (y + h)), abs(x - w) * 0.5, abs(y - h) * 0.5
            else:
                return x, y, w * 0.5, h * 0.5

        _x, _y, _w, _h = init_mode(mode)
        # draw
        if filled_color:
            pr.draw_ellipse(_x, _y, _w, _h, pr.Color(*filled_color))
        if stroke_width and stroke_color:
            if stroke_width == 1:
                pr.draw_ellipse_lines(_x, _y, _w, _h, pr.Color(*stroke_color))
            elif stroke_width > 1:
                # todo draw ellipse stroke lines
                pr.draw_ellipse_lines(_x, _y, _w, _h, pr.Color(*stroke_color))

    def arc(self, x, y, rx, ry, start_angle, end_angle, stroke_width=None, stroke_color: tuple = None,
            filled_color: tuple = None, segments=30):
        stroke_width = self.init_stroke_width(stroke_width)
        stroke_color = self.init_stroke_color(stroke_color)
        filled_color = self.init_filled_color(filled_color)
        if rx == ry:
            if filled_color:
                pr.draw_circle_sector(pr.Vector2(x, y), rx, start_angle, end_angle, segments, pr.Color(*filled_color))
            if stroke_width and stroke_color:
                if stroke_width == 1:
                    pr.draw_circle_sector_lines(pr.Vector2(x, y), rx, start_angle, end_angle, segments,
                                                pr.Color(*stroke_color))
                elif stroke_width > 1:
                    # todo draw arc stroke lines
                    pr.draw_circle_sector_lines(pr.Vector2(x, y), rx, start_angle, end_angle, segments,
                                                pr.Color(*stroke_color))
        else:
            # todo from ellipse
            pass

    def ring(self, x, y, d1, d2, stroke_width=None, stroke_color: tuple = None, filled_color: tuple = None,
             segments=30, mode=None):
        stroke_width = self.init_stroke_width(stroke_width)
        stroke_color = self.init_stroke_color(stroke_color)
        filled_color = self.init_filled_color(filled_color)

        mode = mode or self._circle_mode
        # draw
        def init_mode(rect_mode):
            if rect_mode == CircleMode.CORNER:
                dm = max(d1, d2)
                return int(x + dm * 0.5), int(y + dm * 0.5), d1 * 0.5, d2 * 0.5
            elif rect_mode == CircleMode.CENTER:
                return x, y, d1 * 0.5, d2 * 0.5
            elif rect_mode == CircleMode.RADIUS:
                return x, y, d1, d2
            else:
                return x, y, d1 * 0.5, d2 * 0.5

        _x, _y, _ri, _ro = init_mode(mode)

        if filled_color:
            pr.draw_ring(pr.Vector2(_x, _y), _ri, _ro, 0, 360, segments, pr.Color(*filled_color))
        if stroke_width and stroke_color:
            if stroke_width == 1:
                pr.draw_ring_lines(pr.Vector2(_x, _y), _ri, _ro, 0, 360, segments, pr.Color(*stroke_color))
            elif stroke_width > 1:
                pr.draw_ring(pr.Vector2(_x, _y), _ri - stroke_width * 0.5, _ri + stroke_width * 0.5, 0, 360, segments,
                             pr.Color(*stroke_color))
                pr.draw_ring(pr.Vector2(_x, _y), _ri - stroke_width * 0.5, _ri + stroke_width * 0.5, 0, 360, segments,
                             pr.Color(*stroke_color))

    def triangle(self, x1, y1, x2, y2, x3, y3, stroke_width=None, stroke_color: tuple = None,
                 filled_color: tuple = None):
        stroke_width = self.init_stroke_width(stroke_width)
        stroke_color = self.init_stroke_color(stroke_color)
        filled_color = self.init_filled_color(filled_color)
        if filled_color:
            pr.draw_triangle(pr.Vector2(x1, y1), pr.Vector2(x2, y2), pr.Vector2(x3, y3), pr.Color(*filled_color))
        if stroke_width and stroke_color:
            if stroke_width == 1:
                pr.draw_triangle_lines(pr.Vector2(x1, y1), pr.Vector2(x2, y2), pr.Vector2(x3, y3),
                                       pr.Color(*stroke_color))
            elif stroke_width > 1:
                pr.draw_line_ex(pr.Vector2(x1, y1), pr.Vector2(x2, y2), stroke_width, pr.Color(*stroke_color), )
                pr.draw_line_ex(pr.Vector2(x2, y2), pr.Vector2(x3, y3), stroke_width, pr.Color(*stroke_color), )
                pr.draw_line_ex(pr.Vector2(x3, y3), pr.Vector2(x1, y1), stroke_width, pr.Color(*stroke_color), )

    def poly(self, x, y, r, sides, r_angle=0, stroke_width=None, stroke_color: tuple = None,
             filled_color: tuple = None):
        stroke_width = self.init_stroke_width(stroke_width)
        stroke_color = self.init_stroke_color(stroke_color)
        filled_color = self.init_filled_color(filled_color)
        if filled_color:
            pr.draw_poly(pr.Vector2(x, y), sides, r, r_angle, pr.Color(*filled_color))
        if stroke_width and stroke_color:
            if stroke_width == 1:
                pr.draw_poly_lines(pr.Vector2(x, y), sides, r, r_angle, pr.Color(*stroke_color))
            elif stroke_width > 1:
                pr.draw_poly_lines_ex(pr.Vector2(x, y), sides, r, r_angle, stroke_width, pr.Color(*stroke_color))

