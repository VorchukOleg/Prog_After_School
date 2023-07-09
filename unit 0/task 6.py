## 5
list1 = []
count = (-1, '')
for i in input().split():
    list1.append(i)

for j in set(list1):
    if list1.count(j) > count[0]:
        count = (max(count[0], list1.count(j)), j)
print(count[1]) #cat