import pyray as pr

class MGlyph:
    def __init__(self):
        self.pr_glyph = None
        self.glyphcount = 0

    def unload(self):
        if self.pr_glyph:
            pr.unload_font_data(self.pr_glyph, self.glyphcount)
            self.pr_font = None

    # def gen_image_atlas(self):
    #     pr.gen_image_font_atlas()


class MFont:
    def __init__(self):
        self.pr_font = None

    def unload(self):
        if self.pr_font:
            pr.unload_font(self.pr_font)
            self.pr_font = None

    def glyph_info(self, code_point):
        glyph = MGlyph()
        glyph.pr_glyph = pr.get_glyph_info(self.pr_font, code_point)
        return glyph