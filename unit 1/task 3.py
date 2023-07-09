from functools import reduce

## 1
D = {'Женя': 89, 'Вася': 100, 'Марк': 71, 'Мария': 79}
f = sorted(list(filter(lambda x: D[x] > 80, D)))
print(f)
# Вася Женя

## 2
list1 = [2, 4, 6, 8, 10]
f = list(map(lambda x: x ** 3, list1))
print(f) # [8, 64, 216, 512, 1000]

## 3
list1 = [-1, 4, -7, -8, -10, 1, 0]
f = list(filter(lambda x: x < 0, list1))
print(f) # [-1, -7, -8, -10]

## 4
a = 8
list1 = reduce(lambda x, y: x * y, [i for i in range(1, a + 1)])
print(list1) # 40320

## 5
list1 = [2, 4, 6, 8, 0, 3, 4, 2, 3, 5, 1, 2]
list2 = max(list(filter(lambda x: (x**2 % 9 == 0), list1)))
list3 = max([x for x in list1 if x ** 2 % 9 == 0])
print(list2) # 6
