import pyray as pr
import maliang.structs.matrix as mod_matrix
import maliang.structs.texture as mod_texture

class MShader:
    def __init__(self):
        self.pr_shader = None

    def unload(self):
        pr.unload_shader(self.pr_shader)

    def get_location(self, uniform_name) -> int:
        return pr.get_shader_location(self.pr_shader, uniform_name)

    def get_location_attrib(self, attrib_name) -> int:
        return pr.get_shader_location_attrib(self.pr_shader, attrib_name)

    def set_value(self, loc_index: int, value, uniform_type: int, count: int=1):
        pr.set_shader_value_v(self.pr_shader, loc_index, value, uniform_type, count)

    def set_value_matrix(self, loc_index: int, matrix: mod_matrix.MMatrix):
        pr.set_shader_value_matrix(self.pr_shader, loc_index, matrix.pr_matrix)

    def set_value_texture(self, loc_index: int, texture: mod_texture.MTexture):
        pr.set_shader_value_texture(self.pr_shader, loc_index, texture.pr_texture)
