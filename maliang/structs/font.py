import maliang.structs.image as mod_image
import maliang.structs.color as mod_color
import pyray as pr
import maliang.units.resource_loader as mod_resource
from raylib._raylib_cffi import ffi


class FontEngines:
    # Engines
    FONT_RAYLIB = 1


FontEngineFuncStore = {}


def engine(engine_id):
    global FontEngineFuncStore

    def dec(func):
        func_name = func.__qualname__
        FontEngineFuncStore[(engine_id, func_name)] = func

        def wrap(self, *args, **kwargs):
            f = FontEngineFuncStore.get((self.engine_id, func_name), None)
            if f:
                return f(self, *args, **kwargs)
            elif hasattr(self, 'engine') and self.engine:
                f = FontEngineFuncStore[(0, func_name)]
                return f(self, *args, **kwargs)

        return wrap

    return dec


class MFontSet:
    def __init__(self):
        self.pr_font = None

    # def text(self, text, x, y, text_size=None, text_color: mod_color.MColor=None, space_x=0, space_y=0):
    #     pr.draw_text_ex(self.pr_font, text, pr.Vector2(x, y), text_size, space_x, text_color.to_pyray())

    # def text_image(self, text, text_size=12, text_color: mod_color.MColor=None, space_x=0, space_y=0):
    #     return pr.image_text_ex(self.pr_font, text, text_size, space_x, text_color.to_pyray())

class MFont:
    def __init__(self):
        self._bin = None
        self._len = 0
        self._type = '.ttf'

        # interface engine
        self.engine_id = 0
        self.engine_font = None
        self.engine = None

    def generate_m_image_from_data(self, filetype, filedata):
        m_image = mod_image.MImage()
        m_image.pr_image = pr.load_image_from_memory(filetype, filedata, len(filedata))
        return m_image

    def generate_raylib_temp_font(self, text='', text_size=12):
        codepoints_count = ffi.new("int *")
        codepoints = pr.load_codepoints(text, codepoints_count)
        # print(text, "codepoints_count[0]: ", codepoints_count[0])
        font_runtime = pr.load_font_from_memory(self._type, self._bin, self._len, text_size, codepoints,
                                                codepoints_count[0])
        pr.unload_codepoints(codepoints)
        del codepoints_count
        # add to resource
        mod_resource.ResourceLoader.loaded_fonts_runtime.append(font_runtime)
        # pr.unload_font(font_runtime)
        return font_runtime

    @engine(FontEngines.FONT_RAYLIB)
    def text_image(self, text, text_size=12, text_color: mod_color.MColor=None, space_x=0, space_y=0) -> mod_image.MImage:
        img = mod_image.MImage()
        font_runtime = self.generate_raylib_temp_font(text, text_size)
        img.pr_image = pr.image_text_ex(font_runtime, text, text_size, space_x,
                                        text_color.to_pyray())
        return img

    @engine(FontEngines.FONT_RAYLIB)
    def text(self, text, x, y, text_size=None, text_color: mod_color.MColor=None, space_x=0, space_y=0):
        font_runtime = self.generate_raylib_temp_font(text, text_size)
        pr.draw_text_ex(font_runtime, text, pr.Vector2(x, y), text_size, space_x,
                        text_color.to_pyray())

    @engine(0)
    def text_image(self, text, text_size=12, text_color: mod_color.MColor=None, space_x=0, space_y=0) -> mod_image.MImage:
        img_format, img_data = self.engine.api_text_to_image(self.engine_font, text, text_size=text_size,
                                                             text_color=tuple(text_color),
                                                             space_x=space_x, space_y=space_y)
        m_image = self.generate_m_image_from_data(img_format, img_data)
        return m_image

    @engine(0)
    def text(self, text, x, y, text_size=None, text_color: mod_color.MColor=None, space_x=0, space_y=0):
        texture = self.engine.api_text(self.engine_font, text, x, y, text_size, tuple(text_color), space_x, space_y)
        if texture:
            mod_resource.ResourceLoader.loaded_texture_runtime.append(texture)
