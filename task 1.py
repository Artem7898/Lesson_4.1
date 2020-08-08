"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

# Решение задачи №1

from timeit import default_timer as timer

start = timer()

nums = [3, 8, 10, 12, 5, 9, 2, 1]

for el in range(0,len(nums)):
    if el % 2 == 0:
        print(nums[el])
    else:
        continue

end = timer()
print(end - start)

from timeit import default_timer as timer

start = timer()


nums = [3, 8, 10, 12, 5, 9, 2, 1]
new_arr = [i for i in nums if i % 2 == 0]
print(new_arr)

end = timer()
print(end - start)

"""
Не получилось оптимизировать код, чтобы снизить время выполнения.
Код который давался в пример, оказался быстрей.
Я старался.

"""