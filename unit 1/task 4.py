## 1
# for i in ['Вотяку', 'Вотякову', 'Вотяковчу']:
#     for j in ['Александру', 'Алексу', 'Альберту']:
#         print(f"Диплом с отличием вручается {i} {j} Романовичу.")

## 2
# a = input()
# b = int(input())
# c = int(input())
# print(f"{a}{b:04}-{c:03}") # ABC0024-001

## 3
# a = int(input())
# b = int(input())
# print(f"{a:>9}\n {b:>8}\n {a + b:>8}")
#     10492
#       789
#     11281

## 4
# r = int(input()) / 100
# k = int(input())
# summa = 100_000_000
# for i in range(k):
#     summa += summa * r
# print(f'{summa:,.2f}') # 112,682,503.01

## 5
for a in range(1, 11):
    for b in range(a, 11):
        result = a * b
        if str(a * b)[-1] == '0':
            print(f'[DEBUG] {a=} {b=} {result=}')

## 6
def ip(a, b, c, d):

    s1 = ('{:08b}.' * 4)[:-1]
    s2 = ('{:b}.' * 4)[:-1]
    s3 = ('{:o}.' * 4)[:-1]
    s4 = ('{:x}.' * 4)[:-1]
    return s1.format(a, b, c, d), s2.format(a, b, c, d), s3.format(a, b, c, d), s4.format(a, b, c, d)


list1 = ip(*list(map(int, input().split())))
for i in list1:
    print(i)


