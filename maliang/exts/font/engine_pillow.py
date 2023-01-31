"""
# pip install Pillow

"""
import pyray as pr
from PIL import ImageDraw, Image, ImageFont
import math
from io import BytesIO


class FontEnginePillow():

    @classmethod
    def api_auto_load(cls, _file, filetype, fontsize) -> ImageFont.ImageFont|ImageFont.FreeTypeFont:
        if _file:
            if filetype in ('.ttf', '.ttc', 'freetype', 'truetype') and fontsize:
                pil_obj = ImageFont.truetype(_file, fontsize)
            else:
                pil_obj = ImageFont.load(_file)
        else:
            pil_obj = ImageFont.load_default()
        return pil_obj

    @classmethod
    def api_text_to_image(cls, font: ImageFont.ImageFont|ImageFont.FreeTypeFont, text, text_size=12, text_color=(0, 0, 0, 255), space_x=0, space_y=0):
        pil_img = cls._generate_text_image(font, text, text_size, text_color, space_x, space_y)
        png_data = cls._to_pic(pil_img, 'PNG')
        del pil_img
        return ".png", png_data

    @classmethod
    def api_text(cls, font: ImageFont.ImageFont|ImageFont.FreeTypeFont, text, x, y, text_size=None, text_color=None, space_x=0, space_y=0):
        img_format, img_data = cls.api_text_to_image(font, text, text_size=text_size,
                                                                  text_color=text_color, space_x=space_x, space_y=space_y)
        image = pr.load_image_from_memory(img_format, img_data, len(img_data))
        texture = pr.load_texture_from_image(image)
        pr.draw_texture(texture, x, y, pr.WHITE)
        pr.unload_image(image)
        return texture

    @classmethod
    def _generate_text_image(cls, font: ImageFont.ImageFont|ImageFont.FreeTypeFont, text, text_size=12, text_color=(0, 0, 0, 255), space_x=0, space_y=0):
        left, top, right, bottom = font.getbbox(text)
        width, height = right - left, bottom - top

        line_count = text.count("\n")
        max_sides = (
            max(width + left * (1 + line_count), height + left * (1 + line_count)),
            max(width + top * (1 + line_count), height + left * (1 + line_count)),
        )
        im = Image.new("RGBA", max_sides)
        draw = ImageDraw.Draw(im)
        # 裁剪字体
        if line_count:
            draw.multiline_text(
                xy=(0, 0),
                text=text,
                fill=text_color,
                font=font,
                spacing=space_y,
            )
            text_box = draw.multiline_textbbox(
                xy=(0, 0),
                text=text,
                font=font,
                spacing=space_y,
            )
            im2 = im.crop(text_box)
        else:
            draw.text(
                xy=(0, 0),
                text=text,
                fill=text_color,
                font=font,
                spacing=space_y,
                align="left",
            )
            # textlength = draw.textlength(
            #     text=text,
            #     font=font,
            #     direction=None,
            #     features=None,
            #     language=None,
            #     embedded_color=False,
            # )
            im2 = im.crop((left, top, right, bottom))

        if isinstance(font,  ImageFont.FreeTypeFont):
            raw_text_size = font.size
            scale_rate = text_size / raw_text_size
            im3 = im2.resize((math.floor(im2.width * scale_rate), math.floor(im2.height * scale_rate)), )
            del im2
            return im3
        else:
            # bitmap font pillow not support scale
            return im2

    @classmethod
    def _to_pic(cls, img, format='PNG'):
        output = BytesIO()
        img.save(output, format=format)
        return output.getvalue()
