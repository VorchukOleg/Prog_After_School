## 1
def return_str(name):
    text = ''
    with open(name) as f:
        for i in f.readlines():
            text += i.rstrip()
    return text


## 2
def first_str(name):
    text = ''
    with open(name) as f:
        text = f.readline()
    return text


## 3
def list_str(name):
    with open(name) as f:
        return f.readlines()


## 4
def lists_str(name):
    with open(name) as f:
        return [i.rstrip() for i in f.readlines()]


## 5:
def n_str(name):
    with open(name) as f:
        for i in f:
            print(i, end='')


## 6
def join_str(name):
    answer = []
    with open(name) as f:
        for i in f.readlines():
            answer.append(i.rstrip())
    return ' '.join(answer)


## 7
def clean_str(line):
    return line.rstrip()


## 8
def clean_str2(line):
    return line.rstrip('!?.')


## 9
def file_to_string(file, string):
    with open(file, 'w') as f:
        f.write(string)


## 10
def file_to_string2(file, string):
    with open(file, 'w') as f:
        f.write(string + '\n')


## 11
def in_file(file, list1):
    with open(file, 'w') as f:
        f.writelines(list1)


## 12
def twofiles(one, two):
    with open(one, 'r') as f:
        with open(two, 'w') as g:
            print(*f.readlines(), file=g)


## 13
def start_end(one, two):
    with open(one, 'r') as f:
        with open(two, 'w') as g:
            for line in f.readlines():
                if line.rstrip().startswith('hello') and line.rstrip().endswith('world'):
                    g.write(line)


## 14
def file_to_dic(file):
    dic = {}
    with open(file, 'r', encoding='Utf8') as f:
        first_line = f.readline()
        for line in f.readlines():
            list1 = line.rstrip().split()
            dic[list1[0]] = (list1[1], int(list1[2]))
    return dic
