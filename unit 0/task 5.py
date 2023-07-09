## 5
count = 0
a, b, n = int(input()), int(input()), int(input())
for i in range(n):
    c = int(input())
    if c > 10 and (c % 3 == 0 or c % 4 == 0):

        if c ** 2 == (a ** 2 + b ** 2):
            count += 1
print(count)