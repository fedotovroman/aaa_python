Домашняя работа по Python: pytest, 4 issue. Инструкция к запуску тестирования
==============================
1. Откройте консоль (cmd).
2. Перейдите в директорию проекта (cd directory) и выполните: pytest one_hot_encoder_test.py -v
3. В случае прохождения всех тестов будет выведено: 
```
================================================= test session starts =================================================
platform win32 -- Python 3.9.6, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- c:\users\roman\appdata\local\programs\python\python39\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Roman
collected 4 items

Documents/GitHub/aaa_python/5 tests in python/4 issue/one_hot_encoder_test.py::test_all_features_are_different PASSED [ 25%]
Documents/GitHub/aaa_python/5 tests in python/4 issue/one_hot_encoder_test.py::test_some_features_are_equal PASSED [ 50%]
Documents/GitHub/aaa_python/5 tests in python/4 issue/one_hot_encoder_test.py::test_ft_returns_list PASSED       [ 75%]
Documents/GitHub/aaa_python/5 tests in python/4 issue/one_hot_encoder_test.py::test_at_least_one_arg PASSED      [100%]

================================================== 4 passed in 0.03s ==================================================
```
