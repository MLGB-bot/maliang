import os
import pyray as pr
from maliang.units import ResourceLoader, ImageMode
from maliang.structs import MColor, MShader


class Shader():
    def __init__(self):
        pass

    def load_shader(self, vs_filename, fs_filename) -> MShader:
        vs_file = os.path.join(ResourceLoader.static_dir, vs_filename)
        fs_file = os.path.join(ResourceLoader.static_dir, fs_filename)
        shader = MShader()
        shader.pr_shader = pr.load_shader(vs_file, fs_file)
        return shader

    def load_shader_from_memory(self, vs_code, fs_code):
        shader = MShader()
        shader.pr_shader = pr.load_shader_from_memory(vs_code, fs_code)
        return shader

    def rl_version(self):
        return pr.rl_get_version()

