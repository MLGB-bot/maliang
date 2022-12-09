import pyray as pr

class MaliangColorFormatError(Exception):
    def __init__(self, message):
        self.message = message

class MColor():
    def __init__(self, *args, **kwargs):
        # print('color:', *args)
        self.init_rgba_int(args)

    def init_rgba_int(self, args:tuple):
        """
        Colors are defined by values between 0 and 255 using the RGBA color model
        :param args:
        :return:
        """
        if len(args) == 1:
            self.r = self.g = self.b = args[0]
            self.a = 255
        elif len(args) == 2:
            self.r = self.g = self.b = args[0]
            self.a = args[1]
        elif len(args) == 3:
            self.r, self.g, self.b = args
            self.a = 255
        elif len(args) == 4:
            self.r, self.g, self.b, self.a = args
        else:
            raise MaliangColorFormatError(f"Cannot convert '{args}' to color.")
        assert isinstance(self.r, int)
        assert isinstance(self.g, int)
        assert isinstance(self.b, int)
        assert isinstance(self.a, int)

    def __iter__(self):
        yield self.r
        yield self.g
        yield self.b
        yield self.a

    def to_pyray(self):
        return pr.Color(self.r, self.g, self.b, self.a)