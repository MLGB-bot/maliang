import pyray as pr
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