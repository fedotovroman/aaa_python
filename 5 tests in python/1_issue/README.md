Домашняя работа по Python: doctest, 1 issue. Инструкция к запуску тестирования
==============================
1. Откройте консоль (cmd).
2. Перейдите в директорию проекта (cd directory) и выполните:
	C:\Users\Roman>python -m doctest -o IGNORE_EXCEPTION_DETAIL morse.py -v
3. В случае прохождения всех тестов будет выведено: 
```
Trying:
    encode('MAI-PYTHON-2019')
Expecting:
    '-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.'
ok
Trying:
    encode('HELLO-FROM-ACADEMY') #doctest: +NORMALIZE_WHITESPACE
Expecting:
    '.... . .-.. .-.. --- -....- ..-. .-.      --- -- -....- .- -.-. .- -.. . -- -.--'
ok
Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode('Привет-из-академии!')
Expecting:
    Traceback (most recent call last):
    KeyError:
ok
1 items had no tests:
    morse
1 items passed all tests:
   4 tests in morse.encode
4 tests in 2 items.
4 passed and 0 failed.
Test passed.
```
