try:
    from PIL import ImageDraw, Image, ImageFont
except:
    pass
import math


class FontEnginePillow():

    @classmethod
    def load_truetype(cls, _file, font_size):
        return ImageFont.truetype(_file, size=font_size)

    @classmethod
    def load_(cls, _file):
        return ImageFont.load(_file)

    @classmethod
    def load_default(cls, ):
        return ImageFont.load_default()

    @classmethod
    def auto_load(cls, _file, filetype, font_size):
        if _file:
            if filetype in ('.ttf', '.ttc', 'freetype', 'truetype') and font_size:
                pil_obj = FontEnginePillow.load_truetype(_file, font_size)
            else:
                pil_obj = FontEnginePillow.load_(_file)
        else:
            pil_obj = FontEnginePillow.load_default()
        return pil_obj

    @classmethod
    def generate_pillow_text_image(cls, font: ImageFont.ImageFont|ImageFont.FreeTypeFont, text, text_size=12, text_color=(0, 0, 0, 255), space_x=0, space_y=0):
        # print(font)  # PIL.ImageFont.ImageFont / PIL.ImageFont.FreeTypeFont
        left, top, right, bottom = font.getbbox(text)
        width, height = right - left, bottom - top
        # print(left, top, right, bottom, '=', width, height)

        line_count = text.count("\n")
        max_sides = (
            max(width + left * (1 + line_count), height + left * (1 + line_count)),
            max(width + top * (1 + line_count), height + left * (1 + line_count)),
        )
        # print(max_sides)
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
            # print(text_box)
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
            # print(textlength)
            im2 = im.crop((left, top, right, bottom))

        if isinstance(font,  ImageFont.FreeTypeFont):
            raw_text_size = font.size
            scale_rate = text_size / raw_text_size
            im3 = im2.resize((math.floor(im2.width * scale_rate), math.floor(im2.height * scale_rate)), )
            del im2
            return im3
        else:
            # bitmap font pillow not support scale
            # scale_rate = 3
            # print(font, font.font)
            # im3 = im2.resize((math.floor(im2.width * scale_rate), math.floor(im2.height * scale_rate)) )
            # del im2
            # return im3
            return im2

