from random import shuffle
import re

show_debug = False


def sort(list):
    print(f'---------------- sort {list} ----------------')
    if len(list) > 1:
        # split list in half
        if show_debug:
            print('split')
        half = len(list)//2
        left_half = list[:half]
        right_half = list[half:]

        # sort left half
        sorted_left_half = sort(left_half)
        if show_debug:
            print(f'sorted left half: {sorted_left_half}')

        # sort right half
        sorted_right_half = sort(right_half)
        if show_debug:
            print(f'sorted right half: {sorted_right_half}')
    
        # merge halves
        if show_debug:
            print(f'--- merge {sorted_left_half} and {sorted_right_half} ---')
        sorted_list = []

        for i in range(len(list)):
            if len(sorted_left_half) > 0 and len(sorted_right_half) > 0:
                if sorted_left_half[0] > sorted_right_half[0]:
                    sorted_list.append(sorted_right_half[0])
                    sorted_right_half.pop(0)

                elif sorted_left_half[0] < sorted_right_half[0]:
                    sorted_list.append(sorted_left_half[0])
                    sorted_left_half.pop(0)

                else:
                    sorted_list.append(sorted_left_half[0])
                    sorted_left_half.pop(0)

            elif len(sorted_left_half) > 0:
                sorted_list.append(sorted_left_half[0])
                sorted_left_half.pop(0)

            else:
                sorted_list.append(sorted_right_half[0])
                sorted_right_half.pop(0)
            if show_debug:
                print(sorted_list)
        
        # return sorted list
        if show_debug:
            print(f'merged: {sorted_list}')
        return sorted_list
    
    else:
        return list


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
    sorted_list = sort(unsorted_list)

    # print sorted list
    print('\n-------- Sorted list: --------')
    print(sorted_list)
    print_line(30)


def print_line(n = 10):
    print('-' * n)


main()
