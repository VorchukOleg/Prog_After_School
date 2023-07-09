## 2
p1 = input()
p2 = input()
print(p1 == p2)  # False

## 3
a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(min(a, b, c, d))  # 5

## 4
a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(max(a, b, c, d))  # 30

## 5
a, b, c = int(input()), int(input()), int(input())
list1 = sorted([a, b, c], reverse=True)
print(list1[0] < sum(list1) - list1[0]) # True

## 6
a, b, c = int(input()), int(input()), int(input())
list1 = sorted([a, b, c], reverse=True)
if list1[0] < sum(list1) - list1[0]:
    if list1[0] == list1[1] == list1[2]:
        print('равносторонний')
    elif list1[0] == list1[1] or list1[1] == list1[2]:
        print('равнобедренный')
    else:
        print('разносторонний')

elif list1[0] == (list1[1] + list1[2]):
    print('вырожденный')
# вырожденный

## 7
a, b, c, d = int(input()), int(input()), int(input()), int(input())
list1 = [a, b]
list2 = [c, d]
count = 0
if b < c or d < a:
    print(count)
elif c < a and d < b:
    print(abs(a - d) + 1)
elif c > a and d > b:
    print(abs(c - b) + 1)
else:
    print(min(abs(b - a), abs(d - c)) + 1)
# 7