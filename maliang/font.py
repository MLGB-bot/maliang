import os
import pyray as pr
from raylib._raylib_cffi import ffi
from maliang.units import ResourceLoader
from maliang.structs.font import FontEngines
from maliang.structs import MFont


class Font(FontEngines):
    def __init__(self):
        pass

    def load_font(self, filename='', filetype='.ttf', engine_id=1, engine_font_size=64, engine=None):
        _path = os.path.join(ResourceLoader.static_dir, filename) if filename else ''
        if engine_id == self.FONT_RAYLIB:
            font = MFont()
            font.engine_id = self.FONT_RAYLIB
            font._type = filetype
            # with open(_path, 'rb') as f:
            #     font._bin = f.read()
            #     font._len = len(font._bin)
            file_size = ffi.new('unsigned int *')
            file_data = pr.load_file_data(_path, file_size) if _path else None
            font._bin = file_data
            font._len = file_size[0]
            return font
        elif engine:
            font = MFont()
            font.font_size = engine_font_size
            if _path:
                if os.path.exists(_path) and os.path.isfile(_path):
                    pass
                else:
                    _path = filename
            font._type = filetype
            # set engine info
            font.engine_id = engine_id
            font.engine_font = engine.api_auto_load(_path, filetype, engine_font_size)
            font.engine = engine
            return font
