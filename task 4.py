"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


print(func_1())
print(func_2())

new_array = [1, 3, 1, 3, 4, 5, 1]
print(max(el for el in new_array if new_array.count(el) == max(map(new_array.count, new_array,))))
print('Чаще всего встречается число 1')

####################################################################################################

# Решения Задачи №4

import cProfile
import time

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


print(func_1())
print(func_2())

new_array = [1, 3, 1, 3, 4, 5, 1]
print(max(el for el in new_array if new_array.count(el) == max(map(new_array.count, new_array, ))))
print('Чаще всего встречается число 1')


def func_1():
    print("Я быстрая функция")


def func_2():
    time.sleep(3)
    print("Я очень медленная функция")

    new_array
    time.sleep(0.5)
    print("Я средняя функция...")


def main():
    func_1()
    func_2()
    new_array


if __name__ == '__main__':
    main()

cProfile.run('func_1(),func_2(),new_array.main()')

if __name__ == '__main__':
    import timeit

    print(timeit.timeit("func_1(),func_2(),new_array", setup="from __main__ import func_1()"))