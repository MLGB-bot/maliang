import pyray as pr


class MFont:
    def __init__(self):
        self._bin = b''
        self._len = 0
        self._type = '.ttf'

    # def base_size(self):
    #     return self.pr_font.base_size