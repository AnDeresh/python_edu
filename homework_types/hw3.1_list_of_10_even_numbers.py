def lisf_even(even_numbers):
    list = [x for x in range(even_numbers * 2) if x % 2 == 0]
    return list


if __name__ == '__main__':
    assert lisf_even(5) == [0, 2, 4, 6, 8]
    assert lisf_even(2) == [0, 2]
    assert lisf_even(3) == [0, 2, 4]
