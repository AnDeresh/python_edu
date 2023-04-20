'''
lst = [1, [2, 3], 4, [[6, 7]]]

to

lst = [1, 2, 3, 4, 6, 7]
'''

# lst = [1, [2, 3], 4, [[6, 7]]]
# str = ",".join(lst)
# lst2 = str.split(",")
#
# print(lst2)

'''
lst = [1, [2, 3], 4, [[6, 7]]]
lst2 = []

def openlist(x):
    for i in x:
        if type(i) == list:
            lst2.extend(i)
        else:
            lst2.extend(i)
    print(lst2)

openlist(lst)
'''

'''
lst = [1, [2, 3], 4, [[6, 7]]]

def clear(x):
    string = str(x)
    string2 = string.replace('[', '').replace(']', '')
    lstnew = string2.split(',') 
    lstclear = []
    for i in lstnew: #map використати
        lstclear.append(int(i))
    return lstclear
'''

'''
def clear(x):
    string = str(x)
    string2 = string.replace('[', '').replace(']', '')
    lstnew = string2.split(',')
    print(lstnew)
    def integer(i):
        return int(i)

    lstclear = list(map(integer, lstnew))
    return lstclear


clear(lst)

if __name__ == '__main__':
    assert clear([1, [22, 3], 4, [[6, 7]]]) == [1, 22, 3, 4, 6, 7]
    assert clear([[1, ], [2, 3], 4, [[6, 7], []], []]) == [1, 2, 3, 4, 6, 7]
'''

'''
def lstclear(x):
    string = str(x)
    lstclear = []
    for i in string:
        if i != '[' or ',' or ' ' or ']':
            lstclear.extend(i)
    return lstclear
'''

lst = [[1, ], [2, 3], 4, [[6, 7], []], []]


def clear(x):
    string = str(x)
    string2 = string.replace('[', '').replace(']', '').replace(' ', "")
    lstnew = string2.split(',')

    lstclear = list(map(int, (str_numb for str_numb in lstnew if str_numb.isdigit())))
    print(lstclear)
    return lstclear


if __name__ == '__main__':
    assert clear([1, [22, 3], 4, [[6, 7]]]) == [1, 22, 3, 4, 6, 7]
    assert clear([[1, ], [2, 3], 4, [[6, 7], []], []]) == [1, 2, 3, 4, 6, 7]
