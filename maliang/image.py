import os
import pyray as pr
from maliang.units import ResourceLoader, ImageMode
from maliang.structs import MColor, MImage, MTexture


class Image():
    def __init__(self):
        self._image_mode = ImageMode.CORNER
        self._tint = False
        self._tint_color = pr.WHITE


    def create_image(self, w: int, h: int, color=(255, 255, 255, 255), color1=(255, 255, 255, 255),
                     color2=(255, 255, 255, 255), density=0, checksx=10, checksy=10, factor=0.5, tile_size=10,
                     style=0, ):
        """
        create image from
        :param w:
        :param h:
        :param color:
        :param color1:
        :param color2:
        :param density:
        :param checksx:
        :param checksy:
        :param factor:
        :param tile_size:
        :param style:
        :return:
        """
        img = MImage()
        if style == 0:
            img.pr_image = pr.gen_image_color(w, h, MColor(*color).to_pyray())
        elif style == 1:
            img.pr_image = pr.gen_image_gradient_v(w, h, MColor(*color1).to_pyray(), MColor(*color2).to_pyray())
        elif style == 2:
            img.pr_image = pr.gen_image_gradient_h(w, h, MColor(*color1).to_pyray(), MColor(*color2).to_pyray())
        elif style == 3:
            img.pr_image = pr.gen_image_gradient_radial(w, h, density, MColor(*color1).to_pyray(),
                                                      MColor(*color2).to_pyray())
        elif style == 4:
            assert checksx > 0
            assert checksy > 0
            img.pr_image = pr.gen_image_checked(w, h, checksx, checksy, MColor(*color1).to_pyray(),
                                              MColor(*color2).to_pyray())
        elif style == 5:
            img.pr_image = pr.gen_image_white_noise(w, h, factor)
        elif style == 6:
            img.pr_image = pr.gen_image_cellular(w, h, tile_size)
        else:
            img.pr_image = pr.gen_image_color(w, h, color)
        return img

    def image_mode(self, mode):
        assert isinstance(mode, (str, int))
        if isinstance(mode, str):
            assert hasattr(ImageMode, mode)
            self._image_mode = getattr(ImageMode, mode)
        elif isinstance(mode, int):
            assert mode in ImageMode.__values__
            self._image_mode = mode

    def load_image(self, filename):
        image_path = os.path.join(ResourceLoader.static_dir, filename)
        img = MImage()
        img.pr_image = pr.load_image(image_path)
        return img

    def load_screen(self):
        img = MImage()
        img.pr_image = pr.load_image_from_screen()
        # print(img.pr_image.width, img.pr_image.height, img.pr_image.data)
        return img

    def load_raw(self, filename, w, h, format, header_size):
        """
        加载.raw格式的图片数据
        :param filename:
        :param w:
        :param h:
        :param format:
        :param header_size:
        :return:
        """
        image_path = os.path.join(ResourceLoader.static_dir, filename)
        img = MImage()
        img.pr_image = pr.load_image_raw(image_path, w, h, format, header_size)
        return img

    def load_gif(self, filename, frames):
        image_path = os.path.join(ResourceLoader.static_dir, filename)
        img = MImage()
        img.pr_image = pr.load_image_anim(image_path, frames)
        return img

    def load_image_data(self, data, filetype='.png'):
        img = MImage()
        img.pr_image = pr.load_image_from_memory(filetype, data, len(data))
        return img

    def from_texture(self, texture: MTexture):
        img = MImage()
        img.pr_image = pr.load_image_from_texture(texture.pr_texture)
        return img

    def from_image(self, image: MImage, x, y, w, h):
        img = MImage()
        img.pr_image = pr.image_from_image(image.pr_image, pr.Rectangle(x, y, w, h))
        return img

    def copy_image(self, image: MImage):
        return image.copy()

    def tint(self, *color):
        color = MColor(*color)
        self._tint_color = tuple(color)
        self._tint = True

    def no_tint(self):
        self._tint = False

    def init_tint_color(self, tint_color):
        if self._tint:
            return tint_color or self._tint_color
        return pr.WHITE

    def image(self, img: MImage, x: int, y: int, w=0, h=0, tint_color=None, mode=None):
        if img.pr_image:
            tint_color = self.init_tint_color(tint_color)
            w = w or img.pr_image.width
            h = h or img.pr_image.height
            mode = mode or self._image_mode

            def init_mode(_mode):
                if _mode == ImageMode.CORNER:
                    return x, y, w, h
                elif _mode == ImageMode.CENTER:
                    return int(x - w * 0.5), int(y - h * 0.5), w, h
                elif _mode == ImageMode.RADIUS:
                    return x - w, y - h, 2 * w, 2 * h
                elif _mode == ImageMode.CORNERS:
                    return min(x, w), min(y, h), abs(x - w), abs(y - h)
                else:
                    return x, y, w, h

            _x, _y, _w, _h = init_mode(mode)
            texture = img.load_texture()
            texture.draw_pro(_x, _y, _w, _h, tint=MColor(*tint_color).to_pyray())
