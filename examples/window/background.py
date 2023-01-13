from maliang import Maliang

app = Maliang()

def on_setup():
    app.background(255, 50, 0, 255)

app.regist_event("on_setup", on_setup)

app.run()