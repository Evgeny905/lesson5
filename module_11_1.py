import requests
response = requests.get('https://dzen.ru/?yredirect=true')  # Запрос на сайт
print(response.status_code)                                 # Статус кода, 200 - значит без ошибок
print(response.headers['content-type'])                     # Проверка типа контента
print(response.encoding)                                    # Проверка кодировки - utf-8
print(response.text)                                        # Содержание ответа сервера

import numpy
matrix = numpy.array([[2, 1, 6], [3, 5, 4]])                # Создание матрицы
print(matrix)                                               # Вывод матрицы в консоль
print(matrix.shape)                                         # Вывод параметров матрицы (количество строк, количество столбцов)
print(matrix[0, 2])                                         # Вывод 3-го значения в 1-й строке
print(numpy.sort(matrix))                                   # Сортировка значений матрицы

import matplotlib.pyplot
fig, ax = matplotlib.pyplot.subplots()                         # Создание фигуры с отдельными осями
ax.plot([1, 3, 2, 4], [2, 4, 1, 3], color='orange')      # Заполнение данных по осям, выбор цвета, отрисовка фигуры
matplotlib.pyplot.show()                                       # Отображение фигуры