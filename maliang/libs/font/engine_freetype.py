"""
# pip install freetype-py
"""

import freetype
import numpy as np
from PIL import Image
import math
from io import BytesIO
import pyray as pr


class FreeTyper():
    def __init__(self):
        pass

    def draw_bitmap(self, bitmap, x, y):
        glyph_pixels = bitmap.get("buffer", None)
        cols = bitmap.get("width", None)
        rows = bitmap.get("rows", None)
        for row in range(rows):
            for col in range(cols):
                _index = row * cols + col
                if glyph_pixels[_index] != 0:
                    try:
                        yield x + col, y + row, glyph_pixels[_index]
                    except:
                        continue

    # def draw_bitmap_np(self, bitmap, x, y):
    #     ## too slow
    #     glyph_pixels = bitmap.get("buffer", None)
    #     cols = bitmap.get("width", None)
    #     rows = bitmap.get("rows", None)
    #     np_bitmap = np.array(glyph_pixels).reshape(rows, cols)
    #     for row, col in zip(*np.nonzero(np_bitmap)):
    #         yield x + col, y + row, np_bitmap[row][col]

    def get_bbox(self, face, text, need_extra=True):
        extra_info = {}
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
            if need_extra:
                extra_info[cur_char] = {
                    'bitmap': {
                        'buffer': slot.bitmap.buffer,
                        'width': slot.bitmap.width,
                        'rows': slot.bitmap.rows,
                    },
                    'advance.x': slot.advance.x,
                    'advance.y': slot.advance.y,
                    'bitmap_left': slot.bitmap_left,
                    'bitmap_top': slot.bitmap_top,
                    'bbox': (cbox.xMin, cbox.xMax, cbox.yMin, cbox.yMax)
                }
        return bbox_xmin, bbox_xmax, bbox_ymin, bbox_ymax, extra_info


    def get_bbox_tmp(self, face, text, need_extra=True):
        # 1 计算 cbox 外框
        extra_info = {}
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
            if need_extra:
                extra_info[cur_char] = {
                    'bitmap': {
                        'buffer': bitmap.buffer,
                        'width': bitmap.width,
                        'rows': bitmap.rows,
                    },
                    'advance.x': slot.advance.x,
                    'advance.y': slot.advance.y,
                    'bitmap_left': slot.bitmap_left,
                    'bitmap_top': slot.bitmap_top,
                }
        return 0, max_width, 0, max_height, extra_info

class FontEngineFreetype():

    @classmethod
    def api_auto_load(cls, _file, filetype, font_size):
        face = freetype.Face(_file)
        return face

    @classmethod
    def _yield_points(cls, face, text, x, y, text_color=(0, 0, 0, 255), space_x=0):
        # done : text loaded twice by font need dec 1
        # 1 计算 cbox 外框
        try:
            bbox_xmin, bbox_xmax, bbox_ymin, bbox_ymax, extra_info = FreeTyper().get_bbox(face, text, need_extra=True)
        except:
            bbox_xmin, bbox_xmax, bbox_ymin, bbox_ymax, extra_info = FreeTyper().get_bbox_tmp(face, text, need_extra=True)

        pen = freetype.Vector()
        pen.x = x
        pen.y = y + bbox_ymax # [+]文字在坐标原点右下方 [-]文字在坐标原点右上方
        alpha_cord = text_color[3] / 255
        for cur_char in text:
            char_info = extra_info.get(cur_char, {})
            for _x, _y, alpha in FreeTyper().draw_bitmap(
                    char_info['bitmap'],
                    int(pen.x) + char_info['bitmap_left'],
                    int(pen.y) - char_info['bitmap_top'],
                ):
                yield _x, _y, (*text_color[:3], int(alpha_cord*alpha))

            pen.x += int(char_info['advance.x'] / 64) + space_x
            pen.y += int(char_info['advance.y'] / 64)


    @classmethod
    def _yield_points_multiline(cls, face, text, x, y, text_size=12, text_color=(0, 0, 0, 255), space_x=0, space_y=0, need_size=True):
        resolution = 64
        face.set_char_size(text_size * resolution)

        line_height = math.floor( text_size * face.height / face.units_per_EM)
        # print(line_height)
        max_x, max_y = x, y # 坐标
        line_y = y
        for i, t in enumerate(text.split('\n')):
            if t:
                for _x, _y, color in cls._yield_points(face, t, x, line_y, text_color=text_color, space_x=space_x):
                    yield _x, _y, color
                    if need_size:
                        if _x > max_x: max_x = _x
                        if _y > max_y: max_y = _y
            line_y = line_y + line_height + space_y
        if need_size:
            yield max_x, max_y, None


    @classmethod
    def api_text_to_image(cls, face, text, text_size=12, text_color=(0, 0, 0, 255), space_x=0, space_y=0):
        yield_points = cls._yield_points_multiline(face, text, 0, 0, text_size, text_color, space_x, space_y)
        points = []
        width, height = 0, 0
        for _x, _y, color in yield_points:
            if color:
                points.append(((_x, _y), color))
            else:
                width, height = _x+1, _y+1

        np_array = np.zeros((height, width, 4), np.uint8)
        for xy, color in points:
            np_array[xy[1]][xy[0]] = color
        im = Image.fromarray(np_array, "RGBA")
        output = BytesIO()
        im.save(output, format='PNG')
        del im
        return ".png", output.getvalue()

        # im = Image.new("RGBA", (width, height))
        # for xy, color in points:
        #     im.putpixel(xy, color)
        # # im.show()
        # output = BytesIO()
        # im.save(output, format='PNG')
        # del im
        # return ".png", output.getvalue()


    @classmethod
    def api_text(cls, face, text, x, y, text_size, text_color, space_x, space_y):
        # way2
        # yield_points = cls._yield_points_multiline(face, text, x, y, text_size, text_color, space_x, space_y, need_size=False)
        # for _x, _y, color in yield_points:
        #     if color:
        #         pr.draw_pixel(_x, _y, pr.Color(*color))

        img_format, img_data = cls.api_text_to_image(face, text, text_size=text_size,
                                                     text_color=text_color, space_x=space_x, space_y=space_y)
        image = pr.load_image_from_memory(img_format, img_data, len(img_data))
        texture = pr.load_texture_from_image(image)
        pr.draw_texture(texture, x, y, pr.WHITE)
        pr.unload_image(image)
        return texture

