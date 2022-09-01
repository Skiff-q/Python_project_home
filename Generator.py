# a = []
# for itm in range(1, 11):
#     a.append(itm ** 2)
# print(a)
#
#
# # генератор списка / list comprehension
# b = [itm ** 2 for itm in range(1, 11)]
# print(b)
#
# # Выражения генераторы. Генераторы - итератор, элементы которого можно обойти только 1 раз
# # Итератор - объект, который поддерживает функцию next() и помнит, какой элемент будет браться следующим
# # Итерируемый объект - объект, который предоставляет возможность обойти поочередно свои элементы
# s = [1, 2, 3] # Список - итерируемый объект
#
# # d = iter(s) # Итератор
# # print(next(d))
# # print(next(d))
# # print(next(d))
# # print(next(d)) # ошибка
#
# b = (itm ** 2 for itm in range(1, 11)) # генератор
#
# # for itm in b:
# #     print(itm)
#
# print(sum(b))
# print(sum(b)) # 0


# c = list(range(100000000000000))

# c = [itm for itm in range(10000000000)]

# c = (itm for itm in range(10))  # генератор не записывает в оперативную память, поэтому дает возможность создавать такие большие числа
# # for itm in c:
# #     print(itm)
#
# # print(len(c[52]))  # нельзя использовать
#
# l1 = list(c)
# print(l1)
# l2 = list(c) # пустой список
# print(l2)


# функции генераторы
#
# def fn():
#     return [15, 98, 63]
#
#
# print(fn())
# print(fn())
#
# # генератор
# def gen_g():
#     a = 9
#     for itm in [15, 98, 63, 57]:
#         yield itm
#         print(a)
#         a = a*10 + 9
#
#
# s = gen_g()
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
#
#
# for itm in gen_g():
#     print(itm)


# факториал числа
def fact(n):
    pr = 1
    a = []
    for itm in range(1, n + 1):
        pr = pr * itm
        a.append(pr)
    return a


print(fact(10))


# функция генератор факториал числа

def fact_gen(n):
    pr = 1
    for itm in range(1, n + 1):
        pr = pr * itm
        yield pr


s = fact_gen(20)
print(next(s))
print(next(s))
print(next(s))
print(next(s))

for i in fact_gen(20):
    print(i, end=' ')

