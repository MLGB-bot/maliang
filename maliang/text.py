import pyray as pr
from maliang.structs import MFont, MColor
from maliang.units import ResourceLoader

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

    def text(self, text, x, y, font: MFont=None, text_size=None, text_color=None, space=0):
        # void DrawTextPro(Font font, const char *text, Vector2 position, Vector2 origin, float rotation, float fontSize, float spacing, Color tint); // Draw text using Font and pro parameters (rotation)
        font = font or self.text_font
        text_size = text_size or self.text_size
        text_color = text_color or self.text_color
        if font:
            codepoints_count = 0
            # codepointsCount = ffi.new("int *")
            codepoints = pr.load_codepoints(text, codepoints_count)
            # print(codepoints)
            font_runtime = pr.load_font_from_memory(font._type, font._bin, font._len, text_size, codepoints, len(text) )
            pr.unload_codepoints(codepoints)
            pr.draw_text_ex(font_runtime, text, pr.Vector2(x, y), text_size, space, MColor(*text_color).to_pyray() )
            # pr.unload_font(fontx)
            # done unload font after end_draw()
            ResourceLoader.loaded_fonts_runtime.append(font_runtime)
        else:
            pr.draw_text(text, x, y, text_size, MColor(*text_color).to_pyray())