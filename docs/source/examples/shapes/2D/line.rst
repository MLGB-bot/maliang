线(line)
=====================

.. _line.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/shapes/2D/line.py
.. _line_bezier.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/shapes/2D/line_bezier.py
.. _line_bezier_quad.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/shapes/2D/line_bezier_quad.py
.. _line_bezier_cubic.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/shapes/2D/line_bezier_cubic.py



line()
------------------

::

    line(x1: float, y1: float, x2: float, y2: float)


* 参数::

        x1 第1个点的x坐标
        y1 第1个点的y坐标
        x2 第2个点的x坐标
        y2 第2个点的y坐标


* line.py_

.. image:: /_static/examples/shapes/2D/line.png
.. literalinclude:: ../../../../../examples/shapes/2D/line.py
    :language: python
    :linenos:

* 示例::

        line(0, 0, 100, 100)
        line(150, 150, 50, 150, stroke_width=4)
        line(150, 150, 50, 150, stroke_color=(255, 0, 0))
        line(150, 50, 150, 150, stroke_width=2, stroke_color=(255, 0, 0))


-------------------


line_bezier()
------------------

::

    line_bezier(x1: float, y1: float, x2: float, y2: float)


    x1 第1个点的x坐标
    y1 第1个点的y坐标
    x2 第2个点的x坐标
    y2 第2个点的y坐标


* line_bezier.py_

.. image:: /_static/examples/shapes/2D/line_bezier.png
.. literalinclude:: ../../../../../examples/shapes/2D/line_bezier.py
    :language: python
    :linenos:




-------------------


line_bezier_quad()
------------------

::

    line_bezier_quad(x1: float, y1: float, x2: float, y2: float, cx: float, cy: float)

* 参数 ::

        x1 第1个点的x坐标
        y1 第1个点的y坐标
        x2 第2个点的x坐标
        y2 第2个点的y坐标
        cx 控制点x坐标
        cy 控制点y坐标


*  line_bezier_quad.py_

.. image:: /_static/examples/shapes/2D/line_bezier_quad.png
.. literalinclude:: ../../../../../examples/shapes/2D/line_bezier_quad.py
    :language: python
    :linenos:


----------------------


line_bezier_cubic()
------------------------------------

::

    line_bezier_cubic(x1: float, y1: float, x2: float, y2: float, cx1: float, cy1: float, cx2: float, cy2: float)


* 参数 ::

    x1 第1个点的x坐标
    y1 第1个点的y坐标
    x2 第2个点的x坐标
    y2 第2个点的y坐标
    cx1 第1个控制点x坐标
    cy1 第1个控制点y坐标
    cx2 第2个控制点x坐标
    cy2 第2个控制点y坐标


* line_bezier_cubic.py_

.. image:: /_static/examples/shapes/2D/line_bezier_cubic.png
.. literalinclude:: ../../../../../examples/shapes/2D/line_bezier_cubic.py
    :language: python
    :linenos:
