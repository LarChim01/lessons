#Домашнее задание по теме "Создание потоков".
# Необходимо создать функцию write_words(word_count, file_name), где word_count - количество записываемых слов, file_name - название файла, куда будут записываться слова.
# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
# Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
# В конце работы функции вывести строку "Завершилась запись в файл <название файла>".
#
# После создания файла вызовите 4 раза функцию write_words, передав в неё следующие значения:
#
#     10, example1.txt
#     30, example2.txt
#     200, example3.txt
#     100, example4.txt
#
# После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
#
#     10, example5.txt
#     30, example6.txt
#     200, example7.txt
#     100, example8.txt
#
# Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
# Также измерьте время затраченное на выполнение функций и потоков. Как это сделать рассказано в лекции к домашнему заданию.

from time import sleep
from datetime import datetime
import threading

def write_words(word_count, file_name):
    with open(file_name, "w", encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i+1}\n")
            sleep(0.01)
#Вызовы функций
time_start = datetime.now()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
time_end = datetime.now()

time_res_fun = time_end - time_start
print(f'Время выполнения функций - {time_res_fun}')

# создание потоков
thr_1 = threading.Thread(target=write_words, args=(10, "example1.txt"))
thr_2 = threading.Thread(target=write_words, args=(30, "example2.txt"))
thr_3 = threading.Thread(target=write_words, args=(200, "example3.txt"))
thr_4 = threading.Thread(target=write_words, args=(100, "example4.txt"))
time_start = datetime.now()
# запуск потоков
thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()
#остановка потоков
thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()


time_end = datetime.now()
time_res_f = time_end - time_start

print(f'Время выполнения  в потоке - {time_res_f}')

print(f'Разница в скорости {time_res_fun - time_res_f}')

