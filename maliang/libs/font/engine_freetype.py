"""
# pip install freetype-py
"""
import os.path

try:
    import freetype
except:
    pass
import math
from io import BytesIO
from PIL import ImageDraw, Image, ImageFont
import pyray as pr

from OpenGL.GL import *

class FreeTyper():
    def __init__(self):
        pass

    def draw_bitmap(self, bitmap, x, y, text_color):
        glyph_pixels = bitmap.buffer
        cols = bitmap.width
        rows = bitmap.rows
        for row in range(rows):
            for col in range(cols):
                if glyph_pixels[row * cols + col] != 0:
                    try:
                        yield x + col, y + row, (*text_color[:3], glyph_pixels[row * cols + col])
                    except:
                        continue

    def get_bbox(self, face, text):
        # 1 计算 cbox 外框
        bbox_xmin = None
        bbox_xmax = None
        bbox_ymin = None
        bbox_ymax = None
        pen = freetype.Vector()
        pen.x = 0
        pen.y = 0
        # matrix = freetype.Matrix()
        for cur_char in text:
            # face.set_transform(matrix, pen)
            face.load_char(cur_char)
            # print("kerning: ", kerning.x, kerning.y)
            slot = face.glyph
            glyph = slot.get_glyph()
            cbox = glyph.get_cbox(freetype.FT_GLYPH_BBOX_MODES['FT_GLYPH_BBOX_TRUNCATE'])
            # print(cur_char, cbox, cbox.xMax, cbox.xMin, cbox.yMax, cbox.yMin)
            bbox_xmin = cbox.xMin if bbox_xmin is None else min(bbox_xmin, cbox.xMin)
            bbox_xmax = cbox.xMax if bbox_xmax is None else max(bbox_xmax, cbox.xMax)
            bbox_ymin = cbox.yMin if bbox_ymin is None else min(bbox_ymin, cbox.yMin)
            bbox_ymax = cbox.yMax if bbox_ymax is None else max(bbox_ymax, cbox.yMax)
            # pen.x += slot.advance.x
            # pen.y += slot.advance.y
        return bbox_xmin, bbox_xmax, bbox_ymin, bbox_ymax

    def get_bbox_tmp(self, face, text):
        # 1 计算 cbox 外框
        pen = freetype.Vector()
        pen.x = 0
        pen.y = 0
        max_width, max_height=0, 0
        for cur_char in text:
            face.load_char(cur_char)
            slot = face.glyph
            bitmap = slot.bitmap
            max_width = max(bitmap.width, max_width)
            max_height = max(bitmap.rows, max_height)
        return 0, max_width, 0, max_height

class FontEngineFreetype():

    @classmethod
    def api_auto_load(cls, _file, filetype, font_size):
        face = freetype.Face(_file)
        return face

    @classmethod
    def _yield_points(cls, face, text, x, y, text_size=12, text_color=(0, 0, 0, 255), space_x=0, space_y=0):
        # todo : text loaded twice by font need dec 1
        resolution = 64
        face.set_char_size(text_size * resolution)
        # 1 计算 cbox 外框
        try:
            bbox_xmin, bbox_xmax, bbox_ymin, bbox_ymax = FreeTyper().get_bbox(face, text)
        except:
            bbox_xmin, bbox_xmax, bbox_ymin, bbox_ymax = FreeTyper().get_bbox_tmp(face, text)

        pen = freetype.Vector()
        pen.x = x
        pen.y = y + bbox_xmax # [+]文字在坐标原点右下方 [-]文字在坐标原点右上方

        for cur_char in text:
            # print(cur_char)
            face.load_char(cur_char)
            slot = face.glyph
            bitmap = slot.bitmap
            # print(pen.x, pen.y, slot.bitmap_left, slot.bitmap_top)
            for _x, _y, color in FreeTyper().draw_bitmap(bitmap, int(pen.x) + slot.bitmap_left,
                                                     int(pen.y)-slot.bitmap_top, text_color):
                yield _x, _y, color

            pen.x += int(slot.advance.x / 64)
            pen.y += int(slot.advance.y / 64)


    @classmethod
    def api_text_to_image(cls, face, text, text_size=12, text_color=(0, 0, 0, 255), space_x=0, space_y=0):
        yield_points = cls._yield_points(face, text, 0, 0, text_size, text_color, space_x, space_y)
        min_x, min_y = 0, 0
        max_x, max_y = 0, 0
        points = []
        for _x, _y, color in yield_points:
            max_x = max(max_x, _x)
            max_y = max(max_y, _y)
            points.append(((_x, _y), color))
        width = max_x - min_x + 1
        height = max_y - min_y + 1

        im = Image.new("RGBA", (width, height))
        for xy, color in points:
            im.putpixel(xy, color)
        # im.show()
        output = BytesIO()
        im.save(output, format='PNG')
        del im
        return ".png", output.getvalue()

    @classmethod
    def api_text(cls, face, text, x, y, text_size, text_color, space_x, space_y):
        # way2
        yield_points = cls._yield_points(face, text, x, y, text_size, text_color, space_x, space_y)
        for _x, _y, color in yield_points:
            pr.draw_pixel(_x, _y, pr.Color(*color))


if __name__ == '__main__':
    # text = "FonFtfont"
    text = "Fontfontga阿瓦达多"
    # text = "FONT"
    # text = "Fontf"
    # text = "hello Fontf你好"
    t = FontEngineFreetype()
    face = t.api_auto_load("../../../examples/resources/yezigongchangweifengshouji.ttf", None, None)
    result = t.api_text_to_image(face, text, text_size=24, text_color=(0, 0, 0, 255))
    print(result)
