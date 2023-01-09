import pyray as pr
from maliang.structs import MTexture, MBoundingBox
from maliang.shape_conf import ShapeConfig


class Shapes3d(ShapeConfig):
    def __init__(self):
        ShapeConfig().__init__()

    def point3d(self, x, y, z, **kwargs):
        stroke_color = self.init_stroke_color(kwargs)
        if stroke_color:
            pr.draw_point_3d(pr.Vector3(x, y, z), pr.Color(*stroke_color))

    def line3d(self, x1, y1, z1, x2, y2, z2, **kwargs):
        stroke_color = self.init_stroke_color(kwargs)
        if stroke_color:
            pr.draw_line_3d(pr.Vector3(x1, y1, z1), pr.Vector3(x2, y2, z2), pr.Color(*stroke_color))

    def circle3d(self, x, y, z, diam, rotation_axis=(0, 0, 0), rotation_angle=0.0, **kwargs):
        stroke_color = self.init_stroke_color(kwargs)
        if stroke_color:
            pr.draw_circle_3d(pr.Vector3(x, y, z), diam * 0.5, rotation_axis, rotation_angle, pr.Color(*stroke_color))

    def triangle3d(self, x1, y1, z1, x2, y2, z2, x3, y3, z3, **kwargs):
        stroke_color = self.init_stroke_color(kwargs)
        if stroke_color:
            pr.draw_triangle_3d(pr.Vector3(x1, y1, z1), pr.Vector3(x2, y2, z2), pr.Vector3(x3, y3, z3),
                            pr.Color(*stroke_color))

    def traiangle_strip3d(self, points, **kwargs):
        stroke_color = self.init_stroke_color(kwargs)
        if stroke_color:
            pr.draw_triangle_strip_3d([pr.Vector3(*i) for i in points], len(points), pr.Color(*stroke_color))

    def cube(self, x, y, z, size_x, size_y, size_z, **kwargs):
        filled_color = self.init_filled_color(kwargs)
        stroke_color = self.init_stroke_color(kwargs)
        if filled_color:
            pr.draw_cube_v(pr.Vector3(x, y, z), pr.Vector3(size_x, size_y, size_z), pr.Color(*filled_color))
        if stroke_color:
            pr.draw_cube_wires_v(pr.Vector3(x, y, z), pr.Vector3(size_x, size_y, size_z), pr.Color(*stroke_color))

    def cube_texture(self, texture: MTexture, x, y, z, size_x, size_y, size_z, source=None, **kwargs):
        filled_color = self.init_filled_color(kwargs)
        if filled_color:
            if not source:
                pr.draw_cube_texture(texture.pr_texture, pr.Vector3(x, y, z), size_x, size_y, size_z,
                                     pr.Color(*filled_color))
            else:
                pr.draw_cube_texture_rec(texture.pr_texture, pr.Rectangle(*source), pr.Vector3(x, y, z),
                                     size_x, size_y, size_z, pr.Color(*filled_color))

    def sphere(self, x, y, z, diam, rings=16, slices=16, **kwargs):
        filled_color = self.init_filled_color(kwargs)
        stroke_color = self.init_stroke_color(kwargs)
        if filled_color:
            pr.draw_sphere_ex(pr.Vector3(x, y, z), diam, rings, slices, pr.Color(*filled_color))
        if stroke_color:
            pr.draw_sphere_wires(pr.Vector3(x, y, z), diam, rings, slices, pr.Color(*stroke_color))

    def cylinder(self, x, y, z, diam_top, diam_bottom, height, slices=16, **kwargs):
        filled_color = self.init_filled_color(kwargs)
        stroke_color = self.init_stroke_color(kwargs)
        if filled_color:
            pr.draw_cylinder(pr.Vector3(x, y, z), diam_top*0.5, diam_bottom*0.5, height, slices, pr.Color(*filled_color))
        if stroke_color:
            pr.draw_cylinder_wires(pr.Vector3(x, y, z), diam_top*0.5, diam_bottom*0.5, height, slices, pr.Color(*filled_color))

    def cylinder2(self, x1, y1, z1,  x2, y2, z2, diam1, diam2, sides, **kwargs):
        filled_color = self.init_filled_color(kwargs)
        stroke_color = self.init_stroke_color(kwargs)
        if filled_color:
            pr.draw_cylinder_ex(pr.Vector3(x1, y1, z1), pr.Vector3(x2, y2, z2), diam1*0.5, diam2*0.5, sides, pr.Color(*filled_color))
        if stroke_color:
            pr.draw_cylinder_wires_ex(pr.Vector3(x1, y1, z1), pr.Vector3(x2, y2, z2), diam1*0.5, diam2*0.5, sides, pr.Color(*filled_color))

    def plane(self, x, y, z, width, height, **kwargs):
        # Draw a plane XZ
        filled_color = self.init_filled_color(kwargs)
        if filled_color:
            pr.draw_plane(pr.Vector3(x, y, z), pr.Vector2(width, height), pr.Color(*filled_color))

    def grid(self, slices=0, spacing=0.0):
        # Draw a grid (centered at (0, 0, 0))
        pr.draw_grid(slices, spacing)

    # collision detection functions
    # 碰撞检测
    def check_collision_spheres(self, x1, y1, z1, diam1, x2, y2, z2, diam2, ) -> bool:
        return pr.check_collision_spheres(
            pr.Vector3(x1, y1, z1), diam1 * 0.5,
            pr.Vector3(x2, y2, z2), diam2 * 0.5,
        )

    def check_collision_boxes(self, box1: MBoundingBox, box2: MBoundingBox ) -> bool:
        return pr.check_collision_boxes(
            box1.pr_boundingbox,
            box2.pr_boundingbox,
        )

    def check_collision_box_sphere(self, box: MBoundingBox, sphere_axis, sphere_diam) -> bool:
        return pr.check_collision_box_sphere(
            box.pr_boundingbox,
            pr.Vector3(*sphere_axis),
            sphere_diam
        )

