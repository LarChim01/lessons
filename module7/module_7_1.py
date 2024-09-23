#Домашнее задание по теме "Режимы открытия файлов"
from pprint import pprint
class Product:
    def __init__(self, name ,weight, category):
        self.name = name
        self.weight = weight
        self.category = category
        
    def __str__(self):
        return (f"{self.name}, {self.weight}, {self.category}\n")


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        tear = file.read()
        file.close()
        return tear

    def add(self, *tov):

        tear = self.get_products()

        for item in tov:
            t = str(item)
            if not (t in tear):
                tear += t
            else:
                print(f'Продукт  {t}  уже есть в магазине')

        file = open(self.__file_name, 'w')
        file.write(tear)
        file.close()




if __name__  ==  "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())
