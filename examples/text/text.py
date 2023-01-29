from maliang import Maliang

app = Maliang(width=250, height=200, buffer_proxy=True, fps=0)

text_en = "abcdefg\nhijklmn\nopqrst\nuvwxyz\n,.?!"

def on_draw():
    app.background(255)
    app.text(text_en, 0, 0, text_size=24)
    app.text(text_en, 120, 0, text_color=(255, 0, 0), text_size=24)

app.regist_event("on_draw", on_draw)

app.run()
