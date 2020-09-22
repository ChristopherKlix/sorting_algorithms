from util import generate_list, print_line, get_timestamp


# actual sorting algorithm
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


# printing instructions and results etc.
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
