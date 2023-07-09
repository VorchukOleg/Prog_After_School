## 1
list1 = []
for i in range(1, 11):
    list1 = []
    for j in range(1, 11):
        list1.append(str(i * j))
    print('\t'.join(list1))

## 2
l = int(input())
r = int(input())
count = 0
for x in range(l, r + 1):
    for y in range(l, r + 1):
        for k in range(l, r + 1):
            if k ** 2 == x ** 2 + y ** 2:
                print(x, y, k)
                count += 1
print(count) # 26

## 3
def div(x):
    divs = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            divs.append(i)
            divs.append(x // i)
    return sum(divs)


N = 300
for i in range(1, N):
    for j in range(i):
        if i == (div(j) - j) and (div(i) - i) == j:
            print(i, j) # 284 220


## 4
n = 4
for x in range(1, 10):
    for y in range(0, 10):
        for z in range(0, 10):
            for t in range(0, 10):
                if int(f'{x}{y}{z}{t}') == x ** n + y ** n + z ** n + t ** n:
                    print(f'{x}{y}{z}{t}')
#1634
#8208
#9474