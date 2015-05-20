__author__ = 'shivasankar G Sambandam'

import doctest      # Do not change or remove this line.


def coordinate(my_list):
    """(list) --> list
    Adds a unique index number to item in list and returns a list
    with the index number and item.

    >>> coordinate(['A', 'B', 'C', 'D'])
    ['00-A', '01-B', '02-C', '03-D']
    >>> coordinate(['Peter', 'Linus', 'Sara', 'Olive'])
    ['00-Peter', '01-Linus', '02-Sara', '03-Olive']
    >>> coordinate([])
    []
    """

    coordinate = []     # Do not change or remove this line.

    for i in my_list:
        index_val = my_list.index(i)
        val = '0%s-%s'%(index_val, i)
        coordinate.append(val)

    return coordinate       # Do not change or remove this line.


print doctest.testmod(verbose=True)     # Do not change or remove this line.

