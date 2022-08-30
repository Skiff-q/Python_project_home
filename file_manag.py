# with open('./test.txt', 'a', encoding='UTF-8') as file:
#     file.write('Some thing \n')
#
# with open('./test.txt', 'r', encoding='UTF-8') as file:
#     for line in file:
#         print(line)
#
# import csv
#
#
# with open('./files/data.csv', 'r', encoding='UTF-8') as file:
#     reader = csv.reader(file, delimiter=',')
#     for line in reader:
#         print(line)
#
#
# with open('./files/data.csv', 'r', encoding='UTF-8') as file:
#     reader = csv.DictReader(file, delimiter=',')
#     fieldnames = reader.fieldnames  # заголовки, наименования столбцов
#     print(fieldnames)
#     result = 0
#     for row in reader:
#         # print(row.get('industry_name_ANZSIC'), row.get('value'), row.get('unit'))
#         try:
#             result += int(row.get('value'))
#         except:
#             pass
#     print(result)
#
# import json
#
# with open('./files/weather.json', 'r') as file:
#     data = json.load(file)
#     print(data.get('main').get('temp')-313.75)
#
# with open('./files/text_j', 'r') as file:
#     data = file.read()      # Получаем строку, считаем обычный текстовый файл
#     info = json.loads(data) # Читаем строку, получаем json
#     print(info)
#
# with open('out.json', 'w') as file:
#     data = {'one': 100, 'two': 200, 'three': 500}
#     json.dump(data, file)                 # записываем словарь в json
#
# data = {'one': 100, 'two': 200, 'three': 500} # подготовленный словарь
#
# with open('out.json', 'w') as file:
#     file.write(json.dumps(data))              # записываем в текстовый файл


# from my_lib import monty_hall
#
# print(monty_hall.open_the_door(False))

def check_symbol(symbol):
    punctuation = [',', '.', '!', '?', ';', ':', '-', '(', ')', '"', '=', '+', '«', '–', '№']
    if symbol not in punctuation and not symbol.isdigit():
        return True
    return False


def read_file(path: str):
    uniq_word = []
    with open(path, 'r', encoding='UTF-8') as file:
        text = file.read()
        result = ''
        for itm in text:
            if check_symbol(itm):
                result += itm.lower()

        uniq_word = list(set(result.split()))

        for word in uniq_word:  # убираю лишние предлоги и тд.
            if len(word) <= 2:
                uniq_word.remove(word)
    return uniq_word


def save_file(path: str, text: list):
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(f'Уникальных слов в файле: {len(text)} \n {"=" * 100} \n')
        text.sort()
        for itm in text:
            file.write(itm + '\n')
    return True


if __name__ == '__main__':
    words = read_file('../files/data.txt')
    save_file('../files/data_save.txt', words)
