import pyray as pr
from maliang.units import RectMode, EllipseMode, CircleMode, f2i
from maliang.shape_conf import ShapeConfig
from raylib._raylib_cffi import ffi
import raylib as rl

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


    def point(self, x, y, shape="circle", **kwargs):
        stroke_width = self.init_stroke_width(kwargs)
        stroke_color = self.init_stroke_color(kwargs)
        if stroke_width and stroke_color:
            if stroke_width == 1:
                # 画一个像素
                rl.DrawPixelV(pr.Vector2(x, y), stroke_color.to_pyray())
            elif stroke_width > 1:
                # 画一个圆
                if shape == "circle":
                    self.circle(x, y, diam=stroke_width, stroke_width=0,
                         stroke_color=None, filled_color=stroke_color, mode=CircleMode.CENTER)
                elif shape == 'rect':
                    self.rect(x, y, stroke_width, stroke_width, stroke_width=0,
                         stroke_color=None, filled_color=stroke_color, mode=RectMode.CENTER)


    def line(self, x1, y1, x2, y2, **kwargs):
        stroke_width = self.init_stroke_width(kwargs)
        stroke_color = self.init_stroke_color(kwargs)
        if stroke_width and stroke_color:
            if stroke_width == 1:
                rl.DrawLineV(pr.Vector2(x1, y1), pr.Vector2(x2, y2), stroke_color.to_pyray())
            elif stroke_width > 1:
                rl.DrawLineEx(
                    pr.Vector2(x1, y1),
                    pr.Vector2(x2, y2),
                    stroke_width,
                    stroke_color.to_pyray(),
                )


    def line_bezier(self, x1, y1, x2, y2, **kwargs):
        stroke_width = self.init_stroke_width(kwargs)
        stroke_color = self.init_stroke_color(kwargs)
        if stroke_width and stroke_color:
            rl.DrawLineBezier(
                pr.Vector2(x1, y1),
                pr.Vector2(x2, y2),
                stroke_width,
                stroke_color.to_pyray()
            )


    def line_bezier_quad(self, x1, y1, x2, y2, cx, cy, **kwargs):
        stroke_width = self.init_stroke_width(kwargs)
        stroke_color = self.init_stroke_color(kwargs)
        if stroke_width and stroke_color:
            rl.DrawLineBezierQuad(
                pr.Vector2(x1, y1),
                pr.Vector2(x2, y2),
                pr.Vector2(cx, cy),
                stroke_width,
                stroke_color.to_pyray()
            )


    def line_bezier_cubic(self, x1, y1, x2, y2, cx1, cy1, cx2, cy2, **kwargs):
        stroke_width = self.init_stroke_width(kwargs)
        stroke_color = self.init_stroke_color(kwargs)
        if stroke_width and stroke_color:
            rl.DrawLineBezierCubic(
                pr.Vector2(x1, y1),
                pr.Vector2(x2, y2),
                pr.Vector2(cx1, cy1),
                pr.Vector2(cx2, cy2),
                stroke_width,
                stroke_color.to_pyray()
            )


    @staticmethod
    def _init_rect_mode(x, y, w, h, rect_mode):
        if rect_mode == RectMode.CORNER:
            return x, y, w, h
        elif rect_mode == RectMode.CENTER:
            return x - w * 0.5, y - h * 0.5, w, h
        elif rect_mode == RectMode.RADIUS:
            return x - w, y - h, 2 * w, 2 * h
        elif rect_mode == RectMode.CORNERS:
            return min(x, w), min(y, h), abs(x - w), abs(y - h)
        else:
            return x, y, w, h

    def rect(self, x, y, w, h, mode=None, **kwargs):
        stroke_width = self.init_stroke_width(kwargs)
        stroke_color = self.init_stroke_color(kwargs)
        filled_color = self.init_filled_color(kwargs)

        mode = mode or self._rect_mode
        _x, _y, _w, _h = self._init_rect_mode(x, y, w, h, mode)
        if filled_color:
            rl.DrawRectangleRec(pr.Rectangle(_x, _y, _w, _h), filled_color.to_pyray())
        if stroke_width and stroke_color:
            if stroke_width == 1:
                rl.DrawRectangleLines(f2i(_x), f2i(_y), f2i(_w), f2i(_h), stroke_color.to_pyray())
            else:
                rl.DrawRectangleLinesEx(pr.Rectangle(_x, _y, _w, _h), stroke_width, stroke_color.to_pyray())

    def rect_rounded(self, x, y, w, h, roundness:float=0, segments=30, mode=None, **kwargs):
        stroke_width = self.init_stroke_width(kwargs)
        stroke_color = self.init_stroke_color(kwargs)
        filled_color = self.init_filled_color(kwargs)

        mode = mode or self._rect_mode
        _x, _y, _w, _h = self._init_rect_mode(x, y, w, h, mode)
        if filled_color:
            rl.DrawRectangleRounded(pr.Rectangle(_x, _y, _w, _h), roundness, segments, filled_color.to_pyray())
        if stroke_width and stroke_color:
            rl.DrawRectangleRoundedLines(pr.Rectangle(_x, _y, _w, _h), roundness, segments, stroke_width, stroke_color.to_pyray())

    def rect_gradient(self, x, y, w, h, colors=None, direction="xy", mode=None):
        mode = mode or self._rect_mode
        _x, _y, _w, _h = self._init_rect_mode(x, y, w, h, mode)
        if direction == 'xy':
            rl.DrawRectangleGradientEx(pr.Rectangle(_x, _y, _w, _h), *[self.format_color(color).to_pyray() for color in colors])
        elif direction == 'x':
            rl.DrawRectangleGradientH(f2i(_x), f2i(_y), f2i(_w), f2i(_h), *[self.format_color(color).to_pyray() for color in colors])
        elif direction == 'y':
            rl.DrawRectangleGradientV(f2i(_x), f2i(_y), f2i(_w), f2i(_h), *[self.format_color(color).to_pyray() for color in colors])

    @staticmethod
    def _init_circle_mode(x, y, diam, rect_mode):
        if rect_mode == CircleMode.CORNER:
            return x + diam * 0.5, y + diam * 0.5, diam * 0.5
        elif rect_mode == CircleMode.CENTER:
            return x, y, diam*0.5
        elif rect_mode == CircleMode.RADIUS:
            return x, y, diam
        else:
            return x, y, diam*0.5


    def circle(self, x, y, diam, segments=30, mode=None, **kwargs):
        stroke_width = self.init_stroke_width(kwargs)
        stroke_color = self.init_stroke_color(kwargs)
        filled_color = self.init_filled_color(kwargs)
        mode = mode or self._circle_mode
        _x, _y, _r = self._init_circle_mode(x, y, diam, mode)

        if filled_color:
            rl.DrawCircleV(pr.Vector2(_x, _y), _r, filled_color.to_pyray())
        if stroke_width and stroke_color:
            if stroke_width == 1:
                rl.DrawCircleLines(f2i(_x), f2i(_y), _r, stroke_color.to_pyray())
            elif stroke_width > 1:
                pr.draw_ring(pr.Vector2(_x, _y), _r - stroke_width * 0.5, _r + stroke_width * 0.5, 0, 360, segments,
                             stroke_color.to_pyray())

    def circle_gradient(self, x, y, diam, colors, mode=None):
        mode = mode or self._circle_mode
        _x, _y, _r = self._init_circle_mode(x, y, diam, mode)
        rl.DrawCircleGradient(_x, _y, _r, *[self.format_color(color).to_pyray() for color in colors])

    @staticmethod
    def _init_ellipse_mode(x, y, w, h, rect_mode):
        if rect_mode == EllipseMode.CORNER:
            return (x + w * 0.5), (y + h * 0.5), w * 0.5, h * 0.5
        elif rect_mode == EllipseMode.CENTER:
            return (x), (y), w * 0.5, h * 0.5
        elif rect_mode == EllipseMode.RADIUS:
            return (x), (y), w, h
        elif rect_mode == EllipseMode.CORNERS:
            return (0.5 * (x + w)), (0.5 * (y + h)), abs(x - w) * 0.5, abs(y - h) * 0.5
        else:
            return (x), (y), w * 0.5, h * 0.5

    def ellipse(self, x, y, w, h, mode=None, **kwargs):
        stroke_width = self.init_stroke_width(kwargs)
        stroke_color = self.init_stroke_color(kwargs)
        filled_color = self.init_filled_color(kwargs)
        mode = mode or self._ellipse_mode
        _x, _y, rw, rh = self._init_ellipse_mode(x, y, w, h, mode)
        _x = f2i(_x)
        _y = f2i(_y)
        if filled_color:
            rl.DrawEllipse(_x, _y, rw, rh, filled_color.to_pyray())
        if stroke_width and stroke_color:
            if stroke_width == 1:
                rl.DrawEllipseLines(_x, _y, rw, rh, stroke_color.to_pyray())
            elif stroke_width > 1:
                self.draw_ellipse_lines_py(_x, _y, rw, rh, stroke_width, tuple(stroke_color))

    def arc(self, x, y, w, h, start_angle, end_angle, segments=30, shape=1, mode=None, **kwargs):
        stroke_width = self.init_stroke_width(kwargs)
        stroke_color = self.init_stroke_color(kwargs)
        filled_color = self.init_filled_color(kwargs)
        mode = mode or self._ellipse_mode
        _x, _y, rw, rh = self._init_ellipse_mode(x, y, w, h, mode)
        self.draw_arc_py(_x, _y, rw, rh, start_angle, end_angle, segments=segments, shape=shape,
                                stroke_width=stroke_width,
                                stroke_color=tuple(stroke_color) if stroke_color else None,
                                filled_color=tuple(filled_color) if filled_color else None)

    @staticmethod
    def init_ring_mode(x, y, d1, d2, rect_mode):
        if rect_mode == CircleMode.CORNER:
            dm = max(d1, d2)
            return (x + dm * 0.5), (y + dm * 0.5), d1 * 0.5, d2 * 0.5
        elif rect_mode == CircleMode.CENTER:
            return (x), (y), d1 * 0.5, d2 * 0.5
        elif rect_mode == CircleMode.RADIUS:
            return (x), (y), d1, d2
        else:
            return (x), (y), d1 * 0.5, d2 * 0.5

    def ring(self, x, y, d_in, d_out, start_angle=0, end_angle=360, segments=30, mode=None, **kwargs):
        stroke_width = self.init_stroke_width(kwargs)
        stroke_color = self.init_stroke_color(kwargs)
        filled_color = self.init_filled_color(kwargs)

        mode = mode or self._circle_mode
        _x, _y, _ri, _ro = self.init_ring_mode(x, y, d_in, d_out, mode)
        _start, _end = self.maliang_coor_degree_to_raylib(start_angle, end_angle)
        if filled_color:
            rl.DrawRing(pr.Vector2(_x, _y), _ri, _ro, _start, _end, segments, filled_color.to_pyray())
        if stroke_width and stroke_color:
            if stroke_width == 1:
                rl.DrawRingLines(pr.Vector2(_x, _y), _ri, _ro, _start, _end, segments, stroke_color.to_pyray())
            elif stroke_width > 1:
                rl.DrawRing(pr.Vector2(_x, _y), _ri - stroke_width * 0.5, _ri + stroke_width * 0.5, _start, _end, segments,
                             stroke_color.to_pyray())
                rl.DrawRing(pr.Vector2(_x, _y), _ro - stroke_width * 0.5, _ro + stroke_width * 0.5, _start, _end, segments,
                             stroke_color.to_pyray())
                # draw lines
                if (end_angle - start_angle) % 360:
                    rl.DrawLineEx(
                        pr.Vector2(*self.circle_coor_by_degree(_x, _y, _ri, start_angle)),
                        pr.Vector2(*self.circle_coor_by_degree(_x, _y, _ro, start_angle)),
                        stroke_width,
                        stroke_color.to_pyray(),
                    )
                    rl.DrawLineEx(
                        pr.Vector2(*self.circle_coor_by_degree(_x, _y, _ri, end_angle)),
                        pr.Vector2(*self.circle_coor_by_degree(_x, _y, _ro, end_angle)),
                        stroke_width,
                        stroke_color.to_pyray(),
                    )


    def triangle(self, x1, y1, x2, y2, x3, y3, **kwargs):
        stroke_width = self.init_stroke_width(kwargs)
        stroke_color = self.init_stroke_color(kwargs)
        filled_color = self.init_filled_color(kwargs)

        area = self.calc_polygon_area((
            (x1, y1), (x2, y2), (x3, y3)
        ))
        if area > 0:
            # 顺时针 -> 逆时针
            x2, x3 = x3, x2
            y2, y3 = y3, y2

        if filled_color:
            rl.DrawTriangle(pr.Vector2(x1, y1), pr.Vector2(x2, y2), pr.Vector2(x3, y3), filled_color.to_pyray())
        if stroke_width and stroke_color:
            if stroke_width == 1:
                rl.DrawTriangleLines(pr.Vector2(x1, y1), pr.Vector2(x2, y2), pr.Vector2(x3, y3),
                                       stroke_color.to_pyray())
            elif stroke_width > 1:
                rl.DrawLineEx(pr.Vector2(x1, y1), pr.Vector2(x2, y2), stroke_width, stroke_color.to_pyray(), )
                rl.DrawLineEx(pr.Vector2(x2, y2), pr.Vector2(x3, y3), stroke_width, stroke_color.to_pyray(), )
                rl.DrawLineEx(pr.Vector2(x3, y3), pr.Vector2(x1, y1), stroke_width, stroke_color.to_pyray(), )

    def poly(self, x, y, r, sides, rotation=0, **kwargs):
        stroke_width = self.init_stroke_width(kwargs)
        stroke_color = self.init_stroke_color(kwargs)
        filled_color = self.init_filled_color(kwargs)
        if filled_color:
            pr.draw_poly(pr.Vector2(x, y), sides, r, rotation, filled_color.to_pyray())
        if stroke_width and stroke_color:
            if stroke_width == 1:
                pr.draw_poly_lines(pr.Vector2(x, y), sides, r, rotation, stroke_color.to_pyray())
            elif stroke_width > 1:
                pr.draw_poly_lines_ex(pr.Vector2(x, y), sides, r, rotation, stroke_width, stroke_color.to_pyray())

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
            return (x), (y), (w), (h)
        elif rect_mode == RectMode.CENTER:
            return (x + w * 0.5), (y + h * 0.5), (w), (h)
        elif rect_mode == RectMode.RADIUS:
            return (x + w * 0.5), (y + h * 0.5), (0.5 * w), (0.5 * h)
        elif rect_mode == RectMode.CORNERS:
            return (x), (y), (abs(x + w)), (abs(y + h))
        else:
            return (x), (y), (w), (h)

    def get_collision_rec(self, x1, y1, w1, h1, x2, y2, w2, h2, mode=None):
        mode = mode or self._rect_mode
        _x1, _y1, _w1, _h1 = self._init_rect_mode(x1, y1, w1, h1, mode)
        _x2, _y2, _w2, _h2 = self._init_rect_mode(x2, y2, w2, h2, mode)
        rect = pr.get_collision_rec(
            pr.Rectangle(_x1, _y1, _w1, _h1),
            pr.Rectangle(_x2, _y2, _w2, _h2),
        )
        return self._rev_rect_mode(rect.x, rect.y, rect.width, rect.height, mode)