鼠标事件 (events)
==================================

1. 判断事件(bool)
-----------------------

::

    is_mouse_clicked(): 当前帧是否点击鼠标按键.True/False.
    is_mouse_released(): 当前帧是否释放鼠标按键.True/False.
    is_mouse_up(): 当前帧鼠标按键是否抬起(未点击)状态.True/False.
    is_mouse_down(): 当前帧鼠标按键是否按下(点击)状态.True/False.
    is_mouse_wheel(): 获取鼠标滚动状态. float.

.. _events0.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/mouse/events0.py

* events0.py_

.. literalinclude:: ../../../../examples/mouse/events0.py
    :language: python
    :linenos:


2. 监听函数
-----------------------

::

    on_mouse_clicked(): 鼠标点击事件
    on_mouse_released(): 鼠标松开事件
    on_mouse_down(): 鼠标按键按下(点击)的状态触发事件
    on_mouse_moved(): 鼠标移动触发
    on_mouse_wheel(): 鼠标滚动触发
    on_mouse_dragged(): 拖拽触发
    on_mouse_double_clicked: 鼠标左键双击触发. 双击间隔可以通过"double_click_gap"设置(秒)


.. _events1.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/mouse/events1.py

* events1.py_

.. literalinclude:: ../../../../examples/mouse/events1.py
    :language: python
    :linenos:

