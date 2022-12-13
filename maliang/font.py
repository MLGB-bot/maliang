import os
import pyray as pr
from raylib._raylib_cffi import ffi
from maliang.units import ResourceLoader
from maliang.structs.font import FontEngines
from maliang.structs import MFont
from maliang.libs import FontEnginePillow


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
            font.font_size = font_engine_pillow_font_size
            if _path:
                if os.path.exists(_path) and os.path.isfile(_path):
                    pass
                else:
                    # try to search font in system font dictionary
                    _path = filename
            pil_obj = FontEnginePillow.auto_load(_path, filetype, font_engine_pillow_font_size)
            font._type = filetype
            font._pil = pil_obj
            return font

