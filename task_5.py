import re
import sys

"""
Написать скрипт, который принимает строку, состоящую из слов,
разделённых символом _ или - и возвращает строку в camel case. При этом регистр первого символа менять не нужно.

the_phantom_menace -> thePhantomMenace
The-Phantom-Menace -> ThePhantomMenace
"""


def repr_string(string: str) -> str:
    l = re.split('-|_', string)
    return l[0] + ''.join([i.title() for i in l[1:]])


if __name__ == '__main__':
    try:
        print(repr_string(sys.argv[1]))
    except IndexError:
        print('Wrong input')
