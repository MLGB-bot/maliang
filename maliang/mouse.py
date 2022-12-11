import pyray as pr
from maliang.units import MouseButtons

class Mouse:
    def __init__(self):
        self.double_click_gap = 0.5   # second
        self.double_click_tsp = 0

    @property
    def mouse_x(self):
        return pr.get_mouse_x()

    @property
    def mouse_y(self):
        return pr.get_mouse_y()

    @property
    def mouse(self):
        ver = pr.get_mouse_position()
        return ver.x, ver.y

    @property
    def delta(self):
        ver = pr.get_mouse_delta()
        return ver.x, ver.y

    @property
    def pmouse_x(self):
        p_mouse = self.pmouse
        return int(p_mouse[0])

    @property
    def pmouse_y(self):
        p_mouse = self.pmouse
        return int(p_mouse[1])

    @property
    def pmouse(self):
        mouse = self.mouse
        delta = self.delta
        return mouse[0] - delta[0], mouse[1] - delta[1]

    @property
    def pressed_buttons(self):
        buttons = []
        for button in MouseButtons.enum():
            if pr.is_mouse_button_down(button):
                buttons.append(button)
        return buttons

    def cursor(self, mode: int):
        pr.show_cursor()
        pr.set_mouse_cursor(mode)

    def no_cursor(self):
        pr.hide_cursor()

    def mouse_position(self, x:int, y:int):
        pr.set_mouse_position(x, y)

    def mouse_scale(self, scalex:float, scaley:float):
        pr.set_mouse_scale(scalex, scaley)

    def mouse_offset(self, offsetx:int, offsety:int):
        pr.set_mouse_offset(offsetx, offsety)

    def is_mouse_pressed(self, button: int):
        return pr.is_mouse_button_down(button)

    def is_mouse_released(self, button: int):
        return pr.is_mouse_button_up(button)

    def is_mouse_clicked(self, button: int):
        return pr.is_mouse_button_pressed(button)

    def event_trigger_on_mouse_moved(self):
        delta = self.delta
        if sum(delta) != 0:
            return True, delta
        return False, None

    def event_trigger_on_mouse_pressed(self):
        buttons = self.pressed_buttons
        return bool(buttons), buttons

    def event_trigger_on_mouse_released(self):
        buttons = []
        for button in MouseButtons.enum():
            if pr.is_mouse_button_released(button):
                buttons.append(button)
        return bool(buttons), buttons

    def event_trigger_on_mouse_clicked(self):
        buttons = []
        for button in MouseButtons.enum():
            if pr.is_mouse_button_pressed(button):
                buttons.append(button)
        return bool(buttons), buttons

    def event_trigger_on_mouse_wheel(self):
        delta = pr.get_mouse_wheel_move()
        return bool(delta), delta

    def event_trigger_on_mouse_dragged(self):
        # pressed + move
        press_status, pressed_buttons = self.event_trigger_on_mouse_pressed()
        if press_status:
            # move
            move_status, move_delta = self.event_trigger_on_mouse_moved()
            if move_status:
                return True, (pressed_buttons, move_delta)
        return False, None

    def event_trigger_on_mouse_double_clicked(self):
        released = pr.is_mouse_button_released(MouseButtons.MOUSE_BUTTON_LEFT)
        if released:
            _now = pr.get_time()
            if (_now - self.double_click_tsp) <= self.double_click_gap:
                self.double_click_tsp = 0
                return True, None
            else:
                self.double_click_tsp = _now
        return False, None


