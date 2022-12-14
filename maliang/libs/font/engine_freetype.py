"""
# pip install freetype-py
"""
try:
    import freetype
except:
    pass
import math
from io import BytesIO
from PIL import ImageDraw, Image, ImageFont


class FontEngineFreetype():

    @classmethod
    def api_auto_load(cls, _file, filetype, font_size):
        face = freetype.Face(_file)

        metrics = face.size
        ascender = metrics.ascender / 64   # 上升
        descender = metrics.descender/64.0    # 下降
        height = metrics.height/64.0  # 高度
        linegap = height - ascender + descender # 行间距

        print(ascender, descender, height, linegap)
        return face

    @classmethod
    def _yield_points(cls, face, text, text_size=12, text_color=(0, 0, 0, 255), space_x=0, space_y=0):
        x = 64
        face.set_char_size(text_size * x)
        prev_char = 0
        pen = freetype.Vector()
        pen.x = 0
        pen.y = 0

        cur_pen = freetype.Vector()
        # iterable
        # hscale = 1.0
        # matrix = freetype.Matrix(int(hscale) * 0x10000, int(0.2 * 0x10000),
        #                          int(0.0 * 0x10000), int(1.1 * 0x10000))
        # pen_translate = freetype.Vector()
        for cur_char in text:
            # face.set_transform(matrix, pen_translate)
            face.load_char(cur_char)
            kerning = face.get_kerning(prev_char, cur_char)
            pen.x += kerning.x
            slot = face.glyph
            bitmap = slot.bitmap

            cur_pen.x = pen.x
            cur_pen.y = pen.y - slot.bitmap_top * x
            # self.draw_ft_bitmap(image, bitmap, cur_pen, color)
            x_pos = pen.x
            y_pos = pen.y
            cols = bitmap.width
            rows = bitmap.rows
            # print(x_pos, y_pos, x_pos/x , y_pos)
            glyph_pixels = bitmap.buffer

            for row in range(rows):
                for col in range(cols):
                    if glyph_pixels[row * cols + col] != 0:
                        try:
                            _x, _y = int(x_pos / x) + col, y_pos + row
                            yield (_x, _y), (*text_color[:3], glyph_pixels[row * cols + col])
                        except:
                            continue
            pen.x += (slot.advance.x)
            prev_char = cur_char

    @classmethod
    def api_text_to_image(cls, img, face, text, text_size=12, text_color=(0, 0, 0, 255), space_x=0, space_y=0):
        for xy, color in cls._yield_points(face, text, text_size, text_color, space_x, space_y):
            img.putpixel(xy, color)
        img.show()
        return ".png", b""

    @classmethod
    def api_text(cls, face, text, x, y, text_size, text_color, space_x, space_y):
        for xy, color in cls._yield_points(face, text, text_size, text_color, space_x, space_y):
            pass

if __name__ == '__main__':
    text = "FONT"
    t = FontEngineFreetype()
    face = t.api_auto_load("/Users/nana/Work/maliang/examples/./resources/yezigongchangweifengshouji.ttf", None, None)
    img = Image.new("RGBA", (200, 200), "white")

    # for i in range(0, 200):
    #     img.putpixel((i, 100), (0,0,0,255))
    # img.show()
    # exit(0)
    result = t.api_text_to_png(img, face, text, text_size=64, text_color=(0, 0, 0, 255))
    print(result)
