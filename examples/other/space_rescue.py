"""
"""

import random
from types import NoneType
import maliang
from maliang import Maliang

app = Maliang(width=280, height=320, fps=30)
app.set_window_title("Space Rescue")
app.smooth()


class Alien():
    def __init__(self):
        self.size = 6
        self.color = (255, 100, 100, 255)
        self.catcher = None

    def init_position(self):
        self.x = random.randint(int(0 + self.size), int(app.width - self.size))
        self.y = random.randint(int(0 + self.size), int(app.height - self.size))

    def display(self):
        if self.catcher is None:
            app.circle(self.x, self.y, self.size, filled_color=self.color)
        elif isinstance(self.catcher, Bullet):
            self.x = self.catcher.x
            self.y = self.catcher.y
            app.circle(self.x, self.y, self.size, filled_color=self.color)
            # 如果带到飞船处 胜利
            if app.check_collision_circles(
                    self.x, self.y, self.size,
                    ship.x, ship.y, ship.size,
            ):
                self.catcher = ship
        elif isinstance(self.catcher, SpaceShip):
            self.x = self.catcher.x
            self.y = self.catcher.y
            app.circle(self.x, self.y, self.size, filled_color=self.color)


class Bullet():
    def __init__(self, x, y, px, py, speed=1):
        self.size = 4
        self.color = (0, 0, 0, 255)
        self.x = x
        self.y = y
        self.px = px
        self.py = py
        self.speed = speed
        self.touch_side = False

    def format_p(self):
        p = (self.px ** 2 + self.py ** 2) ** 0.5
        self.px = self.px / p * self.speed
        self.py = self.py / p * self.speed

    def update(self):
        self.x += self.px
        self.y += self.py
        if self.x >= (app.width - self.size * 0.5):
            self.px *= -1
            self.touch_side = True
        elif self.x <= 0:
            self.px *= -1
            self.touch_side = True
        if self.y >= (app.height - self.size * 0.5):
            self.py *= -1
            self.touch_side = True
        elif self.y <= 0:
            self.py *= -1
            self.touch_side = True

    def display(self):
        app.circle(self.x, self.y, self.size, filled_color=self.color)


tmp_bullet = None

class SpaceShip():
    def __init__(self):
        self.x = app.width / 2
        self.y = app.height /2
        self.size = 10
        self.color = (20, 20, 20, 255)
        self.max_bullets = 10
        self.bullets = []

    def shoot(self):
        pass

    def display(self):
        global tmp_bullet
        if tmp_bullet and app.is_mouse_released():
            tmp_bullet.format_p()
            self.bullets.append(tmp_bullet)

        if app.is_mouse_down(0) and len(self.bullets) < self.max_bullets \
                    and (self.x - app.mouse_x) ** 2 + (self.y - app.mouse_y) ** 2 <= 5000:
            # app.triangle(self.x - self.size * 0.5, self.y, self.x + self.size * 0.5, self.y,
            #              # 2 * self.x - app.mouse_x, 2 * self.y - app.mouse_y,
            #              app.mouse_x, app.mouse_y,
            #              filled_color=(255, 200))
            app.line(self.x, self.y, app.mouse_x, app.mouse_y, stroke_width=1, stroke_color=(255, ))
            # draw bullet
            tmp_bullet = Bullet(
                # 2 * self.x - app.mouse_x, 2 * self.y - app.mouse_y,
                app.mouse_x, app.mouse_y,
                self.x-app.mouse_x, self.y-app.mouse_y, speed=10)
            tmp_bullet.display()
        else:
            tmp_bullet = None
        # print(tmp_bullet)
        app.circle(self.x, self.y, self.size, filled_color=self.color)


    def display_bullets(self):
        for bullet in self.bullets:
            bullet.update()
            bullet.display()

            if isinstance(alien.catcher, (Bullet, NoneType)):
                if bullet.touch_side and \
                        app.check_collision_circles(bullet.x, bullet.y, bullet.size,
                                                    alien.x, alien.y, alien.size):
                    alien.catcher = bullet

alien = Alien()
ship = SpaceShip()

background_color = (235,)

def new_game():
    alien.catcher = None
    alien.init_position()
    ship.bullets = []


def on_setup():
    app.no_stroke()
    new_game()


def on_draw():
    # if app.is_mouse_clicked():
    #     on_mouse_clicked()
    if app.is_key_clicked(maliang.KeyboardKeys.KEY_R):
        new_game()
    app.background(*background_color)
    ship.display()
    ship.display_bullets()
    alien.display()


app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)
app.run()
