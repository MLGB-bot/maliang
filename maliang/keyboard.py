import pyray as pr
from collections import deque


class Keyboard:
    def __init__(self):
        self._pressed_keys = deque(maxlen=128)  # 键盘按下的keys
        self.released_keys = []
        self.clicked_keys = []
        self.exit_key = 0
        pr.set_exit_key(0)

    def set_exit_key(self, key: int):
        """
        设置自定义键以退出程序(默认为ESC)
        :param key:
        :return:
        """
        self.exit_key = key

    @property
    def pressed_keys(self):
        return list(self._pressed_keys)

    def _append_key(self, key: int):
        self._pressed_keys.append(key)

    def _delete_key(self, key: int):
        self._pressed_keys.remove(key)

    def keyboard_watcher(self):
        # 1 移除已经松开的key
        released_keys = []
        for _key in self._pressed_keys:
            if not self.is_key_down(_key):
                released_keys.append(_key)
        for _key in released_keys:
            self._delete_key(_key)
        # 2 获取当前按下的key 添加到pressed_keys
        clicked_keys = []
        while True:
            clicked_key = pr.get_key_pressed()
            if clicked_key:
                self._append_key(clicked_key)
                clicked_keys.append(clicked_key)
            else:
                break
        # keys in current loop frame
        self.released_keys = released_keys
        self.clicked_keys = clicked_keys

    def is_key_up(self, key: int):
        return pr.is_key_up(key)

    def is_key_down(self, key:int):
        return pr.is_key_down(key)

    def is_key_clicked(self, key:int):
        return pr.is_key_pressed(key)

    def is_key_released(self, key:int):
        return pr.is_key_released(key)

    def event_trigger_on_key_clicked(self):
        # 如果没有keyboard_watcher
        # key_pressed = pr.get_key_pressed()  #
        # if key_pressed:
        #     return True, key_pressed
        # return False, None
        if self.clicked_keys:
            return True, self.clicked_keys
        return False, None

    def event_trigger_on_key_released(self):
        if self.released_keys:
            return True, self.released_keys
        return False, None

    def event_trigger_on_key_pressed(self):
        # 如果没有keyboard_watcher
        # key_pressed = pr.get_key_pressed()
        # if key_pressed:
        #     return True, key_pressed
        # return False, None
        if self._pressed_keys:
            return True, self.pressed_keys
        return False, None


    def event_trigger_on_char_pressed(self):
        char_pressed = pr.get_char_pressed()
        if char_pressed:
            return True, char_pressed
        return False, None


