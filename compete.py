from generate import generate
from datetime import datetime
from time import sleep


# sorting algorithms

def linear_sort(unsorted_list):
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


def bubble_sort(unsorted_list):
    is_sorted = False

    while not is_sorted:
        changes_made = 0

        for i in range(len(unsorted_list) - 1):

            if unsorted_list[i] > unsorted_list[i + 1]:
                unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
                changes_made += 1

        if changes_made == 0:
            is_sorted = True

    sorted_list = unsorted_list
    return sorted_list


def merge_sort(unsorted_list):

    # if list is large than 1
    if len(unsorted_list) > 1:

        # split list in halves
        left_half, right_half = split(unsorted_list)

        # sort left half
        sorted_left_half = merge_sort(left_half)

        # sort right half
        sorted_right_half = merge_sort(right_half)
    
        # merge halves
        sorted_list = merge(sorted_left_half, sorted_right_half)
        
        # return sorted list
        return sorted_list
    
    # if list is only one number
    else:
        # this is just for clarification
        sorted_list = unsorted_list
        return sorted_list


# merge_sort helper functions

def split(full_list):
    '''
    get length of list
    initialize both halves
    '''
    list_len = len(full_list)
    left_half, right_half = list(), list()

    '''
    iterate over each item in full_list
    and append to left half until i is greater than length / 2
    '''
    for i in range(list_len):
        if i < list_len / 2:
            left_half.append(full_list[i])
        else:
            right_half.append(full_list[i])

    return left_half, right_half


def merge(left_half, right_half):
    merged_list = list()
    both_halves_len = len(left_half) + len(right_half)

    for _ in range(both_halves_len):

            # if both lists have elements left
            if len(left_half) > 0 and len(right_half) > 0:

                # if right list has smallest number
                if left_half[0] > right_half[0]:
                    merged_list.append(right_half[0])
                    right_half.pop(0)

                # if left list has smallest number
                elif left_half[0] < right_half[0]:
                    merged_list.append(left_half[0])
                    left_half.pop(0)

                # if both lists have the same smallest number
                # use left list
                else:
                    merged_list.append(left_half[0])
                    left_half.pop(0)

            # else if only one list has element left
            else:
                if len(left_half) > 0:
                    merged_list.append(left_half[0])
                    left_half.pop(0)
                else:
                    merged_list.append(right_half[0])
                    right_half.pop(0)

    return merged_list


# print function

def sorting_animation(algorithm):
    for i in range(3):
        print('Sorting' + '.' * (i + 1), end='')
        print(' ' * (3 - i) + '   ' + algorithm)
        sleep(1)


# main function

def main():
    # user input for length
    n = int(input('\nLength of unsorted list: '))

    linear = generate(n)
    bubble = linear.copy()
    merge = linear.copy()

    print('\n-------- unsorted list --------')
    if len(linear) > 9:
        for i in range(9):
            print(linear[i], end=', ')
        
        print('...')
    else:
        for i in range(len(linear) - 1):
            print(linear[i], end=', ')
        
        print(linear[-1])
        
    print('-' * 31, end='\n\n')

    input('Press enter to start sorting...')
    print()

    sorting_animation('linear')
    timestamp_start = datetime.now()
    sorted_list = linear_sort(linear)
    timestamp_finish = datetime.now()
    print('Done', end='\n\n')
    sleep(1)
    duration_linear = timestamp_finish - timestamp_start

    sorting_animation('bubble')
    timestamp_start = datetime.now()
    sorted_list = bubble_sort(bubble)
    timestamp_finish = datetime.now()
    print('Done', end='\n\n')
    sleep(1)
    duration_bubble = timestamp_finish - timestamp_start

    sorting_animation('merge')
    timestamp_start = datetime.now()
    sorted_list = merge_sort(merge)
    timestamp_finish = datetime.now()
    print('Done', end='\n\n')
    sleep(1)
    duration_merge = timestamp_finish - timestamp_start

    print('\n------ sorting durations ------')
    duration = duration_linear
    print(f'Linear sort: {duration.seconds}.{duration.microseconds}s')
    duration = duration_bubble
    print(f'Bubble sort: {duration.seconds}.{duration.microseconds}s')
    duration = duration_merge
    print(f'Merge  sort: {duration.seconds}.{duration.microseconds}s')
    print('-' * 31)


main()
