from random import shuffle

def generate(n):
    # initialize an empty list
    unsorted_list = list()

    # generate a sorted list of length list_len
    for i in range(n):
        unsorted_list.append(i + 1)

    # shuffle list (make it unsorted)
    shuffle(unsorted_list)

    return unsorted_list


n = int(input('Length: '))

print(generate(n))