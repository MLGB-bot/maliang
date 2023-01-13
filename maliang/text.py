import pyray as pr
from maliang.structs import MFont, MColor, MImage

class Text:
    def __init__(self):
        self.__text_font = None
        self.__text_size = 12
        self.__text_color = pr.BLACK

    def text_size(self, size):
        self.__text_size = size

    def text_color(self, *color):
        self.__text_color = color

    def text_font(self, font: MFont):
        self.__text_font = font

    def init_text_color(self, text_color):
        if isinstance(text_color, MColor):
            return text_color
        else:
            return MColor(*text_color)

    def text(self, text, x=0, y=0, text_size=None, text_color=None, font: MFont = None, space_x=1):
        font = font or self.__text_font
        text_size = text_size or self.__text_size
        text_color = self.init_text_color(text_color or self.__text_color)
        if font:
            font.text(text, x, y, text_size=text_size, text_color=tuple(text_color), space_x=space_x)
        else:
            pr.draw_text_ex(pr.get_font_default(), text, pr.Vector2(x, y), text_size, space_x, text_color.to_pyray())

    def text_image(self, text, text_size=12, text_color=None, font: MFont = None, space_x=1):
        font = font or self.__text_font
        text_size = text_size or self.__text_size
        text_color = self.init_text_color(text_color or self.__text_color)
        if font:
            img = font.text_image(text, text_size=text_size, text_color=tuple(text_color), space_x=space_x)
        else:
            img = MImage()
            img.pr_image = pr.image_text_ex(pr.get_font_default(), text, text_size, space_x, text_color.to_pyray())
        return img
