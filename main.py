""" Модуль верхнего уровня, для учебного проекта 1: Крестики-нолики """

# импорт дополнительных модулей проекта


# глобальные переменные
PLAYERS_INI_PATH = ''


# суперцикл
while True:
    command = input(' Для начала игры введите new для завершения exit: ').lower()

    if command in ('quit', 'exit', 'q', 'e'):
        break

    elif command in ('new', 'n'):

        def read_ini():
            """ Читает данные из файла """
            # читает из файла
            fh_in = open('players.ini')
            # сохраняет в переменную PLAYERS_INI
            PLAYERS_INI = fh_in.read()
            # закрывает файл
            fh_in.close()
            return PLAYERS_INI

        # сохраняет в глобальную переменную содержание файла players.ini
        PLAYERS_INI_PATH = read_ini()
        print(PLAYERS_INI_PATH.split())


        # начало партии
        def show_field():
            """ Выводит в стандартный поток игровое поле с ходами игроков """


        def check_win():
            """ Проверяет игровое поле, есть ли выигрышная комбинация """
            pass


# Пример вывода игрового поля

#  X | O |
# ———————————
#  O | X | X
# ———————————
#    |   |
