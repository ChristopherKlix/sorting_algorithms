from random import shuffle
from datetime import datetime


def generate_list(n, mode):
    # initialize an empty list
    generated_list = list()

    # generate a sorted list of length list_len
    for i in range(n):
        generated_list.append(i + 1)

    if mode == 'random':
        # shuffle list (make it unsorted)
        shuffle(generated_list)

    return generated_list


def print_line(n = 10):
    print('-' * n)


def get_timestamp():
    return datetime.now()