import os
import time


RESET = '\033[0m'
RED = '\033[41m'
WHITE = '\033[107m'

GREEN = '\033[92m'
BLUE = '\033[94m'

def flag():
    """Флаг Швейцарии."""
    for row in range(9):
        line = ''

        for col in range(9):
            if ((3 <= row <= 5 and 1 <= col <= 7) or
                    (1 <= row <= 7 and 3 <= col <= 5)):
                line += WHITE + '  '
            else:
                line += RED + '  '

        print(line + RESET)


def pattern():
    """Повторяющийся узор j."""
    ring = [
        '  ██████  ',
        '████  ████',
        '██      ██',
        '██      ██',
        '████  ████',
        '  ██████  '
    ]

    for line in ring:
        print((line + '  ' + line + '    ') * 3)


def animation():
    """Анимация из четырёх кадров."""
    frames = [
        '●           ',
        '    ●       ',
        '        ●   ',
        '            ●'
    ]

    for frame in frames:
        os.system('cls')
        print('\033[H', end='')
        print(frame)
        time.sleep(0.5)


def diagram():
    """Диаграмма по данным из sequence.txt."""
    file = open('sequence.txt', 'r')

    inside = 0
    outside = 0

    for line in file:
        number = float(line)

        if -3 <= number <= 3:
            inside += 1
        else:
            outside += 1

    file.close()

    total = inside + outside

    inside_percent = inside / total * 100
    outside_percent = outside / total * 100

    inside_bar = '█' * round(inside_percent / 2)
    outside_bar = '█' * round(outside_percent / 2)

    print('Числа от -3 до 3:')
    print(
        GREEN + inside_bar + RESET,
        f'{inside_percent:.1f}% ({inside} чисел)'
    )

    print('Остальные числа:')
    print(
        BLUE + outside_bar + RESET,
        f'{outside_percent:.1f}% ({outside} чисел)'
    )


animation()

os.system('cls')

flag()
print()

pattern()
print()

diagram()