import pyray as pr
import maliang.structs.color as mod_color
import maliang.structs.boundingbox as mod_boundingbox


class MModel:
    def __init__(self):
        self.pr_model = None

    def draw(self, x, y, z, scale=1, stroke_color: mod_color.MColor = None, filled_color=mod_color.MColor(*pr.WHITE)):
        if filled_color:
            pr.draw_model(self.pr_model, pr.Vector3(x, y, z), scale, filled_color.to_pyray())
        if stroke_color:
            pr.draw_model_wires(self.pr_model, pr.Vector3(x, y, z), scale, stroke_color.to_pyray())

    def draw2(self, x, y, z, scale=(1, 1, 1), rotation_axis=(0, 0, 0), rotation_angle=0,
              stroke_color: mod_color.MColor = None, filled_color=mod_color.MColor(*pr.WHITE)):
        if filled_color:
            pr.draw_model_ex(self.pr_model, pr.Vector3(x, y, z), pr.Vector3(*rotation_axis), rotation_angle,
                             pr.Vector3(*scale), filled_color.to_pyray())
        if stroke_color:
            pr.draw_model_wires_ex(self.pr_model, pr.Vector3(x, y, z), pr.Vector3(*rotation_axis), rotation_angle,
                                   pr.Vector3(*scale), stroke_color.to_pyray())

    def get_bounding_box(self):
        boundingbox = mod_boundingbox.MBoundingBox()
        boundingbox.pr_boundingbox = pr.get_model_bounding_box(self.pr_model)
        return boundingbox

