#Домашнее задание по теме "Позиционирование в файле".
def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='UTF-8')
    stroka = 0
    rezult = {}
    for elem in strings:
        stroka += 1
        key = (stroka, file.tell())
        rezult[key] = elem
        file.write(elem)
        file.write('\n')

    file.close()
    return rezult




if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]
    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
