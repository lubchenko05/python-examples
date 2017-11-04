import sys


"""
Написать скрипт, который принимает список строк, содержащий целые числа и слова и возвращает упорядоченную версию списка
В упорядоченной версии позиции чисел и строк должны сохраняться.

yellow white 2 5 green red 6 1 -> green red 1 2 white yellow 5 6
"""


def sort_string(l: list) -> list:
    d = []  # digits
    s = []  # strings
    v = []  # isdigit

    for i in l:
        if i.isdigit():
            d.append(int(i))
            v.append(1)
        else:
            s.append(i)
            v.append(0)

    s.sort(reverse=True)
    d.sort(reverse=True)

    return [str(d.pop()) if i else s.pop() for i in v]

if __name__ == "__main__":
    try:
        print(' '.join(sort_string(sys.argv[1:])))
    except IndexError:
        print('Wrong input')
