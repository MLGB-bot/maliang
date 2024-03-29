import pyray as pr
from raylib._raylib_cffi import ffi  # ,lib


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


class MusicStream():
    def __init__(self):
        self.pr_stream = None

    def unload(self):
        pr.unload_music_stream(self.pr_stream)

    def play(self):
        pr.play_music_stream(self.pr_stream)

    def playing(self):
        return pr.is_music_stream_playing(self.pr_stream)

    def stop(self):
        pr.stop_music_stream(self.pr_stream)

    def pause(self):
        pr.pause_music_stream(self.pr_stream)

    def resume(self):
        pr.resume_music_stream(self.pr_stream)

    def seek(self, second: float):
        pr.seek_music_stream(self.pr_stream, second)

    def set_volumn(self, volumn: float):
        pr.set_music_volume(self.pr_stream, volumn)

    def set_pitch(self, pitch: float):
        pr.set_music_pitch(self.pr_stream, pitch)

    def set_pan(self, pan: float):
        pr.set_music_pan(self.pr_stream, pan)

    def update(self):
        pr.update_music_stream(self.pr_stream)

    def get_time_length(self) -> float:
        return pr.get_music_time_length(self.pr_stream)

    def get_time_played(self) -> float:
        return pr.get_music_time_played(self.pr_stream)


AUDIO_STREAM_CALLBACK_WRAPPERS = []


class AudioStream():
    def __init__(self, sample_rate: int=44100, sample_size: int=16, channels: int=1):
        self.pr_stream = None
        self.sample_rate = sample_rate
        self.sample_size = sample_size
        self.channels = channels

    def unload(self):
        pr.unload_audio_stream(self.pr_stream)

    def is_processed(self):
        # Check if any audio stream buffers requires refill
        return pr.is_audio_stream_processed(self.pr_stream)

    def play(self):
        pr.play_audio_stream(self.pr_stream)

    def playing(self):
        return pr.is_audio_stream_playing(self.pr_stream)

    def stop(self):
        pr.stop_audio_stream(self.pr_stream)

    def pause(self):
        pr.pause_audio_stream(self.pr_stream)

    def resume(self):
        pr.resume_audio_stream(self.pr_stream)

    def set_volumn(self, volumn: float):
        pr.set_audio_stream_volume(self.pr_stream, volumn)

    def set_pitch(self, pitch: float):
        pr.set_audio_stream_pitch(self.pr_stream, pitch)

    def set_pan(self, pan: float):
        pr.set_audio_stream_pan(self.pr_stream, pan)

    # def set_default_buffer_size(self, size: int):
    #     pr.set_audio_stream_buffer_size_default(size)

    def set_callback(self, callback, frame_size=0):
        """

        :param callback:
        :param frame_size: byte size every frame.
                    frame_size= channels * sample_size / 8  (bytes)
        :return:
        """
        if not frame_size:
            frame_size = self.channels * self.sample_size / 8

        @ffi.callback("void(*)(void *, unsigned int)")
        def wrap_callback(buffer, frame_count):
            """

            :param buffer: cData void point to buffer
            :param frame_count: how many frames
            :return:
            """
            audio_bytes_data = callback(frame_count)  # generate audio binary data
            buf = ffi.buffer(buffer, frame_count * frame_size)  # create write buffer. (‘cdata’, 'bytes')
            buf[:] = audio_bytes_data  # enrich audio data. can play sound in window

        global AUDIO_STREAM_CALLBACK_WRAPPERS
        AUDIO_STREAM_CALLBACK_WRAPPERS.append(wrap_callback)
        pr.set_audio_stream_callback(self.pr_stream, wrap_callback)
        return

    def attach_processor(self, processor):
        pr.attach_audio_stream_processor(self.pr_stream, processor)

    def detach_processor(self, processor):
        pr.detach_audio_stream_processor(self.pr_stream, processor)

    def update(self, data, frame_count):
        pr.update_audio_stream(self.pr_stream, data, frame_count)
