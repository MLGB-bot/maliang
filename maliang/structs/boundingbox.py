import pyray as pr
import maliang.structs.color as mod_color


class MBoundingBox:
    def __init__(self):
        self.pr_boundingbox = None

    @property
    def min(self):
        return (self.pr_boundingbox.min.x, self.pr_boundingbox.min.y, self.pr_boundingbox.min.z)

    @property
    def max(self):
        return (self.pr_boundingbox.max.x, self.pr_boundingbox.max.y, self.pr_boundingbox.max.z)

    @min.setter
    def min(self, value):
        self.pr_boundingbox.min = pr.Vector3(*value)

    @max.setter
    def max(self, value):
        self.pr_boundingbox.max = pr.Vector3(*value)

    def draw(self, color: mod_color.MColor=mod_color.MColor(0,0,0)):
        pr.draw_bounding_box(self.pr_boundingbox, color.to_pyray())

    def init_from_cube(self, x, y, z, size_x, size_y, size_z):
        min = pr.Vector3(
            x - size_x * 0.5,
            y - size_y * 0.5,
            z - size_z * 0.5,
        )
        max = pr.Vector3(
            x + size_x * 0.5,
            y + size_y * 0.5,
            z + size_z * 0.5,
        )
        self.pr_boundingbox = pr.BoundingBox(min, max)
