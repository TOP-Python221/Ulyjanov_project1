
""" Модуль верхнего уровня, для учебного проекта 1: Крестики-нолики """
from pathlib import Path
from configparser import ConfigParser as CP

# суперцикл
while True:
    command = input(' Для начала игры введите new для завершения exit: ').lower()

    if command in ('quit', 'exit', 'q', 'e'):
        break

    elif command in ('new', 'n'):

# сделал так потому что пока не смог решить проблему с импртом Path(pycharm ругается, что неиспользуемый импорт и не важно использую я его или нет)
        PLAYERS_INI_PATH = 'players.ini'
        SAVE_INI_PATH = 'save.ini'

        # создаем объект парсера
        file_ini = CP()

# глолбальные переменные
        STATS = {}
        SAVES = {}


        def read_ini():
            """ Читает из файла """
            file_ini.read(PLAYERS_INI_PATH)
            global STATS, SAVES
            for player in file_ini.sections():
                tr = True if file_ini[player]['training'] == 'True' else False
                st = file_ini[player]['stats'].split(',')
                STATS[player] = {'trainigh': tr, 'stats': {'wins': int(st[0]), 'ties': int(st[1]), 'fails': int(st[2])}}
                # для проверки работы функции read_ini
                print(STATS)

            # Необходимо отчистить объект file_ini, иначе при последовательном чтении второго файла его поляы будут дозаписаны в объект file_ini
            file_ini.clear()
            file_ini.read(PLAYERS_INI_PATH)
            for save in file_ini.sections():
                players = frozenset(save.split(','))
                SAVES[players] = dict(file_ini[save])

            # отсутствие сохраненных ранее имен игроков трактуем как первый запуск приложения
            # if STATS:
            #     return False
            # else:
            #     return True

# вызов функции (чтения из файла)
        read_ini()
        def save_ini():
            """ Записывает данные в файл save.ini """
            # запрашивает имена пользователей (так сделал временно)
            players_name1 = input(' Введите имя игрока1: ')
            players_name2 = input(' Введите имя игрока1: ')
            # данные которые будут записаны в файл save.ini
            file_ini[players_name1, players_name2] = {'X': players_name2, 'turns': '-x-00-0xx'}
            with open('save.ini', 'a') as configfile:
                file_ini.write(configfile)


# вызов функции (записи)
        save_ini()






