import random
from maliang import Maliang

app = Maliang(width=300, height=300, fps=30)
app.set_window_title("Attraction and Repusion")

diagonal = (app.width ** 2 + app.height ** 2) ** 0.5
background_color = (255, 255, 255)


def format_p(px, py, speed=1):
    p = (px ** 2 + py ** 2) ** 0.5
    if p:
        px = px / p * speed
        py = py / p * speed
        return px, py
    else:
        return random.random(), random.random()
