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
import pyray as pr


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
        # metrics = face.size
        # ascender = int((metrics.ascender-metrics.descender)/64)
        # print('ascender ',ascender, metrics.descender/64)
        # 1 计算 cbox 外框
        bbox_xmin, bbox_xmax, bbox_ymin, bbox_ymax = FreeTyper().get_bbox(face, text)
        print("bbox: ", bbox_xmin, bbox_xmax, bbox_ymin, bbox_ymax)
        bbox_width = bbox_xmax - bbox_xmin + 1
        bbox_height = bbox_ymax - bbox_ymin + 1
        print("box_size: ", bbox_width, bbox_height)
        pen = freetype.Vector()
        pen.x = x
        pen.y = y + bbox_height # [+]文字在坐标原点右下方 [-]文字在坐标原点右上方

        for cur_char in text:
            print(cur_char)
            face.load_char(cur_char)
            slot = face.glyph
            bitmap = slot.bitmap
            # print(pen.x, pen.y, slot.bitmap_left, slot.bitmap_top)
            for x, y, color in FreeTyper().draw_bitmap(bitmap, int(pen.x) + slot.bitmap_left,
                                                     int(pen.y)-slot.bitmap_top, text_color):
                if (x>=0 and y>=0):
                    yield x, y, color
                else:
                    print(cur_char, x, y)
            pen.x += int(slot.advance.x / 64)
            pen.y += int(slot.advance.y / 64)

    @classmethod
    def api_text_to_image(cls, img, face, text, text_size=12, text_color=(0, 0, 0, 255), space_x=0, space_y=0):
        for _x, _y, color in cls._yield_points(face, text, x=0, y=0, text_size=text_size, text_color=text_color, space_x=space_x, space_y=space_y):
            img.putpixel((_x, _y), color)
        img.putpixel((0, 0), (255, 0, 0, 255))
        img.putpixel((-1, 0), (255, 0, 0, 255))
        img.putpixel((0, -1), (255, 0, 0, 255))
        img.putpixel((-1, -1), (255, 0, 0, 255))
        img.show()
        return ".png", b""

    @classmethod
    def api_text(cls, face, text, x, y, text_size, text_color, space_x, space_y):
        texshapes = pr.Texture(10, 1, 1, 1, 7)
        texshapesRec = pr.Rectangle(0, 0, 1, 1)
        # pr.rl_set_texture(texshapes.id)
        pr.rl_begin(7)
        pr.rl_normal3f(0.0, 0.0, 1.0)

        def draw_point_quad(x, y, color):
            pr.rl_color4ub(*color)

            pr.rl_tex_coord2f(texshapesRec.x / texshapes.width, texshapesRec.y / texshapes.height)
            pr.rl_vertex2f(x, y)

            pr.rl_tex_coord2f(texshapesRec.x / texshapes.width,
                              (texshapesRec.y + texshapesRec.height) / texshapes.height)
            pr.rl_vertex2f(x, y + 1)

            pr.rl_tex_coord2f((texshapesRec.x + texshapesRec.width) / texshapes.width,
                              (texshapesRec.y + texshapesRec.height) / texshapes.height)
            pr.rl_vertex2f(x + 1, y + 1)

            pr.rl_tex_coord2f((texshapesRec.x + texshapesRec.width) / texshapes.width,
                              texshapesRec.y / texshapes.height)
            pr.rl_vertex2f(x + 1, y)

        for _x, _y, color in cls._yield_points(face, text, x, y, text_size, text_color, space_x, space_y):
            # print(_x, _y, color)
            draw_point_quad(_x, _y, color)

        pr.rl_end()
        # pr.rl_set_texture(0)


if __name__ == '__main__':
    # text = "FonFtfont"
    # text = "Fontfontga阿瓦达多"
    # text = "FONT"
    # text = "Fontf"
    text = "hello Fontf你好"
    t = FontEngineFreetype()
    face = t.api_auto_load("/Users/nana/Work/maliang/examples/./resources/yezigongchangweifengshouji.ttf", None, None)
    img = Image.new("RGBA", (800, 300), "white")

    # for i in range(0, 200):
    #     img.putpixel((i, 100), (0,0,0,255))
    # img.show()
    # exit(0)
    result = t.api_text_to_image(img, face, text, text_size=24, text_color=(0, 0, 0, 255))
    print(result)
