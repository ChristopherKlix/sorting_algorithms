from random import shuffle
import re
from datetime import datetime


def sort(unsorted_list):
    list_len = len(unsorted_list)
    smallest_int = 0
    sorted_list = list()

    for index in range(list_len):
        smallest_int = 1000000

        for element in unsorted_list:
            if element < smallest_int:
                smallest_int = element
        
        unsorted_list.remove(smallest_int)

        sorted_list.append(smallest_int)

    return sorted_list


def main():
    # print instructions
    print_line(30)
    print('# Welcome to sorting\n# Try list lengths of up to 100,000\n')
    print('# For easy overview, sorting works best with lists of 10-30 elements\n')
    print_line(30)

    # initialize an empty list
    unsorted_list = list()

    # get user input for list length
    list_len = int(input('Length of unsorted list: '))

    # generate a sorted list of length list_len
    for i in range(list_len):
        unsorted_list.append(i + 1)

    # shuffle list (make it unsorted)
    shuffle(unsorted_list)

    # print initial unsorted list
    print_line(20)
    print('Unsorted list:')
    print(unsorted_list)

    # wait for user to start sorting
    print_line(20)
    input('Press enter to start sorting ')

    # sort list
    timestamp_start = datetime.now()
    sorted_list = sort(unsorted_list)
    timestamp_finish = datetime.now()

    duration = timestamp_finish - timestamp_start

    # print sorted list
    print('\n-------- Sorted list: --------')
    print(sorted_list)
    print_line(30)
    print(f'{duration.seconds}.{duration.microseconds}s')
    print_line(30)


def print_line(n = 10):
    print('-' * n)


main()