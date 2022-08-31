from pprint import pprint

import math


class Animal:
    name = 'Name'
    __age = 0  # приватный элемент (инкапсуляция)

    def __init__(self, name, age):  # инициализатор
        self.name = name
        self.__age = age

    @property  # декораторы
    def age(self):  # дает доступ к приватным элементам
        return self.__age

    @age.setter
    def age(self, value):  # дает возможность изменять приватные элементы
        if value > 0:
            self.__age = value
        else:
            print('Wrong data')

    # age = property(fget=get_age, fset=set_age)

    @classmethod  # имеет доступ к локальному пространству имен класса, возможно вызвать из любого объекта и любого класса
    def info(cls):  # дает доступ к функциям класса и его переменным
        print(cls.name, cls.__age)
        cls.voice()

    def voice(self):
        print('Voice')

    @staticmethod  # не имеет доступа к локальному пространству имен, ничего не выходит и не заходит (ваккум), инкапсулированное пространство
    def eat():
        Animal.__age += 10
        print('Eating')


class Cat(Animal):
    def __init__(self, name, age, color):  # инициализатор
        super().__init__(name, age)
        self.color = color

    def voice(self):
        super().voice()
        print('Meow')

    @staticmethod
    def eat():
        print('Eating2')

    def info(self):
        print(self.name, self.age, self.color)

class Dog(Animal):
    def __init__(self, name, age, color):  # инициализатор
        super().__init__(name, age)
        self.color = color

    def voice(self):
        super().voice()
        print('Woof')

    @staticmethod
    def eat():
        print('Eating3')

    def info(self):
        print(self.name, self.age)

    def __repr__(self):
        return self.name + ' ' + str(self.age) + ' ' + self.color

    def __str__(self):
        return self.name + ' ' + str(self.age) + ' ' + self.color


cat = Cat(name='Murzik', age=3, color='black')
dog = Dog(name='Reks', age=5, color='red')
print(cat.__dict__)

# Animal.__new__() # конструктор

