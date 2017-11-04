import sys


"""
Написать скрипт, который составляет из списка положительных целых чисел максимально возможное число.

[70 8 20 1 13] -> 87020131
"""

if __name__ == "__main__":
    try:
        print(''.join(sorted(sys.argv[1:], reverse=True)))
    except IndexError or ValueError:
        print('Wrong input')
