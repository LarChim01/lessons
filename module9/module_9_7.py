#Домашнее задание по теме "Декораторы"
import math

def is_prime(func):
    def wrapers(*args, **kwargs):
        def is_prime_(n):
            if n <= 1:
                return False
            if n % 2 == 0:
                return n == 2

            max_div = math.floor(math.sqrt(n))
            for i in range(3, 1 + max_div, 2):
                if n % i == 0:
                    return False
            return True

        result = func(*args, **kwargs)
        if is_prime_(result):
            print("Простое")
        else:
            print("Составное")
        return result

    return wrapers


@is_prime
def sum_three(one, two, three):
    return one + two + three

if __name__ == '__main__':
    result = sum_three(2, 3, 6)
    print(result)
