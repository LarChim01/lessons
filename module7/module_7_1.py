#Домашнее задание по теме "Режимы открытия файлов"
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f"{self.name}, {self.weight}, {self.category}\n")


class Shop:
    

    def get_products(self):
        self.__file_name = 'products.txt'

        file = open(self.__file_name, 'r')
        spisok_tovarov = file.read()
        file.close()
        return spisok_tovarov

    def add(self, *tovar):

        spisok_tovarov = self.get_products()
        file = open(self.__file_name, 'a')
        for item in tovar:
            product = str(item)
            if not (product in spisok_tovarov):
                spisok_tovarov += product
                file.write(product)

            else:
                print(f'Продукт  {product}  уже есть в магазине')



        file.close()


if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')


    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())
