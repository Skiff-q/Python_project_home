import os
import datetime
import pathlib


class Logger:
    datetime_current = datetime.datetime.now()
    _date_current = datetime.date.today()
    _time_current = datetime_current.time()
    path = None
    current_file = None

    def __new__(cls, *args, **kwargs):  # конструктор, задаем паттерн под новый создаваемый объект
        if not hasattr(cls, 'instance'):  # проверяем создан ли объект
            cls.instance = super(Logger, cls).__new__(cls)  # создаем экземпляр класса через родительский класс(object)
        return cls.instance

    def __init__(self, path='./'):
        Logger.file_handing()
        Logger.path = path
        Logger.current_file = f'logger_{self._date_current.day}.{self._date_current.month}.{self._date_current.year}.log'
        Logger.current_time = f'[{self._time_current.hour}:{self._time_current.minute}:{self._time_current.second}]'

    @property
    def current_date(self):
        return self._date_current

    @current_date.setter
    def current_date(self, value):
        self._date_current = value

    @property
    def current_time(self):
        return self._time_current

    @current_time.setter
    def current_time(self, value):
        self._time_current = value

    @classmethod
    def file_handing(cls, text='Updating this file'):

        if os.path.isfile(
                f'{cls.path}{Logger.current_file}'):
            with open(
                    f'{cls.path}{Logger.current_file}',
                    'a+', encoding='UTF-8') as file:
                file.write(f'\n{Logger.current_time} \t \t {text}')
        else:
            with open(
                    f'{cls.path}{Logger.current_file}',
                    'w+', encoding='UTF-8') as file:
                file.write(f'{Logger.current_time} \t \t Create this file')

    def clear_log(self):
        if os.path.isfile(
                f'{self.path}{Logger.current_file}'):
            with open(
                    f'{self.path}{Logger.current_file}',
                    'w', encoding='UTF-8') as file:
                file.write(f'{Logger.current_time} \t \t This file has been cleared')

    def get_logs(self):
        with open(f'{self.path}{Logger.current_file}',
                  'r', encoding='UTF-8') as file:
            logs = []
            for itm in file.readlines():
                itm = itm.replace("\t", "")
                logs.append(itm.replace("\n", ""))
        return logs

    def get_last_event(self):
        logs = Logger.get_logs(self)
        return logs[-1]

    def get_all_logs(self):
        dirfiles = pathlib.Path(self.path)
        current_pattern = 'logger_*.log'
        files = dirfiles.glob(current_pattern)
        loggers = []
        for itm in files:
            loggers.append(str(itm))
        return loggers


if __name__ == '__main__':
    log = Logger('../files/')
    log.file_handing(text='Quit testing....')
    print()
