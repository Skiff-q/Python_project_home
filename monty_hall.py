# while True:
#     name = input('Enter your name or type exit: ')
#     if name == 'exit':
#         break

# price = {
#     'one': 100,
#     'two': 200,
#     'three': 500,
#     'default': 'unknown key'
# }
#
# result = price.get('five', price['default'])
# print(result)
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 1, 2, 5]
# my_set = set(my_list)
# my_list = list(my_set)
# print(my_list)

# my_list = [4, 3, 2, 1]
#
# for itm in my_list:
#     if itm == 2:
#         continue
#     print(itm)


# def calculate_square_of_circle(radius):
#     square = 2 * 3.14 * radius
#     return square
#
#
# user_radius = float(input('Please enter radius: '))
#
# result = calculate_square_of_circle(user_radius)
# print(result)

# x = 10
#
# def df(x):
#     print(x)
#     x = 20
#     print(x)
#
# print(x)
# df(0)
# print(x)

# def args_fn(*numbers):  # args ,  ('1', '2', '3')  tuple[0]
#     for arg in numbers:
#         print(arg)
#
#
# args_fn('1', '2', '3')
#
#
# def kwargs_fn(**numbers):  # kwargs
#     for k, v in numbers.items():
#         print(k, ":", v)
#
#
# kwargs_fn(one=100, two=200, three=500)
import random


def open_the_door(door: int, fact: bool):
    all_doors = [1, 2, 3]
    possible_doors = all_doors.copy() # возможные двери
    price = random.randint(1, 3)
   # primary_choice = random.randint(1, 3) # основной выбор

    try:
        possible_doors.remove(price)
        possible_doors.remove(door)
    except:
        pass

    # номер какой из оставшихся откроет ведущий?
    choice = door # выбор

    reveal = possible_doors.pop() # ведущий открывает эту дверь

    if fact:
        all_doors.remove(reveal)
        all_doors.remove(door)
        choice = all_doors.copy()
        if price == choice[0]:
            return 1
        else:
            return 0
    else:
        if price == choice:
            return 1
        else:
            return 0

i = 1000
true_false_change = []

# при смене
for itm in range(i):
    true_false_change.append(open_the_door(2, True))

value_0 = true_false_change.count(0)
value_1 = true_false_change.count(1)
print(f'Количество проигрышей: {value_0}, Количество выигрышей: {value_1}')


true_false = []

# без смены
for itm in range(i):
    true_false.append(open_the_door(1, False))

value_0 = true_false.count(0)
value_1 = true_false.count(1)
print(f'Количество проигрышей: {value_0}, Количество выигрышей: {value_1}')

### При смене двери вероятность выиграть равна более 60 %, без смены вероятность составляет 30 %