import pyray as pr

class MTexture:
    def __init__(self):
        self.pr_texture = None

    def unload(self):
        if self.pr_texture:
            pr.unload_texture(self.pr_texture)
            self.pr_texture = None