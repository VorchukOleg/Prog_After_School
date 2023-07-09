## 1
x = int(input())
while (x % 2 != 0 and str(x)[-1] != '5'):
    x = int(input())

## 2
i = 0
while i < 10:
    print(i)
    i = i + 1

for i in range(10):
    print(i)

## 3
K = 12345
N = 56789
i = K
count = 0
while K <= i <= N:
    if i % 2 == 1:
        count += i
    i += 1
print(count)  # 768182441

## 4
N = int(input())  # 10
f = 1
for i in range(1, N + 1):
    f *= i
print(f)  # 3628800

## 5
N = int(input()) # 10
if N > 2:
    n1 = 1
    n2 = 1
    for i in range(3, N + 1):
        n1, n2 = n2, n1 + n2
    print(n2)
else:
    print('1')
# 55