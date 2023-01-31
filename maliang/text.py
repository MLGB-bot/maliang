import pyray as pr
from maliang.structs import MFont, MColor, MImage, MFontSet

class Text:
    def __init__(self):
        self.__text_font = None
        self.__font_size = 12
        self.__text_color = pr.BLACK

    def font_size(self, size):
        self.__font_size = size

    def text_color(self, *color):
        self.__text_color = color

    def text_font(self, font: MFont | MFontSet):
        self.__text_font = font

    def init_text_color(self, text_color):
        if isinstance(text_color, MColor):
            return text_color
        else:
            return MColor(*text_color)

    def text(self, text, x=0, y=0, font_size=None, text_color=None, font: MFont|MFontSet = None, space_x=1):
        font = font or self.__text_font
        font_size = font_size or self.__font_size
        text_color = self.init_text_color(text_color or self.__text_color)
        if isinstance(font, MFont):
            font.text(text, x, y, font_size=font_size, text_color=text_color, space_x=space_x)
        else:
            pr_font = font.pr_font if isinstance(font, MFontSet) else pr.get_font_default()
            pr.draw_text_ex(pr_font, text, pr.Vector2(x, y), font_size, space_x, text_color.to_pyray())

    def text_image(self, text, font_size=12, text_color=None, font: MFont|MFontSet = None, space_x=1):
        font = font or self.__text_font
        font_size = font_size or self.__font_size
        text_color = self.init_text_color(text_color or self.__text_color)
        if isinstance(font, MFont):
            img = font.text_image(text, font_size=font_size, text_color=text_color, space_x=space_x)
        else:
            pr_font = font.pr_font if isinstance(font, MFontSet) else pr.get_font_default()
            img = MImage()
            img.pr_image = pr.image_text_ex(pr_font, text, font_size, space_x, text_color.to_pyray())
        return img
