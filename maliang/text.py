import pyray as pr
from maliang.structs import MFont, MColor


class Text:
    def __init__(self):
        self.font = None
        self.font_size = 12
        self.font_color = pr.BLACK

    def init_font(self, font):
        return font or self.font or None


    def text(self, chars, x, y, w, h, font: MFont=None, font_size=None, font_color=None, space=0):
        # todo
        # void DrawText(const char *text, int posX, int posY, int fontSize, Color color);       // Draw text (using default font)
        # void DrawTextEx(Font font, const char *text, Vector2 position, float fontSize, float spacing, Color tint); // Draw text using font and additional parameters
        # void DrawTextPro(Font font, const char *text, Vector2 position, Vector2 origin, float rotation, float fontSize, float spacing, Color tint); // Draw text using Font and pro parameters (rotation)
        font = font or self.font
        font_size = font_size or self.font_size
        font_color = font_color or self.font_color
        if font:
            pr.draw_text_ex(font.pr_font, chars, pr.Vector2(x, y), font_size, space, MColor(*font_color).to_pyray() )
            # pr.draw_text_pro(font.pr_font, chars, pr.Vector2(x, y), font_size,  )
        else:
            pr.draw_text(chars, x, y, font_size, MColor(*font_color).to_pyray())