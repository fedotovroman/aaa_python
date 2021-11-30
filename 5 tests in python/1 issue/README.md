Домашняя работа по Python: doctest. Инструкция к запуску тестирования
==============================
1. Откройте консоль
2. Перейдите в директорию проекта и выполните: python morse.py
3. В случае прохождения всех тестов будет выведено: 
```
Trying:
    encode('MAI-PYTHON-2019')
Expecting:
    '-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.'
ok
Trying:
    encode('HELLO-FROM-ACADEMY')
Expecting:
    '.... . .-.. .-.. --- -....- ..-. .-. --- -- -....- .- -.-. .- -.. . -- -.--'
ok
Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode('Привет-из-академии!') # doctest: +IGNORE_EXCEPTION_DETAIL
Expecting:
    Traceback (most recent call last):
    KeyError:
ok
Trying:
    encode('WINTER2021') # doctest: +ELLIPSIS
Expecting:
    '.--...'
ok
1 items had no tests:
    __main__
1 items passed all tests:
   5 tests in __main__.encode
5 tests in 2 items.
5 passed and 0 failed.
Test passed
```