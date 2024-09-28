#Домашнее задание по теме "Введение в функциональное программирование"

def apply_all_func(int_list, *functions):
    '''
    функция принимает список чисел и функции для их обработки
    '''
    results = {}
    for fun in functions:
        results[fun.__name__] = fun(int_list)
    return results


if __name__ == "__main__":
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
