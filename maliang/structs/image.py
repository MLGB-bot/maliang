import pyray as pr
import maliang.structs.color as mod_color
import maliang.structs.texture as mod_texture


class GifPlayer:
    def __init__(self, mimage=None, fps_delay=None, loop=None):
        self.init_params(mimage=mimage, fps_delay=fps_delay, loop=loop)

    def init_params(self, mimage=None, fps_delay=0, loop=0):
        self.mimage = mimage
        self.frame_current_index = None
        self.fps_delay = fps_delay
        self.fps_counter = 0
        self.loop = loop
        self.loop_counter = 0
        if self.mimage:
            self.texture = mod_texture.MTexture()
            self.texture.pr_texture = pr.load_texture_from_image(self.mimage.pr_image)
        else:
            self.texture = None

    def update_gif_texture(self):
        if self.mimage and (self.loop == 0 or self.loop_counter < self.loop):
            self.fps_counter += 1
            if (self.fps_counter >= self.fps_delay):
                if (self.frame_current_index is None):
                    self.frame_current_index = 0
                else:
                    self.frame_current_index += 1
                if self.frame_current_index > self.mimage.frames - 1:
                    self.frame_current_index = 0
                    if self.loop:
                        self.loop_counter += 1
                nextFrameDataOffset = self.mimage.width * self.mimage.height * 4 * self.frame_current_index
                self.texture.update(self.mimage.pr_image.data + nextFrameDataOffset)
                self.fps_counter = 0
            return self.texture
        elif self.texture:
            return self.texture

    def unload(self):
        if self.texture:
            self.texture.unload()

class MImage:
    def __init__(self):
        self.pr_image = None
        self.texture = None
        # gif image player
        self.frames = 1
        self.gif_player = None

    def load_gif_texture(self, gif_player=None):
        if gif_player:
            if not gif_player.mimage:
                gif_player.init_params(
                    mimage=self,
                    fps_delay=gif_player.fps_delay if gif_player.fps_delay is not None else self.gif_player.fps_delay,
                    loop = gif_player.loop if gif_player.loop is not None else self.gif_player.loop,
                )
            return gif_player.update_gif_texture()
        else:
            return self.gif_player.update_gif_texture()

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

    def gen_mipmaps(self, ):  # 计算所提供图像的所有mipmap级别
        pr.image_mipmaps(self.pr_image)

    @decorate_on_image_change
    def dither(self, r_bpp, g_bpp, b_bpp, a_bpp):  # 抖动图像数据至16bpp或更低(Floyd Steinberg抖动)
        pr.image_dither(self.pr_image, r_bpp, g_bpp, b_bpp, a_bpp)

    @decorate_on_image_change
    def flip_vertical(self):  # 垂直翻转图像
        pr.image_flip_vertical(self.pr_image)

    @decorate_on_image_change
    def flip_horizontal(self):  # 水平翻转图像
        pr.image_flip_horizontal(self.pr_image)

    @decorate_on_image_change
    def rotate_cw(self):  # 顺时针旋转图像 90度
        pr.image_rotate_cw(self.pr_image)

    @decorate_on_image_change
    def rotate_ccw(self):  # 逆时针旋转图像 90度
        pr.image_rotate_ccw(self.pr_image)

    @decorate_on_image_change
    def tint(self, *color):  # 修改图像颜色：色调
        pr.image_color_tint(self.pr_image, mod_color.MColor(*color).to_pyray())

    @decorate_on_image_change
    def color_invert(self):  # 修改图像颜色：反转
        pr.image_color_invert(self.pr_image)

    @decorate_on_image_change
    def color_grayscale(self):  # 修改图像颜色：灰度
        pr.image_color_grayscale(self.pr_image)

    @decorate_on_image_change
    def color_contrast(self, contrast: float):  # 修改图像颜色：对比度(-100到100)
        pr.image_color_contrast(self.pr_image, contrast)

    @decorate_on_image_change
    def color_brightness(self, brightness: int):  # 修改图像颜色：亮度(-255到255)
        pr.image_color_brightness(self.pr_image, brightness)

    @decorate_on_image_change
    def color_replace(self, color: mod_color.MColor, replaced_color: mod_color.MColor):  # 修改图像颜色：替换颜色
        pr.image_color_replace(self.pr_image, color.to_pyray(), replaced_color.to_pyray())

    def load_colors(self):  # 将图像中的颜色数据加载为颜色阵列(RGBA-32位)
        pr_colors = pr.load_image_colors(self.pr_image)
        length = self.width * self.height
        data_list = []
        for i in range(length):
            pr_color = pr_colors[i]
            color = mod_color.MColor(pr_color.r, pr_color.g, pr_color.b, pr_color.a)
            data_list.append(color)
        pr.unload_image_colors(pr_colors)
        return data_list

    def load_palette(self, max_palette_size, color_count):  # 从图像 Load调色板作为颜色阵列(RGBA-32位)
        pr_color = pr.load_image_palette(self.pr_image, max_palette_size, color_count)
        color = mod_color.MColor(pr_color.r, pr_color.g, pr_color.b, pr_color.a)
        pr.unload_image_palette(pr_color)
        return color

    def get_alpha_border(self, threshold):  # 获取图像 alpha边框Rectangle
        rect = pr.get_image_alpha_border(self.pr_image, threshold)
        return rect.x, rect.y, rect.width, rect.height

    def get_color(self, x, y):  # 获取(x, y)位置的图像像素颜色
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
