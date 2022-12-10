import os
import pyray as pr
from maliang.units import ResourceLoader
from maliang.structs import MSound


class Audio:
    def __init__(self):
        pass

    def init_audio_device(self):
        pr.init_audio_device()

    def close_audio_device(self):
        pr.close_audio_device()

    def is_audio_device_ready(self):
        return pr.is_audio_device_ready()

    def set_audio_device_master_volumn(self, volumn: float):
        pr.set_master_volume(volumn)

    def load_sound(self, filename):
        _path = os.path.join(ResourceLoader.static_dir, filename)
        sound = MSound()
        sound.pr_sound = pr.load_sound(_path)
        return sound

