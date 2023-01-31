from maliang import Maliang

app = Maliang(400, 400, buffer_proxy=True)

def on_setup():
    app.rect(0, 0, 220, 220)
    app.transtate(120, 80)
    app.rect(0, 0, 220, 220)
    app.transtate(56, 56)
    app.rect(0, 0, 220, 220)

app.regist_event('on_setup', on_setup)
app.run()
