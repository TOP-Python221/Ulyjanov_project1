"""Модуль для тестирования скопированного кода

Код переносится в этот модуль из проекта-примера, здесь изучается и тестируется, затем переносится в нужные модули проекта"""

from configparser import ConfigParser as CP

stat_path = 'players.ini'
save_path = 'saves.ini'

# fh_in = open(path)
# print(*fh_in)
# fh_in.close()
# with open(path) as fh_in:
#     print(*fh_in)

# ИСПРАВИТЬ: это надо в функциях делать - после завершения чтения или записи файлов данных нам не нужен объект парсера ни в глобальном пространстве имён приложения ни в пространствах имён импортированных модулей
# создаем объект парсера
file_ini = CP()
# читаем конфиг
file_ini.read(stat_path)

# обращение как к обычному словарю
# print(file_ini['player 1']['training'])


STATS = {}
SAVES = {}


def read_ini():
    global STATS, SAVES
    for player in file_ini.sections():
        # ИСПРАВИТЬ: в вашем файле данных это поле называется 'first_time', а не 'training'
        tr = True if file_ini[player]['training'] == 'True' else False
        st = file_ini[player]['stats'].split(',')
        # ИСПРАВИТЬ: следите за одинаковыми именами ключей в словарях - ключа 'trainigh' не существует
        STATS[player] = {'trainigh': tr,
                         'stats': {'wins': int(st[0]), 'ties': int(st[1]), 'fails': int(st[2])}}

    # необходимо очистить объект file_ini, иначе при последовательном чтении второго файла его поля будут дозаписаны в объект file_ini
    file_ini.clear()
    file_ini.read(save_path)

    for save in file_ini.sections():
        players = frozenset(save.split(','))
        SAVES[players] = dict(file_ini[save])

    # отсутствие сохраненных ранее имен игроков трактуем как первый запуск приложения
    # if STATS:
    #     return False
    # else:
    #     return True

read_ini()


def save_ini():
    """ Запись в конфигурационные файлы, из глобальных переменных статистики и сохранений """
    print(SAVES)

save_ini()
