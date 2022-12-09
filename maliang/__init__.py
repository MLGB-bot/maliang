import pyray as pr

from maliang.window import Window
from maliang.units import ResourceLoader

class Maliang(Window):
    def __init__(self, width=100, height=100, title='', double_buffer=True, fps=None,
                 background_color=(235, 235, 235, 255), ):

        Window.__init__(self, width=width, height=height, title=title, fps=fps,
                 background_color=background_color, double_buffer=double_buffer)

    def set_static_relative_dir(self, relative_dir):
        return ResourceLoader.set_static_relative_dir(relative_dir)

    def set_static_absolute_dir(self, absolute_dir):
        return ResourceLoader.set_static_absolute_dir(absolute_dir)


    def run(self):
        self.loop()
