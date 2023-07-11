## 1
from time import time

def timer(func):
    def new_func(*args, **kwargs):
        s = time()
        func(*args, **kwargs)
        print(time() - s)
    return new_func

@timer
def f1(x, y):
    print(x + y)

@timer
def f2():
    x = 0
    lst = []
    while x < 2 ** 19:
        if x % 11 == 0:
            lst.append(x)
        x += 1
    print(*lst[::204])

@timer
def f3(x):
    for i in range(x ** 2):
        for j in range(x):
            if i % 37 ** 2 == 0 and j % 41 == 0:
                for k in range(x ** 3, x ** 4, x):
                    if k % 17293660 == 0 and j % 2:
                        print(j - i + k)


f1(5, 4)
print()
f2()
print()
f3(100)

## 2
def cache(func):
    d = {}
    def new_func(x):
        if x not in d:
            d[x] = func(x)
        return d[x]
    return new_func

@cache
def fib(x):
    if x <= 1:
        return 1
    return fib(x - 2) + fib(x - 1)


for i in range(100):
    print(fib(i))

## 3
def logging(func):
    def new_func(x):
        with open('log.txt', 'a') as file:
            v = func(x)
            file.write(f'{x=} {v=}\n')
        return v
    return new_func

@logging
def func(x):
    return sum(i ** 3 for i in range(x) if i % 3)


for i in range(100):
    func(i)

## 4
from time import sleep

def retry(tries):
    def new_func(func):
        for i in range(tries):
            result = func()
            if result is not None:
                break
            sleep(1)
    return new_func


@retry(3)
def noneinator():
    print(17)
