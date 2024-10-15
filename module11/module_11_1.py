#Домашнее задание по теме "Обзор сторонних библиотек Python"
# numpy - создать массив чисел, выполнить математические операции
# с массивом и вывести результаты в консоль.
# matplotlib - визуализировать данные с помощью библиотеки любым
# удобным для вас инструментом из библиотеки.
# pillow - обработать изображение, например, изменить его размер,
# применить эффекты и сохранить в другой формат.

#numpy
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFilter
# создадим массив из списка
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# или кортежа
ar1 = np.array((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
ar3 = arr * ar1 #каждый элемент первого массива умножается на соответствующий элемент второго массива

print(ar3)
# # создадим массив с элементами типа float
arr_f = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], float)

print(arr_f)
# #  кортеж из чисел для указания количества нулей в каждом измерении
n0 = np.zeros((2, 3))
print(n0)


#плавно переходим к matplotlib построим пару графиков

#"Очки' на основе кардиоды в полярных координатах

plt.axes(projection='polar')
a = 4
rads = np.arange(0, (2 * np.pi), 0.01) # создаём массив значений, функция из numpy
for rad in rads:
    r = a + ( a *  np.cos(2 * rad))
    plt.polar(rad, r, 'r.')
plt.show()

# Логарифметическая функция
x = np.linspace(1, 5, 5000) # снова функция  из numpy
y = np.log(x)
# # # создадим сетку
plt.grid()

# # выведем кривую и подписи на графике
plt.plot(x, y)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.show()
#Круговая диаграмма
vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMW", "Audi", "Jaguar"]

plt.pie(vals, labels=labels, autopct='%1.1f%%')
plt.title("Распределение марок автомобилей на дороге")
plt.show()


#библиотека pillow
im1 = Image.open('fon.jpg') #открываем картинку - фон
im2 = Image.open('caty.png') #открываем котика
mask_im = Image.new("L", im2.size, 0) # cоздаём маску по размеру котика
draw = ImageDraw.Draw(mask_im) #рисуем маску
draw.ellipse((90, 50, 200, 150), fill=255) #русуем элипс
mask_im_blur = mask_im.filter(ImageFilter.GaussianBlur(10)) #применяем фильтр

im1.paste(im2, (100, 50), mask_im_blur) # совмещаем рисунки
im1.save('new_image.png', quality=95) #сохраняем получившийся рисунок
#закрываем открытые файлы
im1.close()
im2.close()
