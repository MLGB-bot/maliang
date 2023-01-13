from maliang import Maliang

app = Maliang()


def on_setup():
    print("window width: ", app.width)  # window width:  100

app.regist_event("on_setup", on_setup)

app.run()
