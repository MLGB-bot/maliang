import pyray as pr
from maliang.structs import MTexture
from maliang.shape_conf import ShapeConfig


class Shapes3d(ShapeConfig):
    def __init__(self):
        ShapeConfig().__init__()

    def point3d(self, x, y, z, stroke_color: tuple = None):
        stroke_color = self.init_stroke_color(stroke_color)
        pr.draw_point_3d(pr.Vector3(x, y, z), pr.Color(*stroke_color))

    def line3d(self, x1, y1, z1, x2, y2, z2, stroke_color: tuple = None):
        stroke_color = self.init_stroke_color(stroke_color)
        pr.draw_line_3d(pr.Vector3(x1, y1, z1), pr.Vector3(x2, y2, z2), pr.Color(*stroke_color))

    def circle3d(self, x, y, z, diam, rotation=(0, 0, 0), stroke_color: tuple = None):
        stroke_color = self.init_stroke_color(stroke_color)
        rotation_axis = pr.Vector3(*[1 if i else 0 for i in rotation])
        pr.draw_circle_3d(pr.Vector3(x, y, z), diam * 0.5, rotation_axis, rotation, pr.Color(*stroke_color))

    def triangle3d(self, x1, y1, z1, x2, y2, z2, x3, y3, z3, stroke_color: tuple = None):
        stroke_color = self.init_stroke_color(stroke_color)
        pr.draw_triangle_3d(pr.Vector3(x1, y1, z1), pr.Vector3(x2, y2, z2), pr.Vector3(x3, y3, z3),
                            pr.Color(*stroke_color))

    def traiangle_strip3d(self, points, stroke_color: tuple = None):
        stroke_color = self.init_stroke_color(stroke_color)
        pr.draw_triangle_strip_3d([pr.Vector3(*i) for i in points], len(points), pr.Color(*stroke_color))

    def cube(self, x, y, z, width, height, length, stroke_color: tuple = None,
             filled_color: tuple = None):
        filled_color = self.init_filled_color(filled_color)
        stroke_color = self.init_stroke_color(stroke_color)
        if filled_color:
            pr.draw_cube_v(pr.Vector3(x, y, z), pr.Vector3(width, height, length), pr.Color(*filled_color))
        if stroke_color:
            pr.draw_cube_wires_v(pr.Vector3(x, y, z), pr.Vector3(width, height, length), pr.Color(*stroke_color))

    def cube_texture(self, texture: MTexture, x, y, z, width, height, length, filled_color: tuple = None, source=None):
        filled_color = self.init_filled_color(filled_color)
        if not source:
            pr.draw_cube_texture(texture.pr_texture, pr.Vector3(x, y, z), width, height, length,
                                 pr.Color(*filled_color))
        else:
            pr.draw_cube_texture_rec(texture.pr_texture, pr.Rectangle(*source), pr.Vector3(x, y, z), width, height,
                                     length, pr.Color(*filled_color))

    def sphere(self, x, y, z, diam, rings=16, slices=16, stroke_color: tuple = None, filled_color=None,):
        filled_color = self.init_filled_color(filled_color)
        stroke_color = self.init_stroke_color(stroke_color)
        if filled_color:
            pr.draw_sphere_ex(pr.Vector3(x, y, z), diam*0.5, rings, slices, pr.Color(*filled_color))
        if stroke_color:
            pr.draw_sphere_wires(pr.Vector3(x, y, z), diam * 0.5, rings, slices, pr.Color(*filled_color))

    def cylinder(self, x, y, z, diam_top, diam_bottom, height, slices=16, stroke_color: tuple = None, filled_color=None):
        filled_color = self.init_filled_color(filled_color)
        stroke_color = self.init_stroke_color(stroke_color)
        if filled_color:
            pr.draw_cylinder(pr.Vector3(x, y, z), diam_top*0.5, diam_bottom*0.5, height, slices, pr.Color(*filled_color))
        if stroke_color:
            pr.draw_cylinder_wires(pr.Vector3(x, y, z), diam_top*0.5, diam_bottom*0.5, height, slices, pr.Color(*filled_color))

    def cylinder2(self, x1, y1, z1,  x2, y2, z2, diam1, diam2, sides, stroke_color: tuple = None, filled_color=None):
        filled_color = self.init_filled_color(filled_color)
        stroke_color = self.init_stroke_color(stroke_color)
        if filled_color:
            pr.draw_cylinder_ex(pr.Vector3(x1, y1, z1), pr.Vector3(x2, y2, z2), diam1*0.5, diam2*0.5, sides, pr.Color(*filled_color))
        if stroke_color:
            pr.draw_cylinder_wires_ex(pr.Vector3(x1, y1, z1), pr.Vector3(x2, y2, z2), diam1*0.5, diam2*0.5, sides, pr.Color(*filled_color))

    def plane(self, x, y, z, width, height, filled_color=None):
        # Draw a plane XZ
        filled_color = self.init_filled_color(filled_color)
        if filled_color:
            pr.draw_plane(pr.Vector3(x, y, z), pr.Vector2(width, height), pr.Color(*filled_color))

    def grid(self, slices=0, spacing=0.0):
        # Draw a grid (centered at (0, 0, 0))
        pr.draw_grid(slices, spacing)
