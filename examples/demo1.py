import random
from maliang import Maliang

class App(Maliang):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_draw(self):
        self.point( random.randint(0, self.width), random.randint(0, self.height), stroke_color=(255, 0,0))

if __name__ == '__main__':
    app = App(fps=60, buffer_proxy=True)
    app.run()