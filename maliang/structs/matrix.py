import pyray as pr

class MMatrix():
    def __init__(self, *args, **kwargs):
        self.pr_matrix = pr.Matrix(*args, **kwargs)

