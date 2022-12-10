import os
import pyray as pr

class ResourceLoader:
    static_dir = os.path.join(os.getcwd(), "resources")

    loaded_fonts_runtime = []
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
    def unload_font(cls, font):
        pr.unload_font(font)

    @classmethod
    def task_unload_fonts_runtime(cls):
        while cls.loaded_fonts_runtime:
            font = cls.loaded_fonts_runtime.pop()
            cls.unload_font(font)