## 1
def summir(x):
    coumt = 0
    for i in x:
       coumt += i
    return coumt


list1 = [1, 7, 42, 12, 10, 1, 4, 0]
print(summir(list1)) # 77

## 2
def range_is(x):
    return list1[0] <= x <= list1[1]


list1 = [1, 9]
a = 7
print(range_is(a)) # True

## 3
def div(x):
    divs = [1]
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            divs.append(i)
            divs.append(x // i)

    return divs


def perfect(x):
    return sum(div(x)) == x


print(perfect(8128)) # True

## 4
def palindrom(x):
    return str(x) == str(x)[::-1]


print(palindrom(1234567899876554321)) # False

## 5
def div(x):
    divs = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            divs.append(i)
            divs.append(x // i)

    return divs


def prost(x):
    return len(div(x)) == 2


print(prost(123321)) # False

## 6
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 1
    return fib(n- 1) + fib(n - 2)


n = 10
print(fib(n)) # 34