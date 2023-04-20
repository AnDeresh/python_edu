def is_balanced(string: str) -> bool:
    res = 0
    for elem in string:
        if elem == '(':
            res += 1
        elif elem == ')':
            res -= 1
        if res < 0:
            return False
    return res == 0


if __name__ == '__main__':
    assert is_balanced("((((((2+2))))))") is True
    assert is_balanced("(2+2)/(2**2)") is True
    assert is_balanced("(2/4 + (5**2))") is True
    assert is_balanced("()()()()") is True
    assert is_balanced("(((1*2))") is False
    assert is_balanced(")()()()(") is False
    assert is_balanced("(2+2") is False
    assert is_balanced("()((2+2)(())()") is False
'''
    assert is_balanced("[((((((2+2))))))]") is True
    assert is_balanced("[(2+2)]/(2**2)") is True
    assert is_balanced("[{(2/4 + (5**2))}]") is True
    assert is_balanced("[][]{}") is True
    assert is_balanced("(((1*2)])") is False
    assert is_balanced(")()()()(") is False
    assert is_balanced("](2+2") is False
    assert is_balanced("{()(2+2)(())()]") is False
'''