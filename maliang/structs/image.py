import pyray as pr
import maliang.structs.color as mod_color
import maliang.structs.texture as mod_texture

class MImage:
    def __init__(self):
        self.pr_image = None
        self.texture = None

    @property
    def width(self):
        return self.pr_image.width

    @property
    def height(self):
        return self.pr_image.height

    @property
    def format(self):
        return self.pr_image.format

    @property
    def mipmaps(self):
        return self.pr_image.mipmaps

    def unload(self):
        if self.pr_image:
            pr.unload_image(self.pr_image)
            self.pr_image = None

    def load_raw(self, image_path, w, h, format, header_size):
        return pr.load_image_raw(image_path, w, h, format, header_size)

    def load_texture(self):
        if self.texture:
            return self.texture
        self.texture = texture = mod_texture.MTexture()
        texture.pr_texture = pr.load_texture_from_image(self.pr_image)
        return texture

    def export_to_file(self, filename, mode=0) -> bool:
        if mode == 0:
            return pr.export_image(self.pr_image, filename)
        else:
            return pr.export_image_as_code(self.pr_image, filename)

    @staticmethod
    def decorate_on_image_change(func):
        def inner(self, *args, **kwargs):
            if self.texture:
                self.texture.unload()
                self.texture = None
            return func(self, *args, **kwargs)

        return inner

    @decorate_on_image_change
    def resize(self, w, h):
        pr.image_resize(self.pr_image, w, h)

    @decorate_on_image_change
    def resize_nn(self, w, h):
        pr.image_resize_nn(self.pr_image, w, h)

    @decorate_on_image_change
    def resize_canvas(self, w, h, offsetx, offsety, fill_color):
        pr.image_resize_canvas(self.pr_image, w, h, offsetx, offsety, mod_color.MColor(*fill_color).to_pyray())

    def copy(self):
        img = MImage()
        img.pr_image = pr.image_copy(self.pr_image)
        return img

    def conv_format(self, format: int):
        pr.image_format(self.pr_image, format)

    @decorate_on_image_change
    def to_pot(self, fill_color):
        pr.image_to_pot(self.pr_image, mod_color.MColor(*fill_color).to_pyray())

    @decorate_on_image_change
    def crop(self, x, y, w, h):
        pr.image_crop(self.pr_image, pr.Rectangle(x, y, w, h))

    @decorate_on_image_change
    def alpha_crop(self, threshold):
        pr.image_alpha_crop(self.pr_image, threshold)

    @decorate_on_image_change
    def alpha_clear(self, color, threshold):
        pr.image_alpha_clear(self.pr_image, mod_color.MColor(*color).to_pyray(), threshold)

    @decorate_on_image_change
    def alpha_mask(self, alpha_mask):
        pr.image_alpha_mask(self.pr_image, alpha_mask.pr_image)

    @decorate_on_image_change
    def alpha_premultiply(self):
        pr.image_alpha_premultiply(self.pr_image)

    def gen_mipmaps(self, ):  # ??????????????????????????????mipmap??????
        pr.image_mipmaps(self.pr_image)

    @decorate_on_image_change
    def dither(self, r_bpp, g_bpp, b_bpp, a_bpp):  # ?????????????????????16bpp?????????(Floyd Steinberg??????)
        pr.image_dither(self.pr_image, r_bpp, g_bpp, b_bpp, a_bpp)

    @decorate_on_image_change
    def flip_vertical(self):  # ??????????????????
        pr.image_flip_vertical(self.pr_image)

    @decorate_on_image_change
    def flip_horizontal(self):  # ??????????????????
        pr.image_flip_horizontal(self.pr_image)

    @decorate_on_image_change
    def rotate_cw(self):  # ????????????????????? 90???
        pr.image_rotate_cw(self.pr_image)

    @decorate_on_image_change
    def rotate_ccw(self):  # ????????????????????? 90???
        pr.image_rotate_ccw(self.pr_image)

    @decorate_on_image_change
    def tint(self, *color):  # ???????????????????????????
        pr.image_color_tint(self.pr_image, mod_color.MColor(*color).to_pyray())

    @decorate_on_image_change
    def color_invert(self):  # ???????????????????????????
        pr.image_color_invert(self.pr_image)

    @decorate_on_image_change
    def color_grayscale(self):  # ???????????????????????????
        pr.image_color_grayscale(self.pr_image)

    @decorate_on_image_change
    def color_contrast(self, contrast: float):  # ??????????????????????????????(-100???100)
        pr.image_color_contrast(self.pr_image, contrast)

    @decorate_on_image_change
    def color_brightness(self, brightness: int):  # ???????????????????????????(-255???255)
        pr.image_color_brightness(self.pr_image, brightness)

    @decorate_on_image_change
    def color_replace(self, color: mod_color.MColor, replaced_color: mod_color.MColor):  # ?????????????????????????????????
        pr.image_color_replace(self.pr_image, color.to_pyray(), replaced_color.to_pyray())

    def load_colors(self):  # ????????????????????????????????????????????????(RGBA-32???)
        pr_colors = pr.load_image_colors(self.pr_image)
        length = self.width * self.height
        data_list = []
        for i in range(length):
            pr_color = pr_colors[i]
            color = mod_color.MColor(pr_color.r, pr_color.g, pr_color.b, pr_color.a)
            data_list.append(color)
        pr.unload_image_colors(pr_colors)
        return data_list

    def load_palette(self, max_palette_size, color_count):  # ????????? Load???????????????????????????(RGBA-32???)
        pr_color = pr.load_image_palette(self.pr_image, max_palette_size, color_count)
        color = mod_color.MColor(pr_color.r, pr_color.g, pr_color.b, pr_color.a)
        pr.unload_image_palette(pr_color)
        return color

    def get_alpha_border(self, threshold):  # ???????????? alpha??????Rectangle
        rect = pr.get_image_alpha_border(self.pr_image, threshold)
        return rect.x, rect.y, rect.width, rect.height

    def get_color(self, x, y):  # ??????(x, y)???????????????????????????
        pr_color = pr.get_image_color(self.pr_image, x, y)
        return mod_color.MColor(pr_color.r, pr_color.g, pr_color.b, pr_color.a)

    def set_color(self, x, y, color: mod_color.MColor):
        return self.draw_pixel(x, y, color)

    # Image drawing functions
    # NOTE: Image software-rendering functions (CPU)
    @decorate_on_image_change
    def clear_background(self, color: mod_color.MColor):  # Clear image background with given color
        pr.image_clear_background(self.pr_image, color.to_pyray())

    @decorate_on_image_change
    def draw_pixel(self, x, y, color: mod_color.MColor):  # Draw pixel within an image
        pr.image_draw_pixel(self.pr_image, x, y, color.to_pyray())

    @decorate_on_image_change
    def draw_line(self, x1, y1, x2, y2, color: mod_color.MColor):  # Draw line within an image
        pr.image_draw_line(self.pr_image, x1, y1, x2, y2, color.to_pyray())

    @decorate_on_image_change
    def draw_circle(self, x, y, r, color: mod_color.MColor):  # Draw circle within an image
        pr.image_draw_circle(self.pr_image, x, y, r, color.to_pyray())

    @decorate_on_image_change
    def draw_rectangle(self, x, y, w, h, color: mod_color.MColor):  # Draw rectangle within an image
        pr.image_draw_rectangle(self.pr_image, x, y, w, h, color.to_pyray())

    @decorate_on_image_change
    def draw_rectangle_lines(self, x, y, w, h, thick, color: mod_color.MColor):  # Draw rectangle lines within an image
        pr.image_draw_rectangle_lines(self.pr_image, pr.Rectangle(x, y, w, h), thick, color.to_pyray())

    @decorate_on_image_change
    def draw(self, x, y, w, h, src_image, src_x, src_y, src_w, src_h,
             tint: mod_color.MColor):  # Draw a source image within a destination image (tint applied to source)
        pr.image_draw(self.pr_image, src_image.pr_image, pr.Rectangle(src_x, src_y, src_w, src_h),
                      pr.Rectangle(x, y, w, h), tint.to_pyray())

    @decorate_on_image_change
    def draw_text(self, x, y, text, fontsize=12, font=None, color: mod_color.MColor = None, space=0):
        if font:
            pr.image_draw_text_ex(self.pr_image, font, text, pr.Vector2(x, y), fontsize, space, color.to_pyray())
        else:
            pr.image_draw_text(self.pr_image, text, x, y, fontsize, color.to_pyray())
