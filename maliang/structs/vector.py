class MVector():
    def __init__(self, *nums):
        self.__bind = None
        self.__nums = list(nums)

    def bind(self, callback=None):
        self.__bind = callback

    def bind_update(self):
        if not (self.__bind is None):
            self.__bind(self.__nums)

    @property
    def value(self):
        return self.__nums

    @value.setter
    def value(self, nums):
        self.__nums = list(nums)
        self.bind_update()

    @property
    def x(self):
        return self.__nums[0]

    @x.setter
    def x(self, value):
        self.__nums[0] = value
        self.bind_update()

    @property
    def y(self):
        return self.__nums[1]

    @y.setter
    def y(self, value):
        self.__nums[1] = value
        self.bind_update()

    @property
    def z(self):
        return self.__nums[2]

    @z.setter
    def z(self, value):
        self.__nums[2] = value
        self.bind_update()

    def __getitem__(self, item):
        return self.__nums[item]

    def __setitem__(self, key, value):
        self.__nums[key] = value
        self.bind_update()

    def __iter__(self):
        for i in self.__nums:
            yield i

