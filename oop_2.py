# абстрактный класс

from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    a = 10

    @abstractmethod
    def voice(self):
        raise NotImplementedError()

    @abstractmethod
    def eat(self):
        raise NotImplementedError()


class Cat(Animal):
    def voice(self):
        print('Meow')

    def eat(self):
        print('Eat cat')


class Dog(Animal):
    def voice(self):
        print('Woof')

    def eat(self):
        print('Eat dog')


print()