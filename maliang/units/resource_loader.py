import os

class ResourceLoader:
    static_dir = os.path.join(os.getcwd(), "resources")


    def __init__(self):
        pass

    @classmethod
    def set_static_relative_dir(cls, relative_dir):
        cls.static_dir = os.path.join(os.getcwd(), relative_dir)

    @classmethod
    def set_static_absolute_dir(cls, absolute_dir):
        cls.static_dir = absolute_dir

