from maliang import Maliang

app = Maliang()


def on_setup():
    print("i am on_setup")

app.regist_event("on_setup", on_setup)

app.run()
