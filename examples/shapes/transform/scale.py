from maliang import Maliang

app = Maliang(400, 400, buffer_proxy=True, )

def on_setup():
    app.background(200)
    app.rect(120, 80, 200, 200)
    app.scale(0.4)
    app.rect(120, 80, 200, 200)

app.regist_event('on_setup', on_setup)
app.run()
