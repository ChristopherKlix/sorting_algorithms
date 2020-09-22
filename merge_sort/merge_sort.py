from util import generate_list, print_line, get_timestamp


def sort(unsorted_list):

    # if list is large than 1
    if len(unsorted_list) > 1:

        # split list in halves
        left_half, right_half = split(unsorted_list)

        # sort left half
        sorted_left_half = sort(left_half)

        # sort right half
        sorted_right_half = sort(right_half)
    
        # merge halves
        sorted_list = merge(sorted_left_half, sorted_right_half)
        
        # return sorted list
        return sorted_list
    
    # if list is only one number
    else:
        # this is just for clarification
        sorted_list = unsorted_list
        return sorted_list


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


def main():
    # print instructions
    print_line(30)
    print('# Welcome to sorting\n# Try list lengths of up to 100,000\n')
    print('# For easy overview, sorting works best with lists of 10-30 elements\n')
    print_line(30)

    # get user input for list length
    list_len = int(input('Length of unsorted list: '))

    unsorted_list = generate_list(list_len, 'random')

    # print initial unsorted list
    print_line(30)
    print('\n------- Unsorted list: -------')
    print(unsorted_list)

    # wait for user to start sorting
    print_line(30)
    input('Press enter to start sorting ')

    # sort list
    timestamp_start = get_timestamp()

    sorted_list = sort(unsorted_list)
        
    timestamp_finish = get_timestamp()

    duration = timestamp_finish - timestamp_start

    # print sorted list
    print('\n-------- Sorted list: --------')
    print(sorted_list)
    print_line(30)
    print(f'Duration: {duration.seconds}.{duration.microseconds}s')
    print_line(30)


main()
