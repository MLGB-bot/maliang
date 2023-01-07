
class FrameCounter:
    def __init__(self):
        self.base = 1024
        self.nums = []

    def add(self, num, _index=0):
        """
        :param num: must > 0
        :param _index:
        :return:
        """
        if _index == len(self.nums):
            self.nums.append(0)

        self.nums[_index] += num
        if self.nums[_index] > self.base:
            next_num = int(self.nums[_index] / self.base)
            left_num = self.nums[_index] % self.base
            self.nums[_index] = left_num
            self.add(next_num, _index+1)

    @property
    def value(self):
        number = 0
        for _index, num in enumerate(self.nums):
            number += num * (self.base ** _index)
        return number

    def __bool__(self):
        return len(self.nums) > 0

    @property
    def odd_even(self):
        """

        :return:
            None: empty
            0: even
            1: odd
        """
        if self:
            return self.nums[0] % 2


