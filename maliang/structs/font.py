import pyray as pr


class MFont:
    def __init__(self):
        self._bin = b''
        self._len = 0
        self._type = '.ttf'

    # def unload(self):
    #     if self.pr_font:
    #         pr.unload_font(self.pr_font)
    #         self.pr_font = None

    # def base_size(self):
    #     return self.pr_font.base_size