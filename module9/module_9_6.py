#Домашнее задание по теме "Генераторы"
# Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор, при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
#
# Пункты задачи:
#
#     Напишите функцию-генератор all_variants(text).
#     Опишите логику работы внутри функции all_variants.
#     Вызовите функцию all_variants и выполните итерации.
#

def all_variants(text):
    """
    функция использует функцию combinations
    из библиотеки itertools
    для перебора всех возможных значений
    сначала 1 символ, потом 2 и заканчивая всеми символами в строке

    """
    from itertools import combinations
    for j in range(1, len(text) + 1):
        for i in combinations(text, j):
            yield ''.join(i)

if __name__ == '__main__':
    text = 'abc678'

    for i in all_variants(text):
        print(i)
