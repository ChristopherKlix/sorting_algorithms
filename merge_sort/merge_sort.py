from util import generate_list, print_line, get_timestamp

show_debug = False


def sort(unsorted_list):
    print(f'---------------- sort {unsorted_list} ----------------')
    if len(unsorted_list) > 1:
        # split list in half
        if show_debug:
            print('split')
        half = len(unsorted_list)//2
        left_half = unsorted_list[:half]
        right_half = unsorted_list[half:]

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

        for i in range(len(unsorted_list)):
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
        return unsorted_list


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
    print(f'{duration.seconds}.{duration.microseconds}s')
    print_line(30)


main()
