
import random
try:
    from .config import app, format_p, diagonal
    from .geohash import GeoHash
except:
    from config import app, format_p, diagonal
    from geohash import GeoHash

class Electron():
    def __init__(self):
        self.size = 1
        self.color = (0, 100, 0, 180)
        self.distance_electron = 10
        self.genhash = GeoHash(minx=0, maxx=app.width, miny=0, maxy=app.height, bitcount=5)

        self.init_random_position()
        self.init_genhash_id()

    def init_random_position(self):
        self.x = random.randint(0, app.width)
        self.y = random.randint(0, app.height)

    def display(self):
        app.point(self.x, self.y, self.size, stroke_color=self.color, shape='circle')

    def init_genhash_id(self):
        self.genhash_id = self.genhash.encode(self.x, self.y)

    def update(self, neutrons, electrons_genhashs):
        min_distance = None
        clostest_neu = None
        for n in neutrons:
            distance = ((self.x - n.x) ** 2 + (self.y - n.y) ** 2) ** 0.5
            if min_distance is None:
                min_distance = distance
                clostest_neu = n
            else:
                if distance < min_distance:
                    min_distance = distance
                    clostest_neu = n
        if clostest_neu is not None:
            if min_distance > clostest_neu.distance_electron:
                px, py = format_p(clostest_neu.x - self.x, clostest_neu.y - self.y, speed=1 - 1 / diagonal * min_distance)
            elif min_distance < clostest_neu.distance_electron:
                px, py = format_p(self.x - clostest_neu.x, self.y - clostest_neu.y, speed=1 - 1 / diagonal * min_distance)
            else:
                px, py = 0, 0
            self.x += px
            self.y += py

        min_e_distance = None
        clostest_ele = None
        # genhash
        for neighboor in self.genhash.neighbors(self.x, self.y):
            if neighboor in electrons_genhashs:
                for e in electrons_genhashs[neighboor]:
                    if e == self:
                        continue
                    distance = ((self.x - e.x) ** 2 + (self.y - e.y) ** 2) ** 0.5
                    if min_e_distance is None:
                        min_e_distance = distance
                        clostest_ele = e
                    else:
                        if distance < min_e_distance:
                            min_e_distance = distance
                            clostest_ele = e

        if clostest_ele is not None and min_e_distance < self.distance_electron:
            px, py = format_p(self.x - clostest_ele.x, self.y - clostest_ele.y, speed=1 - 1 / diagonal * min_e_distance)
            self.x += px
            self.y += py

        if self.x < self.size * 0.5:
            self.x = self.size * 0.5
        elif self.x > app.width - self.size * 0.5:
            self.x = app.width - self.size * 0.5
        if self.y < self.size * 0.5:
            self.y = self.size * 0.5
        elif self.y > app.height - self.size * 0.5:
            self.y = app.height - self.size * 0.5

        # genhash
        def update_genhash_id():
            electrons_genhashs[self.genhash_id].remove(self)
            if not electrons_genhashs[self.genhash_id]:
                del electrons_genhashs[self.genhash_id]
            self.init_genhash_id()
            if self.genhash_id not in electrons_genhashs:
                electrons_genhashs[self.genhash_id] = []
            electrons_genhashs[self.genhash_id].append(self)

        update_genhash_id()