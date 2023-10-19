---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.15.2
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Шпаргалка по Python и Jupyter


## Загрузка кода из файла

```python
%load -r 16:19 vector.py
```

```python
%load -s Vector vector.py
```

## Сохранение кода в файл

```python
%%writefile class_info.py

import inspect

def get_class_info(cls):
    '''Displays information about the class'''
    
    print(f'Класс {cls.__name__}: # {cls.__doc__}')

    print('Attributes:')
    init_signature = inspect.signature(cls.__init__)
    for param_name, param in init_signature.parameters.items():
        if param.name != 'self':
            param_annotation = ': ' + str(param.annotation)[:-1]
            param_default = '' if str(param.default) == "<class 'inspect._empty'>" else ' = ' + str(param.default)
            print(f'    {param.name}{param_annotation}{param_default}')

    print('Methods:')
    for attribute in dir(cls):
        if callable(method:=getattr(cls, attribute)) and not attribute.startswith("__"):
            method_name = method.__name__
            method_args = inspect.signature(method)
            method_doc = str(inspect.getdoc(method)).splitlines()[0]
            print(f'    {method_name}{method_args}: # {method_doc}')
```

```python
# %load class_info.py

import inspect

def get_class_info(cls):
    '''Displays information about the class'''
    
    print(f'Класс {cls.__name__}: # {cls.__doc__}')

    print('Attributes:')
    init_signature = inspect.signature(cls.__init__)
    for param_name, param in init_signature.parameters.items():
        if param.name != 'self':
            param_annotation = ': ' + str(param.annotation)[:-1]
            param_default = '' if str(param.default) == "<class 'inspect._empty'>" else ' = ' + str(param.default)
            print(f'    {param.name}{param_annotation}{param_default}')

    print('Methods:')
    for attribute in dir(cls):
        if callable(method:=getattr(cls, attribute)) and not attribute.startswith("__"):
            method_name = method.__name__
            method_args = inspect.signature(method)
            method_doc = str(inspect.getdoc(method)).splitlines()[0]
            print(f'    {method_name}{method_args}: # {method_doc}')

```

```python
get_class_info(Vector)
```

```python
from class_info import get_class_info

get_class_info(Vector)
```

## Дополнение кода в файле

```python
%%writefile vector_info.py
import vector
```

```python
%%writefile -a vector_info.py
import class_info
```

```python
%%writefile -a vector_info.py
class_info.get_class_info(vector.Vector)
```

## Запуск кода из файла

```python
%run vector_info.py
```

## Оформление кода

1. https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings

2. https://numpydoc.readthedocs.io/en/latest/format.html



1. Переменныи, функции - snake_case
2. Классы - CamelCase
3. docstring


### Именование

1. _bar - private
2. __ init __ - builts !!! НЕ ИСПОЛЬЗОВАТЬ
3. class_
   


### Принципы
1. Принцип одной ответственности
2. Комментарии врут
3. TDD
4. Типизация (+/-)
5. Будь консервативен, когда передаешь, будь либерален, когда принимаешь. (Закон Постела, или принцип надежности)


## Вызов справки

```python
help(len)
```

```python
len.__doc__
```

```python
# Справка по собственному коду
help(Vector.norm)
```

```python
%lsmagic
```

```python
%load?
```

```python
len?
```

```python
Vector.radius?
```

## Работа с терминалом

```python
!ls
```

```bash
echo Hello World!
```

### pydoc

```bash

python -m pydoc vector
```

```python
!python -m pydoc vector
```

```bash

python -m pydoc -n localhost
```

```python
!python -m pydoc -w vector
```

```python
!python -m pydoc -w vector.Vector.norm
```

### doctest

```bash
python -m doctest vector.py
```

## Где еще можно получить информацию

```python
dir(str)
```

```python
import random

random.__dir__()
```

```python
dir(Vector)
```

## Полезые инструменты
1. Линтеры: flake8, pylint
2. Инструменты форматирования: autopep, black, blue
3. Проверка типов: mypy, pytype
4. Тестирование: pytest, unittest
