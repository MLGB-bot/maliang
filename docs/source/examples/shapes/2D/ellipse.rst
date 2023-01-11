椭圆(ellipse)
=====================

.. _ellipse.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/shapes/2D/ellipse.py
.. _ellipse_mode.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/shapes/2D/ellipse_mode.py


ellipse()
-----------

::

    ellipse(x: float, y: float, w: float, h:float)

* 参数 ::

        x  椭圆心x坐标
        y  椭圆心y坐标
        w  椭圆宽度
        h  椭圆高度



*  ellipse.py_

.. image:: /_static/examples/shapes/2D/ellipse.png
.. literalinclude:: ../../../../../examples/shapes/2D/ellipse.py
    :language: python
    :linenos:

* 示例 ::

        ellipse(0, 0, 100)
        ellipse(0, 0, 100)
        ellipse(0, 0, 100, stroke_color=(255, 0, 0))
        ellipse(0, 0, 100, stroke_color=None, filled_color=(255, 0, 0), stroke_width=6)

----------------


ellipse_mode()
------------------

椭圆坐标模式

::

    ellipse_mode(mode: int)

.. glossary::

    EllipseMode.CENTER
        ::

            x: 椭圆中心点x坐标
            y: 椭圆中心点y坐标
            w: 椭圆宽
            h: 椭圆高


    EllipseMode.CORNER
        ::

            x: 椭圆外切矩形左上角顶点x坐标
            y: 椭圆外切矩形左上角顶点y坐标
            w: 椭圆宽
            h: 椭圆高


    EllipseMode.RADIUS
        ::

            x: 椭圆中心点x坐标
            y: 椭圆中心点y坐标
            w: 椭圆宽的一半
            h: 椭圆高的一半

    EllipseMode.CORNERS
        ::

            x: 椭圆外切矩形左上角顶点x坐标
            y: 椭圆外切矩形左上角顶点y坐标
            w: 椭圆外切矩形右下角顶点x坐标
            h: 椭圆外切矩形右下角顶点y坐标

        .. attention::
            当mode==EllipseMode.CORNERS时, w和h参数不再代表宽度和高度, 而是椭圆外切矩形的右下角顶点坐标.

* ellipse_mode.py_

.. image:: /_static/examples/shapes/2D/ellipse_mode.png
.. literalinclude:: ../../../../../examples/shapes/2D/ellipse_mode.py
    :language: python
    :linenos:
