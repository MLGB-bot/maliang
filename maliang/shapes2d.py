import pyray as pr
from maliang.units import RectMode, EllipseMode, CircleMode, f2i
from maliang.shape_conf import ShapeConfig
from raylib._raylib_cffi import ffi


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
                pr.draw_pixel(x, y, pr.Color(*stroke_color))
        elif stroke_color:
            pr.draw_pixel(x, y, pr.Color(*stroke_color))

    def line(self, x1, y1, x2, y2, stroke_width=None, stroke_color: tuple = None):
        stroke_width = self.init_stroke_width(stroke_width)
        stroke_color = self.init_stroke_color(stroke_color)
        if stroke_width and stroke_color:
            pr.draw_line_ex(
                pr.Vector2(f2i(x1), f2i(y1)),
                pr.Vector2(f2i(x2), f2i(y2)),
                stroke_width,
                pr.Color(*stroke_color),
            )
        elif stroke_color:
            pr.draw_line(f2i(x1), f2i(y1), f2i(x2), f2i(y2), pr.Color(*stroke_color), )

    @staticmethod
    def _init_rect_mode(x, y, w, h, rect_mode):
        if rect_mode == RectMode.CORNER:
            return f2i(x), f2i(y), f2i(w), f2i(h)
        elif rect_mode == RectMode.CENTER:
            return f2i(x - w * 0.5), f2i(y - h * 0.5), f2i(w), f2i(h)
        elif rect_mode == RectMode.RADIUS:
            return f2i(x - w), f2i(y - h), f2i(2 * w), f2i(2 * h)
        elif rect_mode == RectMode.CORNERS:
            return f2i(min(x, w)), f2i(min(y, h)), f2i(abs(x - w)), f2i(abs(y - h))
        else:
            return f2i(x), f2i(y), f2i(w), f2i(h)

    def rect(self, x, y, w, h, stroke_width=None, stroke_color: tuple = None, filled_color: tuple = None, mode=None):
        stroke_width = self.init_stroke_width(stroke_width)
        stroke_color = self.init_stroke_color(stroke_color)
        filled_color = self.init_filled_color(filled_color)

        mode = mode or self._rect_mode
        _x, _y, _w, _h = self._init_rect_mode(x, y, w, h, mode)
        if filled_color:
            pr.draw_rectangle(_x, _y, _w, _h, pr.Color(*filled_color))
        if stroke_width and stroke_color:
            if stroke_width == 1:
                pr.draw_rectangle_lines(_x, _y, _w, _h, pr.Color(*stroke_color))
            else:
                pr.draw_rectangle_lines_ex(pr.Rectangle(_x, _y, _w, _h), stroke_width, pr.Color(*stroke_color))

    @staticmethod
    def _init_circle_mode(x, y, diam, rect_mode):
        if rect_mode == CircleMode.CORNER:
            return f2i(x + diam * 0.5), f2i(y + diam * 0.5), diam * 0.5
        elif rect_mode == CircleMode.CENTER:
            return f2i(x), f2i(y), diam*0.5
        elif rect_mode == CircleMode.RADIUS:
            return f2i(x), f2i(y), diam
        else:
            return f2i(x), f2i(y), diam*0.5


    def circle(self, x, y, diam, stroke_width=None, stroke_color: tuple = None, filled_color: tuple = None, segments=30,
               mode=None):
        stroke_width = self.init_stroke_width(stroke_width)
        stroke_color = self.init_stroke_color(stroke_color)
        filled_color = self.init_filled_color(filled_color)
        mode = mode or self._circle_mode
        _x, _y, _r = self._init_circle_mode(x, y, diam, mode)

        if filled_color:
            pr.draw_circle(_x, _y, _r, pr.Color(*filled_color))
        if stroke_width and stroke_color:
            if stroke_width == 1:
                pr.draw_circle_lines(_x, _y, _r, pr.Color(*stroke_color))
            elif stroke_width > 1:
                pr.draw_ring(pr.Vector2(_x, _y), _r - stroke_width * 0.5, _r + stroke_width * 0.5, 0, 360, segments,
                             pr.Color(*stroke_color))

    @staticmethod
    def _init_ellipse_mode(x, y, w, h, rect_mode):
        if rect_mode == EllipseMode.CORNER:
            return f2i(x + w * 0.5), f2i(y + h * 0.5), w * 0.5, h * 0.5
        elif rect_mode == EllipseMode.CENTER:
            return f2i(x), f2i(y), w * 0.5, h * 0.5
        elif rect_mode == EllipseMode.RADIUS:
            return f2i(x), f2i(y), w, h
        elif rect_mode == EllipseMode.CORNERS:
            return f2i(0.5 * (x + w)), f2i(0.5 * (y + h)), abs(x - w) * 0.5, abs(y - h) * 0.5
        else:
            return f2i(x), f2i(y), w * 0.5, h * 0.5

    def ellipse(self, x, y, w, h, stroke_width=None, stroke_color: tuple = None, filled_color: tuple = None, mode=None):
        stroke_width = self.init_stroke_width(stroke_width)
        stroke_color = self.init_stroke_color(stroke_color)
        filled_color = self.init_filled_color(filled_color)
        mode = mode or self._ellipse_mode
        _x, _y, _w, _h = self._init_ellipse_mode(x, y, w, h, mode)

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

    @staticmethod
    def init_ring_mode(x, y, d1, d2, rect_mode):
        if rect_mode == CircleMode.CORNER:
            dm = max(d1, d2)
            return f2i(x + dm * 0.5), f2i(y + dm * 0.5), d1 * 0.5, d2 * 0.5
        elif rect_mode == CircleMode.CENTER:
            return f2i(x), f2i(y), d1 * 0.5, d2 * 0.5
        elif rect_mode == CircleMode.RADIUS:
            return f2i(x), f2i(y), d1, d2
        else:
            return f2i(x), f2i(y), d1 * 0.5, d2 * 0.5

    def ring(self, x, y, d_in, d_out, stroke_width=None, stroke_color: tuple = None, filled_color: tuple = None,
             segments=30, mode=None):
        stroke_width = self.init_stroke_width(stroke_width)
        stroke_color = self.init_stroke_color(stroke_color)
        filled_color = self.init_filled_color(filled_color)

        mode = mode or self._circle_mode
        _x, _y, _ri, _ro = self.init_ring_mode(x, y, d_in, d_out, mode)

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

    # collision detection functions
    # 碰撞检测
    def check_collision_recs(self, x1, y1, w1, h1, x2, y2, w2, h2, mode=None) -> bool:
        mode = mode or self._rect_mode
        _x1, _y1, _w1, _h1 = self._init_rect_mode(x1, y1, w1, h1, mode)
        _x2, _y2, _w2, _h2 = self._init_rect_mode(x2, y2, w2, h2, mode)
        return pr.check_collision_recs(
            pr.Rectangle(_x1, _y1, _w1, _h1),
            pr.Rectangle(_x2, _y2, _w2, _h2),
        )

    def check_collision_circles(self, x1, y1, diam1, x2, y2, diam2, mode=None) -> bool:
        mode = mode or self._circle_mode
        _x1, _y1, _r1 = self._init_circle_mode(x1, y1, diam1, mode)
        _x2, _y2, _r2 = self._init_circle_mode(x2, y2, diam2, mode)
        return pr.check_collision_circles(
            pr.Vector2(_x1, _y1), _r1,
            pr.Vector2(_x2, _y2), _r2,
        )

    def check_collision_circle_rec(self, circle_x, circle_y, circle_diam, rec_x, rec_y, rec_w, rec_h,
                                         circle_mode=None, rec_mode=None) -> bool:
        rec_mode = rec_mode or self._rect_mode
        _x1, _y1, _w1, _h1 = self._init_rect_mode(rec_x, rec_y, rec_w, rec_h, rec_mode)
        circle_mode = circle_mode or self._circle_mode
        _x2, _y2, _r2 = self._init_circle_mode(circle_x, circle_y, circle_diam, circle_mode)
        return pr.check_collision_circle_rec(
            pr.Vector2(_x2, _y2), _r2,
            pr.Rectangle(_x1, _y1, _w1, _h1)
        )

    def check_collision_point_rec(self, point_x, point_y, rec_x, rec_y, rec_w, rec_h, rec_mode=None) -> bool:
        rec_mode = rec_mode or self._rect_mode
        _x1, _y1, _w1, _h1 = self._init_rect_mode(rec_x, rec_y, rec_w, rec_h, rec_mode)
        return pr.check_collision_point_rec(
            pr.Vector2(point_x, point_y),
            pr.Rectangle(_x1, _y1, _w1, _h1)
        )

    def check_collision_point_circle(self, point_x, point_y, circle_x, circle_y, circle_diam, circle_mode=None) -> bool:
        circle_mode = circle_mode or self._circle_mode
        _x1, _y1, _r1 = self._init_circle_mode(circle_x, circle_y, circle_diam, circle_mode)
        return pr.check_collision_point_circle(
            pr.Vector2(point_x, point_y),
            pr.Vector2(_x1, _y1), _r1
        )

    def check_collision_point_triangle(self, point_x, point_y, x1, y1, x2, y2, x3, y3) -> bool:
        return pr.check_collision_point_triangle(
            pr.Vector2(point_x, point_y),
            pr.Vector2(x1, y1),
            pr.Vector2(x2, y2),
            pr.Vector2(x3, y3),
        )

    def check_collision_lines(self, line1_point1, line1_point2, line2_point1, line2_point2,):
        collision_point = ffi.new("struct Vector2 *")
        result = pr.check_collision_lines(
            pr.Vector2(*line1_point1),
            pr.Vector2(*line1_point2),
            pr.Vector2(*line2_point1),
            pr.Vector2(*line2_point2),
            collision_point
        )
        if result:
            return collision_point.x, collision_point.y
        else:
            return None

    def check_collision_point_line(self, point_x, point_y, x1, y1, x2, y2, threadhold=1):
        return pr.check_collision_point_line(
            pr.Vector2(point_x, point_y),
            pr.Vector2(x1, y1),
            pr.Vector2(x2, y2),
            threadhold,
        )

    def _rev_rect_mode(self, x, y, w, h, rect_mode):
        if rect_mode == RectMode.CORNER:
            return f2i(x), f2i(y), f2i(w), f2i(h)
        elif rect_mode == RectMode.CENTER:
            return int(x + w * 0.5), int(y + h * 0.5), f2i(w), f2i(h)
        elif rect_mode == RectMode.RADIUS:
            return int(x + w * 0.5), int(y + h * 0.5), f2i(0.5 * w), f2i(0.5 * h)
        elif rect_mode == RectMode.CORNERS:
            return f2i(x), f2i(y), f2i(abs(x + w)), f2i(abs(y + h))
        else:
            return f2i(x), f2i(y), f2i(w), f2i(h)

    def get_collision_rec(self, x1, y1, w1, h1, x2, y2, w2, h2, mode=None):
        mode = mode or self._rect_mode
        _x1, _y1, _w1, _h1 = self._init_rect_mode(x1, y1, w1, h1, mode)
        _x2, _y2, _w2, _h2 = self._init_rect_mode(x2, y2, w2, h2, mode)
        rect = pr.get_collision_rec(
            pr.Rectangle(_x1, _y1, _w1, _h1),
            pr.Rectangle(_x2, _y2, _w2, _h2),
        )
        return self._rev_rect_mode(rect.x, rect.y, rect.width, rect.height, mode)