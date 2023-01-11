点(point)
=====================

.. _point.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/shapes/2D/point.py

::

    point(x: float, y: float, shape="circle")


* 参数 ::

        x 点x坐标
        y 点y坐标
        shape: "circle"/"rect"



* point.py_

    .. image:: /_static/examples/shapes/2D/point.png
    .. literalinclude:: ../../../../../examples/shapes/2D/point.py
        :language: python
        :linenos:


* 示例 ::

        point(0, 0)
        point(50, 50, stroke_width=10, shape="circle")
        point(50, 50, stroke_width=10, shape="rect")
        point(50, 50, stroke_color=(255, 0, 0))

