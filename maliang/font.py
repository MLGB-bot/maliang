import os
from maliang.units import ResourceLoader
from maliang.structs import MFont

class Font():
    def __init__(self):
        pass

    def load_font(self, filename, filetype='.ttf'):
        _path = os.path.join(ResourceLoader.static_dir, filename)
        font = MFont()
        with open(_path, 'rb') as f:
            font._bin = f.read()
            font._len = len(font._bin)
            font._type = filetype
        return font


    # def load_font_from_image(self, img: MImage, color: MColor, firstchar=0):
    #     font = MFont()
    #     font.pr_font = pr.load_font_from_image(img.pr_image, color.to_pyray(), firstchar)
    #     return font

