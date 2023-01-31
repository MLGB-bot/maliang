

class FontEngineDemo():

    @classmethod
    def api_auto_load(cls, _file, filetype='.ttf', fontsize=None) -> any:
        """

        :param _file: font file path
        :param filetype:
        :param fontsize:
        :return:
        """
        anytype_obj = any
        return anytype_obj

    @classmethod
    def api_text_to_image(cls, font, text, font_size=12, text_color=(0, 0, 0, 255), space_x=0, space_y=0):
        """

        :param font: cls.api_auto_load() -> anytype_obj
        :param text:
        :param font_size:
        :param text_color:
        :param space_x:
        :param space_y:
        :return: ".png", b""
        """
        png_data = b""
        '''
        # png_data is same with follow python code
        with open("image.png", 'rb') as f:
            png_data = f.read()
        '''
        return ".png", png_data

    @classmethod
    def api_text(cls, font, text, x, y, font_size=None, text_color=None, space_x=0, space_y=0):
        """

        :param font: cls.api_auto_load() -> anytype_obj
        :param text:
        :param x:
        :param y:
        :param font_size:
        :param text_color:
        :param space_x:
        :param space_y:
        :return: None / raylib.Texture
        """
        # draw text as you wish
