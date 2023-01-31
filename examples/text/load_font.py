from maliang import Maliang

app = Maliang(width=500, height=400)
app.set_static_relative_dir('../resources/')
font = app.load_font(filename="fonts/LXGWWenKaiLite-Regular.ttf", )

text = "How are you?\nI am Fine, thank you! and you?\n" \
       "落霞与孤鹜齐飞\n秋水共长天一色"
text_img = app.text_image(text, font_size=24, font=font, text_color=(255, 0, 0))

def on_draw():
    app.background(255)
    app.text(text, 0, 0, font_size=12)
    app.text(text, 0, 90, font_size=18, font=font)
    app.image(text_img, 0, 220, )

def on_exit():
    text_img.unload()
    text_img.unload_texture()

app.regist_event("on_draw", on_draw)
app.regist_event("on_exit", on_exit)

app.run()
