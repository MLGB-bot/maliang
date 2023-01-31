from maliang import Maliang

app = Maliang(width=250, height=200, fps=0)

text_en = "abcdefg\nhijklmn\nopqrst\nuvwxyz\n,.?!"
# text_en = "abcdefgnhijklmn"

img = app.text_image(text_en, font_size=20, text_color=(255, 0, 0), space_x=1)

def on_draw():
    app.background(255)
    app.image(img, 0, 0)
    # app.image(img, 50, 50)
    # if "\n" in text_en:
    #     app.text(text_en, 120, 0, text_color=(255, 0, 0), font_size=20, space_x=1)
    # else:
    #     app.text(text_en, 0, 50, text_color=(255, 0, 0), font_size=20, space_x=1)

def on_exit():
    img.unload()
    img.unload_texture()

app.regist_event("on_draw", on_draw)
app.regist_event("on_exit", on_exit)

app.run()