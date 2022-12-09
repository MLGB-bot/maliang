import os
import pyray as pr
from maliang.units import ResourceLoader
from maliang.structs import MColor, MFont, MImage, MGlyph


class Font():
    def __init__(self):
        pass

    def default_font(self):
        font = MFont()
        font.pr_font = pr.get_font_default()
        return font

    def load_font(self, filename, fontsize=None, fontchars=None, glyphcount=0):
        _path = os.path.join(ResourceLoader.static_dir, filename)
        font = MFont()
        if fontsize:
            font.pr_font = pr.load_font(_path)
        else:
            font.pr_font = pr.load_font_ex(_path, fontsize, fontchars, glyphcount)
        return font

    def load_font_from_image(self, img: MImage, color: MColor, firstchar=0):
        font = MFont()
        font.pr_font = pr.load_font_from_image(img.pr_image, color.to_pyray(), firstchar)
        return font

    def load_font_data(self, data, filetype='.ttf', fontsize=None, fontchars=None, glyphcount=0):
        font = MFont()
        font.pr_font = pr.load_font_from_memory(filetype, data, len(data), fontsize, fontchars, glyphcount)
        return font

    def unload_font(self, font: MFont):
        font.unload()

    def load_glyph_from_font_data(self, data, fontsize=None, fontchars=None, glyphcount=0, type=0):
        glyph = MGlyph()
        glyph.pr_glyph = pr.load_font_data(data, len(data), fontsize, fontchars, glyphcount, type)
        glyph.glyphcount = glyphcount
        return glyph
