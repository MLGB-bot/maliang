
class Events(object):
    def __init__(self):
        self.events = {
            'on_setup': None,
            'on_draw': None,
            'on_close': None,
            'on_exit': None,
            # window
            "on_resize": None,
            # mouse
            "on_mouse_clicked": None,
            "on_mouse_released": None,
            "on_mouse_down": None,
            "on_mouse_double_clicked": None,
            "on_mouse_dragged": None,
            "on_mouse_moved": None,
            "on_mouse_wheel": None,
            # keyboard
            "on_key_clicked": None,
            "on_key_released": None,
            "on_key_down": None,
            "on_char_down": None,
        }
        self.events_registed = []
        self.events_not_trigger = ('on_setup', 'on_draw', 'on_close', 'on_exit', 'on_resize')

    def regist_event(self, event_name, func):
        if event_name in self.events:
            setattr(self, event_name, func)

    def unregist_event(self, event_name):
        if event_name in self.events:
            delattr(self, event_name)
            self.events[event_name] = None
        if event_name in self.events_registed:
            self.events_registed.remove(event_name)

    def catpure_events(self):
        # events
        for event_name in self.events_registed:
            if self.events[event_name]:
                trigger_func = f"event_trigger_{event_name}"
                if hasattr(self, trigger_func):
                    trigged, args = getattr(self, trigger_func)()
                    if trigged:
                        if args:
                            self.events[event_name](args)
                        else:
                            self.events[event_name]()

    def refresh_events(self):
        pass

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in self.events:
            self.events[key] = value
            if key not in self.events_not_trigger:
                self.events_registed.append(key)