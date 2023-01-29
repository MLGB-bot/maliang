事件 (events)
==================================

1. 判断事件(bool)
-----------------------

::

    is_key_clicked(): 是否点击键盘按键.True/False.
    is_key_released(): 是否释放键盘按键.True/False.
    is_key_up(): 键盘按键是否抬起(未点击)状态.True/False.
    is_key_down(): 键盘按键是否按下(点击)状态.True/False.

.. _events0.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/keyboard/events0.py

* events0.py_

.. literalinclude:: ../../../../examples/keyboard/events0.py
    :language: python
    :linenos:


2. 监听函数
-----------------------

::

    on_key_clicked(): 键盘点击事件
    on_key_released(): 键盘松开事件
    on_key_down(): 键盘按键按下(点击)的状态触发事件
    on_char_down(): 字符按下(点击)的状态触发事件


.. _events1.py:      https://github.com/MLGB-bot/maliang/blob/main/examples/keyboard/events1.py

* events1.py_

.. literalinclude:: ../../../../examples/keyboard/events1.py
    :language: python
    :linenos:

