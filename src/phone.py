from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f'{self.__class__.__name__}{self.name, self.price, self.quantity, self.__number_of_sim}'

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if value <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
        self.__number_of_sim = value
    def __add__(self, other):
        if isinstance(other, (Item, Phone)):
            return self.quantity + other.quantity
        raise TypeError('Нельзя сложить Phone или Item с экземплярами не Phone или Item классов.')
    def __radd__(self, other):
        return self.__add__(other)