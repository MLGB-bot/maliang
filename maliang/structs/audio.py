import pyray as pr


class MSound:
    def __init__(self):
        self.pr_sound = None

    def unload(self):
        if self.pr_sound:
            pr.unload_sound(self.pr_sound)

    def play(self):
        pr.play_sound(self.pr_sound)

    def stop(self):
        pr.stop_sound(self.pr_sound)

    def play_multi(self):
        pr.play_sound_multi(self.pr_sound)

    def stop_multi(self):
        pr.stop_sound_multi()

    def get_multi(self):
        return pr.get_sounds_playing()

    def pause(self):
        pr.pause_sound(self.pr_sound)

    def resume(self):
        pr.resume_sound(self.pr_sound)

    def playing(self):
        return pr.is_sound_playing(self.pr_sound)

    def set_volumn(self, volumn: float):
        pr.set_sound_volume(self.pr_sound, volumn)

    def set_pitch(self, pitch: float):
        pr.set_sound_pitch(self.pr_sound, pitch)

    def set_pan(self, pan: float):
        pr.set_sound_pan(self.pr_sound, pan)

