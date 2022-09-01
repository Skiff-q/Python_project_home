# дата классы
from dataclasses import dataclass


# class Date:
#     def __init__(self, day, month, year, hour, minute, second):
#         self.day = day
#         self.month = month
#         self.year = year
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#
#
# d1 = Date(13, 1, 2022, 6, 7, 8)
# d2 = Date(13, 1, 2022, 6, 7, 8)


@dataclass(order=True)  # order=True даем возможность сравнивать
class Date:
    day: int
    month: int
    year: int
    hour: int
    minute: int
    second: int

    # def __lt__(self, other):  # даем возможность сравнивать
    #     return self.day < other.day


d1 = Date(13, 1, 2022, 6, 7, 8)
d2 = Date(13, 1, 2022, 6, 7, 8)

print(d1 < d2)

a = 5
b = 0

try:
    print(a / b)
except:
    print('Деление на ноль')
finally:
    print('блок отработал')

print(a)
