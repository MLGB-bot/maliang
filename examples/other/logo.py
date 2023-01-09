from maliang import Maliang

app = Maliang(width=300, height=300, fps=0, title="Logo")


def on_setup():
    r = 40

    space_x = int(app.width / (r*0.5))
    space_y = int(app.height /(r*0.5*3/4))
    stroke_width = int(app.width / r)

    background = [0] * 3
    stroke_color = [255] * 3
    background, stroke_color = stroke_color, background

    app.no_loop()
    app.background(*background)

    app.stroke((*stroke_color, 50), width=1)

    app.rect(0, 0, app.width, app.height, stroke_width=stroke_width, filled_color=None, stroke_color=stroke_color)
    app.line(0, 0, app.width, app.height)
    app.line(0, app.height, app.width, 0)
    app.line(0, app.height / 2, app.width, app.height / 2)
    app.line(app.width / 2, 0, app.width / 2, app.height)

    app.stroke((*stroke_color, 255), width=stroke_width)

    def ma():
        startx = space_x * 1
        starty = space_y * 2
        points = []
        points.append((startx, starty))  # 0
        points.append((app.width / 2 - 2 * startx, points[0][1]))  # 1
        points.append((points[1][0] , app.height / 2.1))  # 2
        points.append((startx + startx, points[0][1]))  # 3
        points.append((points[3][0], points[2][1]))  # 4
        points.append((app.width / 2 - startx, points[4][1]))  # 5
        points.append((points[5][0], app.height - starty / 2))  # 6
        points.append((points[6][0] - space_x, points[6][1] - space_x))  # 7
        middle_56 = (points[6][1] - points[5][1]) * 0.5 + points[5][1]
        points.append((points[0][0], middle_56))  # 8
        points.append((points[5][0], middle_56))  # 9
        app.line(*points[0], *points[1])
        app.line(*points[1], *points[2])
        app.line(*points[3], *points[4])
        app.line(*points[4], *points[5])
        app.line(*points[5], *points[6])
        app.line(*points[6], *points[7])
        app.line(*points[8], *points[9])

        for point in points:
            app.point(*point, )
            # app.rect(*point, stroke_width, stroke_width)
        # for point in points:
        #     app.circle(*point, diam=stroke_width*2, stroke_width=1, filled_color=None)

    def liang():
        startx = app.width / 2
        starty = space_y
        points = []
        points.append((startx / 2 * 3, starty))  # 0
        points.append((startx + space_x, starty * 2))  # 1
        points.append((app.width - space_x, points[1][1]))  # 2
        points.append((points[2][0], app.height / 2.1))  # 3
        middle_34 = (points[3][1] - points[2][1]) * 0.5 + points[2][1]
        points.append((points[1][0], middle_34))  # 4
        points.append((points[2][0], middle_34))  # 5
        points.append((points[1][0], points[3][1]))  # 6
        points.append((points[2][0], points[3][1]))  # 7
        points.append((points[1][0], app.height - starty))  # 8
        points.append((points[1][0] + space_x, points[8][1] - space_x))  # 9
        points.append((points[2][0], points[8][1]))  # 10
        points.append(((points[2][0] - points[1][0]) * 0.5 + points[1][0],
                       (app.height - starty - points[3][1]) * 0.5 + points[3][1]))  # 11
        points.append((points[11][0] + space_x * 2, points[11][1] - space_x * 2,))  # 12

        app.ellipse(*points[0], stroke_width, stroke_width, filled_color=stroke_color)
        app.circle(*points[0], stroke_width * 2, filled_color=None, stroke_width=1)
        app.line(*points[1], *points[2])
        app.line(*points[2], *points[3])
        app.line(*points[4], *points[5])
        app.line(*points[6], *points[7])
        app.line(*points[1], *points[8])
        app.line(*points[8], *points[9])
        app.line(*points[11], *points[12])
        app.line(*points[6], *points[10])
        for point in points:
            app.point(*point)
        # for point in points:
        #     app.circle(*point, diam=stroke_width*2, stroke_width=1, filled_color=None)
    ma()
    liang()

app.regist_event('on_setup', on_setup)
app.run()
