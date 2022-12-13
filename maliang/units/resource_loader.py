import os
import pyray as pr


class ResourceLoader:
    static_dir = os.path.join(os.getcwd(), "resources")

    loaded_fonts_runtime = []
    loaded_texture_runtime = []
    loaded_images = []

    def __init__(self):
        pass

    @classmethod
    def set_static_relative_dir(cls, relative_dir):
        cls.static_dir = os.path.join(os.getcwd(), relative_dir)

    @classmethod
    def set_static_absolute_dir(cls, absolute_dir):
        cls.static_dir = absolute_dir

    @classmethod
    def task_unload_fonts_runtime(cls):
        # print("lenL1", len(cls.loaded_fonts_runtime), len(cls.loaded_texture_runtime))
        while cls.loaded_fonts_runtime:
            font = cls.loaded_fonts_runtime.pop()
            pr.unload_font(font)
        while cls.loaded_texture_runtime:
            texture = cls.loaded_texture_runtime.pop()
            pr.unload_texture(texture)
        # print("lenL2", len(cls.loaded_fonts_runtime), len(cls.loaded_texture_runtime))
