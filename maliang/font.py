import os
import pyray as pr
from raylib._raylib_cffi import ffi
from maliang.units import ResourceLoader
from maliang.structs.font import FontEngines
from maliang.structs import MFont
try:
    from PIL import ImageFont
except:
    pass

class Font(FontEngines):
    def __init__(self):
        pass

    def load_font(self, filename='', filetype='.ttf', font_engine=1, font_engine_pillow_font_size=64):
        _path = os.path.join(ResourceLoader.static_dir, filename) if filename else ''
        if font_engine == self.FONT_RAYLIB:
            font = MFont()
            font._eng = self.FONT_RAYLIB
            font._type = filetype
            # with open(_path, 'rb') as f:
            #     font._bin = f.read()
            #     font._len = len(font._bin)
            file_size = ffi.new('unsigned int *')
            file_data = pr.load_file_data(_path, file_size) if _path else None
            font._bin = file_data
            font._len = file_size[0]
            return font
        elif font_engine == self.FONT_PILLOW:
            font = MFont()
            font._eng = self.FONT_PILLOW
            if _path:
                if filetype in ('.ttf', '.ttc'):
                    pil_obj = ImageFont.truetype(_path, size=font_engine_pillow_font_size)
                    font.font_size = font_engine_pillow_font_size
                else:
                    pil_obj = ImageFont.load(_path)
            else:
                pil_obj = ImageFont.load_default()

            font._type = filetype
            font._pil = pil_obj
            return font


    # def load_font_from_image(self, img: MImage, color: MColor, firstchar=0):
    #     font = MFont()
    #     font.pr_font = pr.load_font_from_image(img.pr_image, color.to_pyray(), firstchar)
    #     return font

