def two_maximum(list):
    sorted_list = [x for x in set(x for x in list)]
    return tuple(sorted_list[:-3:-1])


if __name__ == '__main__':
    assert two_maximum([42, 3, 4, 5, 5, 6, 7, 2, 3]) == (42, 7)
