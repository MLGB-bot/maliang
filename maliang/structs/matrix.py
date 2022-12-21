import pyray as pr

class MMatrix(pr.Matrix):
    def __init__(self, *args, **kwargs):
        pr.Matrix.__init__(self, *args, **kwargs)