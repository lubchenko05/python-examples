import time
import sys


"""
Есть последовательность чисел, содержащая как минимум 3 элемента, но которая может быть очень большой.
Элементы являются целыми числами, которые либо все чётные, либо все нечётные, за исключением одного.
Нужно написать скрипт, выводящий это единственное отличающееся число.

[0 8 2 50 13 6 34] -> 13
"""


# def timer(f):  # Use to check how much time need to run function
#     def wrapper(*args, **kwargs):
#         t_start = time.time()
#         result = f(*args, **kwargs)
#         print("Время выполнения %s: %.8f" % (f.__name__, time.time()-t_start))
#         return result
#     return wrapper


# @timer
def my_diff_digits(digits_list: list) -> int:
    if (digits_list[0] % 2 == 0 and digits_list[2] % 2 != 0) \
            or (digits_list[0] % 2 != 0 and digits_list[2] % 2 == 0):
        if (digits_list[0] % 2 == 0) and (digits_list[1] % 2 == 0) \
                or (digits_list[0] % 2 != 0) and (digits_list[1] % 2 != 0):
            return digits_list[2]
        else:
            return digits_list[0]
    elif (digits_list[0] % 2 == 0) != (digits_list[1] % 2 == 0):
        return digits_list[1]
    elif digits_list[0] % 2 == 0 and digits_list[1] % 2 == 0:
        return get_first_unpaired(digits_list)
    else:
        return get_first_paired(digits_list)


def get_first_paired(l):
    for i in l:
        if i % 2 == 0:
            return i


def get_first_unpaired(l):
    for i in l:
        if i % 2 != 0:
            return i

if __name__ == "__main__":
    try:
        digits = [int(i) for i in sys.argv[1:]]
        print(my_diff_digits(digits))
    except IndexError:
        print('Wrong input')
