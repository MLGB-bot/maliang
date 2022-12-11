import os
import pyray as pr
from maliang.units import ResourceLoader
from maliang.structs import MSound, MusicStream, AudioStream


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

    def load_music_stream(self, filename):
        _path = os.path.join(ResourceLoader.static_dir, filename)
        stream = MusicStream()
        stream.pr_stream = pr.load_music_stream(_path)
        return stream

    def init_audio_stream(self, sample_rate: int=44100, sample_size: int=16, channels: int=1):
        """
        现实生活中，声音是时间连续的[模拟信号]。在计算机里,声音需要被采集转化为数字[数字信号]后才能使用。
        :param sample_rate:
            采样频率: 1秒钟"采集声音"的次数. 采样率越高,声音越还原真实,但同时占的资源越多. 常见的采样率有16000HZ、44100HZ
        :param sample_size:
            采样位数: 每次"采集声音"的二进制位数[bit],用以描述声音信号的震动幅度, 常见的采样位数有8/16/24/32bit...
            8bit的位数可以描述256[2**8]种状态，而16bit则可以表示65536[2**16]种状态.
        :param channels:
            音频通道数: 同时有多少通道/设备采集声音. 通道数越多,音质越真实,占的资源越多. 通常为1[单声道]/2[双声道]/n[多声道]

        :extent bit_rate(bps):
            比特率/码率: 即每秒采集的声音信号的计算机大小. 计算公式位:
            bit_rate = sample_rate * sample_size * channels
            bit_rate = 44100 * 16 * 1 (bit/second)
        :return:
        """
        stream = AudioStream()
        stream.pr_stream = pr.load_audio_stream(sample_rate, sample_size, channels)
        return stream