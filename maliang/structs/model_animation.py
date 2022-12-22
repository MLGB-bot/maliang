import pyray as pr

class MModelAnimation:
    def __init__(self):
        self.pr_model_animation = None

    def unload(self):
        pr.unload_model_animation(self.pr_model_animation)

