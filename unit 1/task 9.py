## 1
try:
    line = [float(i) for i in input().split() if i != '/']
    print(line[0]/line[1])
except ZeroDivisionError:
    print('ERROR')

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

class Binge(Exception):
    pass
class Zero(Exception):
    pass
class LizardError(Exception):
    pass
class BurntBar(Exception):
    pass
class WrongOrder(Exception):
    pass


def joke():
    try:
        order = (input('Сколько кружек лимонада хотите?'))
        if order == 'ящерицу в стакан':
            raise LizardError
        if order == 'где туалет?':
            raise BurntBar
        if int(order) > 1:
            raise Binge
        if int(order) == 0:
            raise Zero
        if int(order) < 0:
            raise WrongOrder
        print('Ваша кружка!')
    except ValueError:
        print('Такого числа не существует')
    except Binge:
        print('Не стоит пить так много')
    except Zero:
        print('Спасибо за компанию!')
    except LizardError:
        print('Обратитесь в соседнюю дверь')
    except BurntBar:
        print('Бар сгорел')
    except WrongOrder:
        print('Отдайте ваши кружки!')
    joke()
joke()
