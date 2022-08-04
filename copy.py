# noinspection PyUnresolvedReferences
from configparser import ConfigParser as CP
path = 'players.ini'
save_path = 'saves.ini'
# fh_in = open(path)
# print(*fh_in)
# fh_in.close()
# with open(path) as fh_in:
#     print(*fh_in)

# создаем объект парсера
file_ini = CP()
# читаем конфиг
file_ini.read(path)

# обрацение как к обычному словарю
#print(file_ini['player 1']['training'])


STATS = {}
SAVES = {}
def read_ini():
    global STATS, SAVES
    for player in file_ini.sections():
        tr = True if file_ini[player]['training'] == 'True' else False
        st = file_ini[player]['stats'].split(',')
        STATS[player] = {'trainigh': tr, 'stats': {'wins': int(st[0]), 'ties': int(st[1]), 'fails': int(st[2])}}

# Необходимо отчистить объект file_ini, иначе при последовательном чтении второго файла его поляы будут дозаписаны в объект file_ini
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
