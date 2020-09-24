from util import generate_list, print_line, get_timestamp
from time import sleep

sleep_duration = 0


# actual sorting algorithm
def sort(unsorted_list):
    is_sorted = False
    # debug
    counter = 0

    while not is_sorted:
        print(f'Run: {counter + 1}')
        changes_made = 0

        for i in range(len(unsorted_list) - 1):

            if unsorted_list[i] > unsorted_list[i + 1]:
                # debug
                a = unsorted_list[i]
                b = unsorted_list[i + 1]

                unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
                changes_made += 1

                print(f'    swapped [{a}, {b}] -> [{b}, {a}]')
                sleep(sleep_duration * 0.2)

        if changes_made == 0:
            is_sorted = True
            print('Done')
        else:
            print(unsorted_list)
            print('Not yet sorted', end='\n\n')
            sleep(sleep_duration)

        counter += 1

    print(f'\nTotal runs: {counter}')
    sorted_list = unsorted_list
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

    # sgge retsae

    if list_len == 1:
        for i in range(5):  
            print (' Loading' + '.' * i, end='\r')
            sleep(1)
        print('\n\n')
        sleep(1)
        print('Looks like linear sort fell asleep...', end='\n\n')
        return

    if list_len == 42:
        while True:
            print('hehe')
            sleep(0.2)

    if list_len == 69:
        print('  /$$$$$$   /$$$$$$ ')
        print(' /$$__  $$ /$$__  $$')
        print('| $$  \__/| $$  \ $$')
        print('| $$$$$$$ |  $$$$$$$')
        print('| $$__  $$ \____  $$')
        print('| $$  \ $$ /$$  \ $$')
        print('|  $$$$$$/|  $$$$$$/')
        print(' \______/  \______/ ')
        return

    # set sleep duration

    global sleep_duration
    sleep_duration = 1 if input('Slow down sorting? [y/n] ').lower() == 'y' else 0

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
