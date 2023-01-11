圆(circle)
=====================

.. _circle.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/shapes/2D/circle.py
.. _circle_gradient.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/shapes/2D/circle_gradient.py
.. _circle_mode.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/shapes/2D/circle_mode.py


circle()
-----------

::

    circle(x: float, y: float, diam: float)


* 参数 ::

        x  圆心x坐标
        y  圆心y坐标
        diam  圆直径


* circle.py_

.. image:: /_static/examples/shapes/2D/circle.png
.. literalinclude:: ../../../../../examples/shapes/2D/circle.py
    :language: python
    :linenos:

* 示例 ::

        circle(0, 0, 100)
        circle(0, 0, 100, stroke_width=4)
        circle(0, 0, 100, stroke_color=(255, 0, 0))
        circle(0, 0, 100, stroke_width=2, stroke_color=None, filled_color=(255, 0, 0))


----------------

circle_gradient()
--------------------

渐变圆

::

    circle_gradient(x:float, y:float, diam: float, colors: tuple|list)

.. attention::
   stroke_width, stroke_color, filled_color 这三个属性对当前方法无效

* 参数 ::

        x  同circle()
        y  同circle()
        diam  同circle()
        colors: [
                color1: 圆心颜色(inside),
                color2: 圆边缘颜色(outside)
            ]

* circle_gradient.py_

.. image:: /_static/examples/shapes/2D/circle_gradient.png
.. literalinclude:: ../../../../../examples/shapes/2D/circle_gradient.py
    :language: python
    :linenos:

------------------------

circle_mode()
------------------

圆坐标模式

::

    circle_mode(mode: int)


.. glossary::

    CircleMode.CENTER
        ::

            x: 圆中心点x坐标
            y: 圆中心点y坐标
            w: 圆宽
            h: 圆高


    CircleMode.CORNER
        ::

            x: 圆左上角顶点x坐标
            y: 圆左上角顶点y坐标
            w: 圆宽
            h: 圆高



    CircleMode.RADIUS
        ::

            x: 圆中心点x坐标
            y: 圆中心点y坐标
            w: 圆宽的一半
            h: 圆高的一半


* circle_mode.py_

.. image:: /_static/examples/shapes/2D/circle_mode.png
.. literalinclude:: ../../../../../examples/shapes/2D/circle_mode.py
    :language: python
    :linenos:
