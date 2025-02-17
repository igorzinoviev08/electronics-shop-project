import csv
import os.path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f'{self.__class__.__name__}{self.__name, self.price, self.quantity}'

    def __str__(self):
        return f'{self.__name}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
        else:
            self.__name = value[0:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path="../src/items.csv"):
        try:
            if not os.path.exists(path):
                raise FileNotFoundError(f"Отсутствует файл {path.split('/')[-1]}")
            cls.all.clear()
            with open(path, 'r', encoding='windows-1251') as fp:
                file_reader = csv.DictReader(fp)
                for row in file_reader:
                    if set(row) != {'name', 'price', 'quantity'}:
                        raise InstantiateCSVError(path)

                    cls(row['name'], float(row['price']), int(row['quantity']))
        except FileNotFoundError:
            raise

        except InstantiateCSVError:
            raise InstantiateCSVError(path)

    @staticmethod
    def string_to_number(value):
        return int(float(value))


class InstantiateCSVError(Exception):
    def __init__(self, path):
        super().__init__(f"Файл {path.split('/')[-1]} поврежден")
