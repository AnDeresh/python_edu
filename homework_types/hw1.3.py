def is_balanced(str) -> bool:
    res_1 = 0
    res_2 = 0
    res_3 = 0
    data_dict_1 = {'(': 1, ')': -1}
    data_dict_2 = {'[': 1, ']': -1}
    data_dict_3 = {'{': 1, '}': -1}
    for i in str:
        res_1 += data_dict_1.get(i, 0)
        res_2 += data_dict_2.get(i, 0)
        res_3 += data_dict_3.get(i, 0)
        if res_1 < 0 or res_2 < 0 or res_3 < 0:
            return False
    return res_1 == 0 and res_2 == 0 and res_3 == 0

if __name__ == '__main__':
    assert is_balanced("((((((2+2))))))") is True
    assert is_balanced("(2+2)/(2**2)") is True
    assert is_balanced("(2/4 + (5**2))") is True
    assert is_balanced("()()()()") is True
    assert is_balanced("(((1*2))") is False
    assert is_balanced(")()()()(") is False
    assert is_balanced("(2+2") is False
    assert is_balanced("()((2+2)(())()") is False
    assert is_balanced("[((((((2+2))))))]") is True
    assert is_balanced("[(2+2)]/(2**2)") is True
    assert is_balanced("[{(2/4 + (5**2))}]") is True
    assert is_balanced("[][]{}") is True
    assert is_balanced("(((1*2)])") is False
    assert is_balanced(")()()()(") is False
    assert is_balanced("](2+2") is False
    assert is_balanced("(2+2]") is False
    assert is_balanced("{()(2+2)(())()]") is False