
class GeoHash():
    CharMap = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
                9: '9', 10: 'b', 11: 'c', 12: 'd', 13: 'e', 14: 'f', 15: 'g', 16: 'h', 17: 'j',
                18: 'k', 19: 'm', 20: 'n', 21: 'p', 22: 'q', 23: 'r', 24: 's', 25: 't', 26: 'u',
                27: 'v', 28: 'w', 29: 'x', 30: 'y', 31: 'z'}

    def __init__(self, minx=-90, maxx=90, miny=-180, maxy=180, bitcount=20, bin_step=5):
        self.bitcount = bitcount
        self.bin_step = bin_step

        assert bitcount % self.bin_step == 0

        self.minx = minx
        self.maxx = maxx
        self.miny = miny
        self.maxy = maxy

    def to_binary(self, num, min=None, max=None, degree="x", timer=0):
        if timer >= self.bitcount:
            return []
        if min == None and max == None:
            if degree == 'x':
                min = self.minx
                max = self.maxx
            else:
                min = self.miny
                max = self.maxy
        # 二分
        middle = (min + max) * 0.5
        if num <= middle:
            bin_num = '0'
            max = middle
        else:
            bin_num = '1'
            min = middle
        timer += 1
        return [bin_num] + self.to_binary(num, min, max, degree=degree, timer=timer)

    def to_base32(self, bin_list):
        chars = []
        for index in range(0, len(bin_list), self.bin_step):
            bin_str = ''.join(bin_list[index: index+self.bin_step])
            numer = int(bin_str, 2)
            chars.append(self.CharMap[numer])
        return chars

    def bind_bin_xy(self, bin_x, bin_y):
        bin_list = []
        for _x, _y in zip(bin_x, bin_y):
            bin_list.append(_y)
            bin_list.append(_x)
        return bin_list

    def encode(self, x, y):
        bin_x = self.to_binary(x, degree='x')
        bin_y = self.to_binary(y, degree='y')
        # 2 combine bin_x and bin_y
        bin_list = self.bind_bin_xy(bin_x, bin_y)
        # 3 transfer to base32
        chars = self.to_base32(bin_list)
        return ''.join(chars)

    def i2b(self, number, count):
        return ('{:0'+str(count)+'b}').format(number)

    def neighbors(self, x, y):
        if x < self.minx:
            x = self.minx
        elif x>self.maxx:
            x = self.maxx
        if y < self.miny:
            y = self.miny
        elif y > self.maxy:
            y = self.maxy

        bin_x = self.to_binary(x, degree='x')
        bin_y = self.to_binary(y, degree='y')
        # print(x, y, bin_x, bin_y)
        num_x = int(''.join(bin_x), 2)
        num_y = int(''.join(bin_y), 2)
        # print(num_x, num_y)
        left_bin_x = self.i2b(num_x - 1, self.bitcount) if num_x - 1 > 0 else bin_x
        right_bin_x = self.i2b(num_x + 1, self.bitcount)
        left_bin_y = self.i2b(num_y - 1, self.bitcount) if num_y - 1 > 0 else bin_y
        right_bin_y = self.i2b(num_y + 1, self.bitcount)
        data_list = []
        for _x in (left_bin_x, bin_x, right_bin_x):
            for _y in (left_bin_y, bin_y, right_bin_y):
                bin_list = self.bind_bin_xy(_x, _y)
                # 3 transfer to base32
                chars = self.to_base32(bin_list)
                data_list.append( ''.join(chars))
        return data_list

    # def neighbors_genid(self, gen_id):
    #
    # def loop_neighboors(self, xys, max_looper=3):
    #     looper = 0
    #     while looper < max_looper:
    #         genids = []
    #         for x, y in xys:
    #             ns = self.neighbors(x, y)
    #             genids.extend(ns)
    #         yield looper, genids
    #         xys = genids
    #         looper += 1

    def near(self, x, y, distance):
        # 1 create the minimum bounding rectangle
        min_x = x - distance
        min_y = y - distance
        max_x = x + distance
        max_y = y + distance
        if min_x < self.minx:
            min_x = self.minx
        if max_x > self.maxx:
            max_x = self.maxx
        if min_y < self.miny:
            min_y = self.miny
        if max_y > self.maxy:
            max_y = self.maxy

        # print(min_x, max_x, min_y, max_y)
        # # 2 calc corner genhashs
        left_up_id = self.encode(min_x, min_y)
        right_up_id = self.encode(max_x, min_y)
        left_down_id = self.encode(min_x, max_y)
        right_down_id = self.encode(max_x, max_y)
        print(left_up_id, right_up_id, left_down_id, right_down_id)

        # _y = min_y
        # while True:
        #     # _y 不端相加
        #     if _y > max_y:
        #         break
        #     print("_y: ", _y)
        #     _x = min_x
        #     while True:
        #         if _x > max_x:
        #             print()
        #             break
        #         print(self.encode(_x, _y), end=", ")
        #         _x += 1
        #     _y += 1


if __name__ == '__main__':
    t = GeoHash(bitcount=5, minx=0, maxx=300, miny=0, maxy=300, bin_step=5)
    x = 39.912279
    y = 116.404844
    # i = 0
    # while i < 10:
    #     hashid = t.encode(x+i, y)
    #     print(hashid)
    #     i += 1
    # for i in t.neighbors(x, y):
    #     print(i)
    # for i in t.loop_neighboors([(x, y), ], max_looper=2):
    #     print(i)
    t.near(x, y, distance=10)
    print(t.encode(0, 0))
    print(t.encode(0, 300))
    print(t.encode(300, 0))
    print(t.encode(300, 300))


