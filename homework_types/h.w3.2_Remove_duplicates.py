def remove_duplicates(list):
    list_2 = [x for x in set(x for x in list)]
    return list_2


if __name__ == '__main__':
    assert remove_duplicates([1, 2, 3, 3, 3, 4, 5, 5, 2, 2, 1]) == [1, 2, 3, 4, 5]
