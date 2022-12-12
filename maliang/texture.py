import os
import pyray as pr
from maliang.units import ResourceLoader, TextureMode
from maliang.structs import MTexture, MImage


class Texture:
    def __init__(self):
        self._texture_mode = TextureMode.CORNER
        self._tint = False
        self._tint_color = pr.WHITE

    def load_texture(self, filename):
        image_path = os.path.join(ResourceLoader.static_dir, filename)
        texture = MTexture()
        texture.pr_texture = pr.load_texture(image_path)
        return texture

    def load_texture_cubemap(self, image: MImage, layout: int):
        texture = MTexture()
        texture.pr_texture = pr.load_texture_cubemap(image.pr_image, layout)
        return texture

    def from_image(self, image: MImage):
        texture = MTexture()
        texture.pr_texture = pr.load_texture_from_image(image.pr_image)
        return texture

    def texture(self, texture: MTexture):
        """
        to maintain the code way:
            Maliang.mouse_x
            Maliang.mouse_y
            Maliang.point
            Maliang.rect
            Maliang.texture(texture: MTexture).draw_pro(*args, **kwargs)
        :param texture:
        :return:
        """
        return texture
