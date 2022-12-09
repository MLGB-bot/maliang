from maliang import Maliang
import pyray as pr

import random
class App(Maliang):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_draw(self):
        self.point( random.randint(0, self.width), random.randint(0, self.height), stroke_color=pr.RED)

if __name__ == '__main__':
    app = App(fps=60, double_buffer=False)
    app.loop()