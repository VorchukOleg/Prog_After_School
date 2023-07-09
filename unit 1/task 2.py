## 1
a = [2, 4, 6, 8]
b = {1, 3, 5, 7}
a_itera = iter(a)
b_iterb = iter(b)
next(iter(a_itera))
print(next(iter(a_itera)), next(iter(b_iterb)))
next(iter(b_iterb))
print(next(iter(b_iterb)), next(iter(a_itera)))
# 4 1
# 5 6

## 2
str='ППШ'
iterator=iter(str)
for x in iterator:
    print(x)
# П
# П
# Ш

## 3
d = {1: 'bee', 2: 'raccoon', 3: 'snake'}
iterator = iter(d)
print(d[next(iterator)])
# bee

## 4
a = [int(s) for s in range(1, 20)]
iterator = iter(a)
print(9 in iterator)
print(9 in iterator)
# True
# False

## 5
a = (i ** 2 for i in range (10) if i % 3 != 0)
print(next(a))
print(next(a))
print(next(a))
# 1 4 16

## 6
gener = (i ** 2 for i in range(1, 6))
print(next(gener))
next(gener)
print(next(gener))
next(gener)
print(next(gener))
# 1 9 25

## 7
koloda = (f'{x} {y}' for x in ['6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace'] for y in ['spades', 'clubs', 'diamonds', 'hearts'])
for i in range(37):
    print(next(koloda))

