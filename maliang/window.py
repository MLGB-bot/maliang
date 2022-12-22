import pyray as pr
from maliang.structs import MColor


class Window():
    def __init__(self, width=100, height=100, title='',
                 background_color=(235, 235, 235, 255)):
        self.width = width
        self.height = height
        self.background_color = tuple(MColor(*background_color))
        self.title = title
        self.init_window()
        while not pr.is_window_ready():
            pass

    def init_window(self):
        return pr.init_window(self.width, self.height, self.title)

    def background(self, *color):
        color = MColor(*color)
        if color.a == 255:
            pr.clear_background(color.to_pyray())
        else:
            pr.draw_rectangle(0, 0, self.width, self.height, color.to_pyray())

