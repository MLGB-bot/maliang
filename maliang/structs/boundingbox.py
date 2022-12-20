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

