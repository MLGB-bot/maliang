import random
try:
    from .config import app, format_p, diagonal
    from .geohash import GeoHash
except:
    from config import app, format_p, diagonal
    from geohash import GeoHash

class Neutron():
    def __init__(self):
        # colors
        self.color = (180, 0, 0, 200)
        self.size = 6
        self.init_random_position()
        self.distance_neutron = 100
        self.distance_electron = 80
        self.sides_distance_ratio = random.randint(1, 5)
        # self.genhash = GeoHash(minx=0, maxx=app.width, miny=0, maxy=app.height, bitcount=5)
        # self.init_genhash_id()

    # 1 init random cells
    def init_random_position(self):
        self.x = random.randint(0, app.width)
        self.y = random.randint(0, app.height)

    # def init_genhash_id(self):
    #     self.genhash_id = self.genhash.encode(self.x, self.y)

    def display(self):
        app.circle(self.x, self.y, self.size, filled_color=self.color)

    def update(self, neutrons):
        min_distance = None
        clostest_neu = None
        for n in neutrons:
            if n == self:
                continue
            distance = ((self.x - n.x) ** 2 + (self.y - n.y) ** 2) ** 0.5
            if min_distance is None:
                min_distance = distance
                clostest_neu = n
            else:
                if distance < min_distance:
                    min_distance = distance
                    clostest_neu = n
        if clostest_neu is not None and (min_distance < self.distance_neutron):
            px, py = format_p(self.x - clostest_neu.x, self.y - clostest_neu.y, speed=1-1/diagonal * min_distance)
            self.x += px
            self.y += py
            if self.x < self.size * self.sides_distance_ratio:
                self.x = self.size * self.sides_distance_ratio
            elif self.x > app.width - self.size * self.sides_distance_ratio:
                self.x = app.width - self.size * self.sides_distance_ratio
            if self.y < self.size * self.sides_distance_ratio:
                self.y = self.size * self.sides_distance_ratio
            elif self.y > app.height - self.size * self.sides_distance_ratio:
                self.y = app.height - self.size * self.sides_distance_ratio

