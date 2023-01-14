import os
import pyray as pr
from raylib._raylib_cffi import ffi
from maliang.units import ResourceLoader
from maliang.structs.font import FontEngines
from maliang.structs import MFont, MFontSet


class Font:
    def __init__(self):
        pass

    def load_font(self, filename='', filetype='.ttf', engine=None, engine_fontsize=64, ):
        _path = os.path.join(ResourceLoader.static_dir, filename) if filename else ''
        if not engine:
            font = MFont()
            font.engine_id = FontEngines.FONT_RAYLIB
            font._type = filetype
            # with open(_path, 'rb') as f:
            #     font._bin = f.read()
            #     font._len = len(font._bin)
            file_size = ffi.new('unsigned int *')
            file_data = pr.load_file_data(_path, file_size) if _path else None
            font._bin = file_data
            font._len = file_size[0]
            return font
        else:
            font = MFont()
            font.fontsize = engine_fontsize
            if _path:
                if os.path.exists(_path) and os.path.isfile(_path):
                    pass
                else:
                    _path = filename
            font._type = filetype
            # set engine info
            font.engine_id = 0
            font.engine_font = engine.api_auto_load(_path, filetype, engine_fontsize)
            font.engine = engine
            return font

    def load_fontset(self, filename='', fontsize=32, words=''):
        _path = os.path.join(ResourceLoader.static_dir, filename) if filename else ''
        fontset = MFontSet()
        codepoints_count = ffi.new("int *")
        codepoints = pr.load_codepoints(words, codepoints_count)
        fontset.pr_font = pr.load_font_ex(_path, fontsize, codepoints, codepoints_count[0])
        # print(fontset.pr_font.baseSize)
        pr.unload_codepoints(codepoints)
        del codepoints_count
        return fontset