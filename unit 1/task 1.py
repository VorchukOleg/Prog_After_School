# 1) 108

# 2) 5 35

# 3) 966

# 4) 36 6
from sys import getrefcount as grc

animals = ["cat", "cat", "dog", "dog", "bird", "capybara", "capybara", "capybara"]
d = {x: animals.count(x) for x in set(animals)}
print(sum(grc(x) for x in set(animals)), sum(x for x in (1, 2, 3)))

# 5) 15 21
backpack = ["capybara", "capyraba", "capyba", "capyba", "capybara",
2999, 2999, "capybara", [7, 7, 7], [7, 7, 7], [7, 7, 7],
[7, 7, 7]] + [[8, 8]] * 5
equal = 0
one = 0
for i in range(len(backpack)):
    for j in range(i + 1, len(backpack)):
        if backpack[i] is backpack[j]:
            one += 1
        if backpack[i] == backpack[j]:
            equal += 1
print(one, equal)

# 6) tomatoes pepper
salad = []
salad.append('lettuce')
salad.append('chicken')
salad.append('cheese')
salad.append('sauce')
salad.append('tomatoes')
salad.append('croutons')
salad.append(salad)
salad1 = salad.copy()
salad.append('salt')
salad.append('pepper')
print(salad1[-1][-3][-3][-3][4], salad1[-1][-3][-3][-3][-1])