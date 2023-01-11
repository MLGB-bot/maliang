矩形(rect)
=====================

.. _rect.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/shapes/2D/rect.py
.. _rect_rounded.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/shapes/2D/rect_rounded.py
.. _rect_gradient.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/shapes/2D/rect_gradient.py
.. _rect_mode.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/shapes/2D/rect_mode.py


rect()
-----------

::

    rect(x: float, y: float, w: float, h: float)


* 参数 ::

        x  矩形顶点x坐标(默认左上角)
        y  矩形顶点y坐标(默认左上角)
        w  矩形的宽(默认)
        h  矩形的高(默认)



* rect.py_

.. image:: /_static/examples/shapes/2D/rect.png
.. literalinclude:: ../../../../../examples/shapes/2D/rect.py
    :language: python
    :linenos:

* 示例 ::

        rect(0, 0, 100, 100)
        rect(0, 0, 100, 100, stroke_width=4)
        rect(0, 0, 100, 100, stroke_color=(255, 0, 0))
        rect(0, 0, 100, 100, stroke_width=2, stroke_color=(255, 0, 0), filled_color=None)

----------

rect_rounded()
--------------------
圆角矩形

::

    rect_rounded(x: float, y: float, w: float, h: float, roundness: float, segments: int=30)


* 参数 ::

        x  同rect()
        y  同rect()
        w  同rect()
        h  同rect()
        roundness  弧度的比例, 介于[0, 1]之间的小数
        segments  每个圆弧由多少小段组成, 数字越大,越圆润, 同时需要的计算资源越多, 默认30


* rect_rounded.py_

.. image:: /_static/examples/shapes/2D/rect_rounded.png
.. literalinclude:: ../../../../../examples/shapes/2D/rect_rounded.py
    :language: python
    :linenos:

* 示例 ::

        rect_rounded(0, 0, 100, 100)
        rect_rounded(0, 0, 100, 100, stroke_width=4)
        rect_rounded(0, 0, 100, 100, stroke_color=(255, 0, 0))
        rect_rounded(0, 0, 100, 100, stroke_width=2, stroke_color=(255, 0, 0), filled_color=None)

----------------

rect_gradient()
--------------------

渐变矩形

::

    rect_gradient(x:float, y:float, w:float, h:float, colors: tuple|list, direction: str="xy")

.. attention::
   stroke_width, stroke_color, filled_color 这三个属性对当前方法无效

* 参数 ::

        x  同rect()
        y  同rect()
        w  同rect()
        h  同rect()
        direction <见下方>
        colors

.. glossary::

    direction = "xy"
        ::

            colors =[
                color1: 左上角颜色(left-up),
                color2: 左下角颜色(left-down),
                color3: 右下角颜色(right-down),
                color4: 右上角颜色(right-up),
            ]

    direction = "x"
        ::

            colors =[
                color1: 左颜色(left),
                color2: 右颜色(right),
            ]

    direction = "Y"
        ::

            colors =[
                color1: 上方颜色(up),
                color2: 下方颜色(down),
            ]


* rect_gradient.py_

.. image:: /_static/examples/shapes/2D/rect_gradient.png
.. literalinclude:: ../../../../../examples/shapes/2D/rect_gradient.py
    :language: python
    :linenos:

------------------------

rect_mode()
------------------

矩形坐标模式

::

    rect_mode(mode: int)

.. glossary::

    RectMode.CORNER
        ::

            x: 矩形左上角顶点x坐标
            y: 矩形左上角顶点y坐标
            w: 矩形宽
            h: 矩形高

    RectMode.CENTER
        ::

            x: 矩形中心点x坐标
            y: 矩形中心点y坐标
            w: 矩形宽
            h: 矩形高

    RectMode.RADIUS
        ::

            x: 矩形中心点x坐标
            y: 矩形中心点y坐标
            w: 矩形宽的一半
            h: 矩形高的一半

    RectMode.CORNERS
        ::

            x: 矩形左上角顶点x坐标
            y: 矩形左上角顶点y坐标
            w: 矩形右下角顶点x坐标
            h: 矩形右下角顶点y坐标

    .. attention::
        当mode==RectMode.CORNERS时, w和h参数不再代表矩形的宽度和高度, 而是矩形右下角顶点坐标.


* rect_mode.py_

.. image:: /_static/examples/shapes/2D/rect_mode.png
.. literalinclude:: ../../../../../examples/shapes/2D/rect_mode.py
    :language: python
    :linenos:
