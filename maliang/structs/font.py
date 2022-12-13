import maliang.structs.image as mod_image
import maliang.structs.color as mod_color
import pyray as pr
from io import BytesIO
import maliang.units.resource_loader as mod_resource
from raylib._raylib_cffi import ffi
from maliang.libs import FontEnginePillow


class FontEngines:
    FONT_RAYLIB = 1
    FONT_PILLOW = 2

    #
    FONT_ENGINE_PILLOW_DEFAULT_TRUETYPE_SIZE = 64  # pillow truetype default size


FontEngineFuncStore = {}


def engine(engine_id):
    global FontEngineFuncStore

    def dec(func):
        func_name = func.__qualname__
        FontEngineFuncStore[(engine_id, func_name)] = func

        def wrap(self, *args, **kwargs):
            f = FontEngineFuncStore.get((self._eng, func_name), None)
            if f:
                return f(self, *args, **kwargs)
            else:
                raise RuntimeError("No valud func matched")

        return wrap

    return dec


class MFont:
    def __init__(self):
        self._bin = None
        self._len = 0
        self._type = '.ttf'
        self._eng = 0
        self._pil = None  # Pillow engine

    def generate_raylib_temp_font(self, text='', text_size=12):
        codepoints_count = ffi.new("int *")
        codepoints = pr.load_codepoints(text, codepoints_count)
        # print(text, "codepoints_count[0]: ", codepoints_count[0])
        font_runtime = pr.load_font_from_memory(self._type, self._bin, self._len, text_size, codepoints,
                                                codepoints_count[0])
        pr.unload_codepoints(codepoints)
        # add to resource
        mod_resource.ResourceLoader.loaded_fonts_runtime.append(font_runtime)
        # pr.unload_font(font_runtime)
        return font_runtime

    @engine(FontEngines.FONT_RAYLIB)
    def text_image(self, text, text_size=12, text_color=(0, 0, 0, 255), space=0) -> mod_image.MImage:
        img = mod_image.MImage()
        font_runtime = self.generate_raylib_temp_font(text, text_size)
        img.pr_image = pr.image_text_ex(font_runtime, text, text_size, space, mod_color.MColor(*text_color).to_pyray())
        return img

    @engine(FontEngines.FONT_RAYLIB)
    def text(self, text, x, y, text_size=None, text_color=None, space=0):
        font_runtime = self.generate_raylib_temp_font(text, text_size)
        pr.draw_text_ex(font_runtime, text, pr.Vector2(x, y), text_size, space,
                        mod_color.MColor(*text_color).to_pyray())


    @engine(FontEngines.FONT_PILLOW)
    def text_image(self, text, text_size=12, text_color=(0, 0, 0, 255), space=0) -> mod_image.MImage:
        pillow_image = FontEnginePillow.generate_pillow_text_image(self._pil, text, text_size=text_size, text_color=text_color, space_y=space)
        m_image = mod_image.MImage()
        # raw  = pillow_image.tobytes()
        output = BytesIO()
        pillow_image.save(output, format='PNG')
        raw = output.getvalue()
        m_image.pr_image = pr.load_image_from_memory('.png', raw, len(raw))
        del pillow_image
        return m_image

    @engine(FontEngines.FONT_PILLOW)
    def text(self, text, x, y, text_size=None, text_color=None, space=0):
        img = self.text_image(text, text_size=text_size, text_color=text_color, space=space)
        # done unload texture
        texture = img.gen_texture()
        texture.draw(x, y, tint=pr.WHITE)
        img.unload()
        mod_resource.ResourceLoader.loaded_texture_runtime.append(texture.pr_texture)
