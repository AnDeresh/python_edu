'''
set1 = set((1, 2, 3))
print(set1)

set2 = set([1,2, 3])
print(set2)

a = 12
b = 12 + 2j
print(type(a), type(b))

import math

pi = math.pi
print(pi)
print(type(pi))

x = 0.7
y= -1
print(math.ceil(x)) #заокруглює до найближчого цілого вверх
print(math.floor(x)) #заокруглює до найближчого цілого вниз
print(math.copysign(y, x)) #число з першого, знак з другого
print(math.fabs(y)) #модуль
print(math.modf(5.7)) #повертає цілу і десяткову частину числа

print(math.trunc(5.9))
print(math.floor(5.9)) #відрізає число до цілого

print(math.pow(3, 2)) #X в степені Y
print(math.hypot(3, 4)) #гіпотенуза трикутника з катетами X, Y
'''

'''
str1 = "hello"
print(len(str1))
print(str1[0])
print(str1[-1])
print(str1[1:3])
print(str1[::2])
print(str1[::-1])
'''

'''
S = "s\np\ta\nbbb" #?
str3 = "hello"
print(str3.find("l")) #номер першого входження або -1
print(str3.rfind("l")) #номер останнього входження або -1
print(str3.replace("l", "m", 1))
print(str3.split("e")) #створює лист по розділювачу

str4 = 'one, two, three'
print(str4.split(","))

str5 = "324"
print(str5.isdigit())
print(str4.isalpha())

str6 = str4.split(",")
print(str4)
print(str6)
print(".".join(str6))

print(str3.count("l")) #hello
'''

'''
str7 = "One"
str8 = "Two"
str9 = "Three"
print("Hello, {}".format(str7))

print("{}, {}, {}".format(str7, str8, str9))
print("{2}, {0}, {1}".format(str7, str8, str9))
print("{}, {}, {}".format(*"abc"))

print("{0} {1} {0}".format(str7, str8))

print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord))

print("Units destroyed: {players[0]!r}".format(players = ['1', '2', '3']))
print("Units destroyed: {players[0]}".format(players = ['1', '2', '3']))
print("Units destroyed: {players[0]!s}".format(players = ['1', '2', '3']))
'''

'''
name = 'Alex'
age = 26

print(f'Hello {name}, you are {age}.')
print(f'Hello {name*2}.')

num = 2

def sqrnum(numb):
    return numb*numb

print(f'{num} squared is {sqrnum(num)}')
'''

'''
list_1 = [1, 2, 3, 'a']
str_1 = 'bcd'
list_2 = ['b', 'c', 'bc']
list_1.append(str_1) # вставляє повністю одним елементом str_1 в кінець list_1
print(list_1)
(list_1.append(list_2))
print(list_1)
'''

'''
list_1 = [1, 2, 3, 'a']
str_1 = 'bcd'
list_2 = ['b', 'c', 'bc', [1, 2]]
list_1.extend(str_1) # вставляє кожен елемент з str_1 в кінець list_1
print(list_1)
(list_1.extend(list_2))
print(list_1)
'''

'''
list_1 = [1, 2, 3, 'a']
str_1 = 'bcd'
list_2 = ['b', 'c', 'bc', [1, 2]]
list_1.insert(2, str_1) # бере str_1 і вставляє на 2 місце в list_1
print(list_1)
(list_1.insert(3, list_2))
print(list_1)
'''

'''
list_1 = [1, 2, 3, 'a', 2, 3]
list_1.remove(2)  # видаляє перший вказаний елемент
print(list_1)

list_2 = ['b', 'c', 'bc', [1, 2]]
list_2.pop(1) # видаляє елемент по індексу(остаанній, якщо не вказано) та повертає його
print(list_2) 
'''

'''
list_1 = [1, 2, 3, 'a', 2, 3]
print(list_1.index(3)) #повертає індекс першого вказаного елемента

list_2 = ['b', 'c', 'bc', [1, 2], 'b', 'c', 'b']
print(list_2.count('b')) # повертає кількість вказаних елементів
'''

'''
list_1 = [5, 6, 1, 2, 9]
list_2 = ['banana', 'pineapple', 'apple']

list_1.sort()  # [1, 2, 5, 6, 9]

list_1.sort(reverse=True)  # [9, 6, 5, 2, 1]

list_2.sort()  # ['apple', 'banana', 'pineapple']


def Fun(lst):
    return len(lst)


list_2.sort(reverse=False, key=Fun)
print(list_2)

list_2.reverse()
print(list_2)
'''

'''
old_list = [1, 2, 3, 4, 5, 6]
new_list = old_list.copy()
new_list2 = old_list[4:2:-1]
print(new_list)
print(new_list2)

list01 = [1, 2, 3, 4, 5, 6]
list01.clear()
print(list01)

list02 = [1, 2, 3, 4]

del list02
print(list02)
'''

'''
dict_01 = {'key_1': 1, 'key_2': 2}
dict_02 = dict(key_1=1, key_2=2)
dict_03 = dict.fromkeys(['key_1', 'key_2'])
dict_04 = dict.fromkeys(['key_1', 'key_2'], 100)
dict_05 = {a: a ** 2 for a in range(1, 7)}

print(dict_01['key_1'])
dict_01['key_3'] = 3
dict_01['key_2'] = 22
print(dict_01)

dict_02.clear()
print(dict_02)

my_dict = {'one': 1, }
print(my_dict.get('one'))

print(dict_01)
print(dict_01.items())
print(dict_01.keys())

dict_01.pop('key_1')  # видаляє пару по ключу і поверта значення
print(dict_01)

print(dict_05)
x = dict_05.popitem()  # видаляє останню пару та повертає кортеж з них
print(x)
print(dict_05)

dict_06 = {'key_1': 1, 'key_2': 2}
print(dict_06.setdefault('key_1'))
print(dict_06.setdefault('key_3', 3))  # добавляє в словник
print(dict_06)

dict_07 = {'key_1': 1, 'key_2': 2}
print(dict_07.get('key_1'))
print(dict_07.get('key_3', 3))  # не добавляє в словник
print(dict_07)

dict_08 = {'key_1': 1, 'key_2': 2}
dict_09 = {'key_3': 3}
dict_08.update(dict_09)
print(dict_08)

dict_08.update([('key_3', 33), ('key_4', 4)])
print(dict_08)

print(dict_08.values())
print(type(dict_08.values()))
'''


tpl_01 = ()
tpl_02 = 0, 1, 'a'

print(type(tpl_01), type(tpl_02))


