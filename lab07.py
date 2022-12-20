import logging
# Работаем с логированием
logger = logging.getLogger("Logger")
logger.setLevel(logging.INFO)

# Создаем файл для логирования
file_handler = logging.FileHandler("pyy.log")
# Создаем форматер, отображающий дату, время, имя логгера, уровень и сообщение
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
while True: 
    try:
        logger.info('Program started')
        k = int(input('Введите координату клетки по горизонтали\nЧиcлo должно быть больше 0 и не больше 8\n '))
        if k > 8 or k <=0:
            print('Внимательно прочитайте текст и введите верные данные.')
            logger.error('Incorrect value.')
            continue
        l = int(input('Введите координату клетки по вертикали\nЧиcлo должно быть больше 0 и не больше 8\n '))
        if l > 8 or l <=0:
            print('Внимательно прочитайте текст и введите верные данные.')
            logger.error('Incorrect value.')
            continue
        m = int(input('Введите координату клетки по горизонтали\nЧиcлo должно быть больше 0 и не больше 8\n '))
        if m > 8 or m <=0:
            print('Внимательно прочитайте текст и введите верные данные.')
            logger.error('Incorrect value.')
            continue
        n = int(input('Введите координату клетки по вертикали\nЧиcлo должно быть больше 0 и не больше 8\n '))
        if n > 8 or n <=0:
            print('Внимательно прочитайте текст и введите верные данные.')
            logger.error('Incorrect value.')
            continue

    except ValueError:
        print('Внимательно прочитайте текст и введите верные данные.')
        logging.info("ValueError.")
        continue
    dx = abs(k - m)
    dy = abs(l - n)

    if (k + l + m + n) % 2 == 0:
        print('Да, являются')
        s = 1
    else:
        print('Нет, не явлются')
        s = 0
    print('Введите фигуру, расположенную на полях k, l \n 1 - Ферзь \n 2 - Ладья \n 3 - Слон \n 4 - Конь' )

    figure = int(input())

    if figure < 0 or figure > 4:
        print('Выберите число от 1 до 4, где каждое число - это опредленная фигура')
        logging.info("ValueError.")
        continue
    if figure == 1:

        if k == m or l == n or dx == dy:
            print(f"Ферзь угрожает фигуре, стоящей на клетках({m}; {n})")

        else:
            print(f"Ферзь не угрожает фигуре, стоящей на клетках ({m}; {n})")
            print(f'Чтобы за два хода попасть на фигуру, необходимо встать на поле ({m}; {l})')

    if figure == 2:

        if k == m or l == n:
            print(f"Ладья угрожает фигуре, стоящей на клетках ({m}; {n})")

        else:
            print(f"Ладья не угрожает фигуре, стоящей на клетках ({m}; {n})")
            print(f'Чтобы за два хода попасть на фигуру, необходимо встать на поле ({m}; {l})')

    if figure == 3:

        if dx == dy:
            print(f"Слон угрожает фигуре, стоящей на клетках ({m}; {n})")

        else:
            print(f"Слон не угрожает фигуре, стоящей на клетках ({m}; {n})")
            if s == 0:
                print(f"Слон никак не может угрожать фигуре, стоящей на клетках ({m}; {n}) ")

    if figure == 4:

        if dx == 1 and dy == 2 or dx == 2 and dy == 1:
            print(f"Конь угрожает фигуре, стоящей на клетках ({m}; {n})")

        else:
            print(f"Конь не угрожает фигуре, стоящей на клетках ({m}; {n})")
    break
logger.info('Program done')
