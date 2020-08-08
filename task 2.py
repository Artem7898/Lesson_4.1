"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""

def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'
    return factorial_memo[number]
#__________________________________________________________________________________________________

# Решения Задачи №2

from math import factorial
from timeit import default_timer as timer

start = timer()
factorial_memo = {}


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'
    return factorial_memo[number]

########################################################################################

factorial_memo = {}


def recursive_reverse(number):
    if number < 0: return 10
    return number % factorial(number // 10)
    return factorial_memo[number]


end = timer()
print(end - start)
##########################################################################################

from timeit import default_timer as timer
start = timer()

class Memoize:
    def __init__(self, num):
        self.f = num
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

def recursive_reverse(num):
    if num < 0: return 10
    return num % factorial(num // 10)

factorial = Memoize(recursive_reverse)
print(recursive_reverse) # Добавив print + recursive_reverse функция начала работать еще медленей, получилось + хеш.
end = timer()
print(end - start)
