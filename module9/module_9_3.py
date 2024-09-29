#Домашнее задание по теме "Генераторные сборки"

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
#В переменную first_result запишите генераторную сборку, которая высчитывает
# разницу длин строк из списков first и second, если их длины не равны.
# Для перебора строк попарно из двух списков используйте функцию zip.

first_result = (len(x[0]) - len(x[1]) for x in zip(first,second) if len(x[0]) != len(x[1]))
#В переменную second_result запишите генераторную сборку,
# которая содержит результаты сравнения длин строк в одинаковых позициях из
# списков first и second. Составьте эту сборку НЕ используя функцию zip.
# Используйте функции range и len.

second_result = (len(first[i]) == len(second[i]) for i in range(0, len(first)))


print(list(first_result))
print(list(second_result))
