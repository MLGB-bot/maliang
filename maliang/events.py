
class Events:
    def __init__(self):
        self.events = {
            'on_setup': None,
            'on_draw': None,
            'on_exit': None,
            # mouse
            "on_mouse_clicked": None,
            "on_mouse_double_clicked": None,
            "on_mouse_dragged": None,
            "on_mouse_moved": None,
            "on_mouse_pressed": None,
            "on_mouse_released": None,
            "on_mouse_wheel": None,
            # keyboard
            "on_key_clicked": None,
            "on_key_released": None,
            "on_key_pressed": None,
            "on_char_pressed": None,
        }
        self.events_registed = []
        self.events_not_trigger = ('on_setup', 'on_draw', 'on_exit')


    def regist_event(self, event_name, func):
        if event_name in self.events:
            setattr(self, event_name, func)
            self.events[event_name] = func
        if event_name not in self.events_registed and event_name not in self.events_not_trigger:
            self.events_registed.append(event_name)

    def unregist_event(self, event_name):
        if event_name in self.events:
            setattr(self, event_name, None)
            self.events[event_name] = None
        if event_name in self.events_registed and event_name not in self.events_not_trigger:
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


