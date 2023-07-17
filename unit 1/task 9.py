## 1
# try:
#     line = [float(i) for i in input().split() if i != '/']
#     print(line[0]/line[1])
# except ZeroDivisionError:
#     print('ERROR')

## 2
def passwordValidation(*args):
    list1 = []
    for i in args:
        try:
            int(i, 16)
            list1.append(i)
        except ValueError:
            continue
    return list1

print(passwordValidation("password", "123456", "abcdef", "bcdefg"))

## 3
olympiad1 = {"name": "Пробная вышка",
"winners": {
"Олеся Олимпиадникова": 594,
"Олег Олимпиадников": 587,
"Онисим Олимпиадников": 581,
}
}
olympiad2 = {"name": "Горные воробьи",
"winners": {
"Ольга Олимпиадникова": (20, 20, 19, 20),
"Олеся Олимпиадникова": (19, 19, 20, 20, 17),
"Офелия Олимпиадникова": (20, 20, 20, 20, 13)
}
}


def check_winners(olympiad1, olympiad2, name):
    status = 'призер'
    try:
        points1 = olympiad1["winners"][name]
        status = 'победитель'
        print(f'[{olympiad1["name"]}] {status} {points1}')
    except KeyError:
        print(f'[{olympiad1["name"]}] {status}')
    finally:
        print("-" * 20)
    try:
        points2 = olympiad2["winners"][name][4]
        status = 'победитель'
        print(f'[{olympiad2["name"]}] {status} {points2}')
    except IndexError:
        status = 'победитель'
        print(f'[{olympiad2["name"]}] {status}')
    except KeyError:
        print(f'[{olympiad2["name"]}] {status}')
    finally:
        print("-" * 20)


check_winners(olympiad1, olympiad2, 'Ольга Олимпиадникова')
check_winners(olympiad1, olympiad2, 'Олеся Олимпиадникова')

## 4
def try_out():
    try:
        input()
    except KeyboardInterrupt:
        print("Ты не пройдёшь!")
        input()
try_out()

## 5
joke = """Заходит однажды тестировщик в бар.
Заказывает:
кружку лимонада,
2 кружки лимонада,
0 кружек лимонада,
999999999 кружек лимонада,
ящерицу в стакане,
–1 кружку лимонада,
qwerty кружек лимонада.
Первый реальный клиент заходит в бар и спрашивает, где туалет. Бар вспыхивает
пламенем."""