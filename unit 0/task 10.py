## 1
def slovar(x):
    dic = {}
    for i in x:
        dic.update({i: i})
    return dic


list1 = [1, 2, 3, 4, 5]
print(slovar(list1)) # {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

## 2
n = 5
dic = {}
for i in range(1, n + 1):
    dic.update({i: i ** 2})

print(dic) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

## 3
dic = {'dat1': 375, 'data2': 567, 'data3': -37, 'data4': 21}
count = 1
for i in dic.keys():
    count *= dic[i]
print(count) # -165209625

## 4
punkt = set([i for i in ".,:;!?"])
count = 0
line = '''Летний день - это день, когда наступает летнее
солнцестояние и длительность дня достигает своего максимума. В разных странах и
регионах летние дни могут иметь разную продолжительность и характеризоваться
разными погодными условиями. Вообще, летние дни обычно ассоциируются с теплой
и ясной погодой, зелеными лугами, пляжами, купанием в море или озере,
пикниками и барбекю. В летние дни люди часто отдыхают и проводят время на открытом
воздухе, занимаются спортом, путешествуют и открывают новые места!'''
for i in line:
    if i in punkt:
        count += 1
print(count) # 12

## 5
ch = set([str(i) for i in range(10)])
v = set()
line = 'kn1mb9c7c5cv5cc9cvv7cx9sd8nm4cz2bm4k6hf9d'
for i in line:
    if i in ch:
        v.add(int(i))

otvet = ''
if len(v) > 0:
    for i in v:
        otvet += str(i)
    print(otvet) # 12456789
else:
    print('NO')