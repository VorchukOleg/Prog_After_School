## 1
def sum_numbers(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_numbers(1, 2, 3))  # 6
print(sum_numbers(10, 20, 30, 40))  # 100

## 2
def print_kwargs(**kwargs):
    for i in kwargs:
        print(f'{i}: {kwargs[i]}')
print_kwargs(name='Alice', age=25, country='USA')
# name: Alice
# age: 25
# country: USA

## 3
def filter_by_length(len_str, *args):
    list1 = []
    for i in args:
        if len(i) >= len_str:
            list1.append(i)
    return list1

strings = ["hello", "world", "how", "are", "you"]
print(filter_by_length(4, *strings)) # ['hello', 'world']

## 4
def calculate_total_price(price, **kwargs):
    return price * (1 - (sum(kwargs[i] for i in kwargs) / 100))

print(calculate_total_price(100, student=10, coupon=20)) # 70.0
print(calculate_total_price(200, holiday=25)) # 150.0
print(calculate_total_price(500)) # 500

## 5
def custom_print(*args, **kwargs):
    separ = ' '
    ending = ''
    answer = ''
    for i in args:
        answer += str(i)
    for i in kwargs:
        if i == 'sep':
            separ = kwargs[i]
        elif i == 'end':
            ending = kwargs[i]
        else:
            answer += str(kwargs[i])
    print(answer, sep=separ, end=ending)


custom_print(1, 2, 3, a=4, b=5, sep='-', end='!')
# 1-2-3-a=4-b=5!
custom_print('Hello', 'World', sep=' ')
# Hello World
custom_print('apple', 'banana', 'cherry', sep=', ')
# apple, banana, cherry
custom_print(a=1, b=2, end='...')
# a=1 b=2...
