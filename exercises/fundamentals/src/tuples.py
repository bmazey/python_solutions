

def main():
    # tuples are immutable
    tuple1 = (1, 2, 3)

    # lists are mutable
    list1 = [1, 2, 3]

    tuple2 = append_to_sequence(tuple1)
    list2 = append_to_sequence(list1)

    # outputs (1, 2, 3)
    print('tuple1 = ', tuple1)

    # outputs (1, 2, 3, 9, 9, 9)
    print('tuple2 = ', tuple2)

    # outputs [1, 2, 3, 9, 9, 9]
    print('list1 = ', list1)

    # outputs [1, 2, 3, 9, 9, 9]
    print('list2 = ', list2)

    dictionary = {'hello': 'world', 'weight': 'African or European?'}

    # prints 'world'
    print(dictionary.get('hello'))

    # prints 'African or European?'
    print(dictionary.get('weight'))


def append_to_sequence(sequence):
    sequence += (9, 9, 9)
    return sequence


if __name__ == '__main__':
    main()
