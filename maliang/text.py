import pyray as pr
from maliang.structs import MFont, MColor, MImage

class Text:
    def __init__(self):
        self.text_font = None
        self.text_size = 12
        self.text_color = pr.BLACK

    def init_font(self, font):
        return font or self.text_font or None

    def textSize(self, _size):
        self.text_size = _size

    def textColor(self, *color):
        self.text_color = color

    def textFont(self, font: MFont):
        self.text_font = font

    def text(self, text, x=0, y=0, text_size=None, text_color=None, font: MFont = None):
        space = 0   # not supported yet
        font = font or self.text_font
        text_size = text_size or self.text_size
        text_color = text_color or self.text_color
        if font:
            font.text(text, x, y, text_size=text_size, text_color=text_color)
        else:
            pr.draw_text_ex(pr.get_font_default(), text, pr.Vector2(x, y), text_size, space, MColor(*text_color).to_pyray())

    def text_image(self, text, text_size=12, text_color=None, font: MFont = None):
        space = 0   # not supported yet
        font = font or self.text_font
        text_size = text_size or self.text_size
        text_color = text_color or self.text_color
        if font:
            img = font.text_image(text, text_size=text_size, text_color=text_color)
        else:
            img = MImage()
            img.pr_image = pr.image_text_ex(pr.get_font_default(), text, text_size, space, MColor(*text_color).to_pyray())
        return img
