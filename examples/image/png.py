from maliang import Maliang


app = Maliang(width=500, height=400)
app.set_static_relative_dir('../resources/')

logo = app.load_image('img/logo_300x250.png')

def on_draw():
    app.background(255)
    app.image(logo, 0, 0, )
    app.image(logo, 310, 10, 180, 100)
    app.image(logo, 310, 120, 180, 100, tint_color=(255, 100))
    app.image(logo, 310, 230, 180, 100, tint_color=(255, 0, 0))

def on_exit():
    logo.unload()
    if logo.texture:
        logo.texture.unload()

app.regist_event('on_draw', on_draw)
app.regist_event('on_exit', on_exit)
app.run()