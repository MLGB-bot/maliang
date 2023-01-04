"""

"""

import random
from maliang import Maliang

app = Maliang(width=300, height=300, fps=30)
app.set_window_title("Attraction and Repusion")

background_color = (255, 255, 255)
neutrons = []
electrons = []

diagonal = (app.width ** 2 + app.height ** 2) ** 0.5


def format_p(px, py, speed=1):
    p = (px ** 2 + py ** 2) ** 0.5
    if p:
        px = px / p * speed
        py = py / p * speed
        return px, py
    else:
        return random.random(), random.random()


class Neutron():
    def __init__(self):
        # colors
        self.color = (200, 0, 0, 255)
        self.size = 6
        self.init_random_position()
        self.distance_neutron = 100
        self.distance_electron = 80
        self.sides_distance_ratio = random.randint(1, 10)

    # 1 init random cells
    def init_random_position(self):
        self.x = random.randint(0, app.width)
        self.y = random.randint(0, app.height)

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


class Electron():
    def __init__(self):
        self.size = 1
        self.color = (0, 100, 0, 255)
        self.init_random_position()
        self.distance_electron = 10

    def init_random_position(self):
        self.x = random.randint(0, app.width)
        self.y = random.randint(0, app.height)

    def display(self):
        app.point(self.x, self.y, self.size, stroke_color=self.color, shape='circle')

    def update(self, neutrons, electrons):
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
        for e in electrons:
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

def on_setup():
    app.no_stroke()
    app.smooth()
    global neutrons, electrons
    for _ in range(50):
        neutrons.append(Neutron())

    for _ in range(1000):
        electrons.append(Electron())


def on_draw():
    app.background(*background_color)
    for i in neutrons:
        i.update(neutrons)
        i.display()
    for j in electrons:
        j.update(neutrons, electrons)
        j.display()


app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)
app.loop()
