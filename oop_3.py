# множественное наследование

class MealMixin:
    meal = None

    def get_food(self):
        if self.meal is None:
            raise ValueError('Food is not set')
        print(f'Eating {self.meal}')


class Meal:
    name_meal = 'Meat'
    weight = 1000

    def eat_meal(self):
        print(f'Eating {self.name_meal} {self.weight}')
        self.weight = 0

    def info_meal(self):
        print(self.name_meal, self.weight)


class Animal:
    name = 'Name'

    def __init__(self, name, age):  # инициализатор
        self.name = name
        self.__age = age

    def eat(self):
        print('Eating food')


class Cat(MealMixin, Animal, Meal):
    meal = 'Meat'

    def __init__(self, name, age, color):  # инициализатор
        super().__init__(name, age)
        self.color = color

    def voice(self):
        print('Meow')


    def info(self):
        print(self.name, self.age, self.color)


class Dog(MealMixin, Animal, Meal):
    meal = 'Bone'

    def __init__(self, name, age, color):  # инициализатор
        super().__init__(name, age)
        self.color = color

    def voice(self):
        print('Woof')

    def info(self):
        print(self.name, self.age)



cat = Cat(name='Murzik', age=3, color='black')
dog = Dog(name='Reks', age=5, color='red')
print()