## 1
# NameError: name 'b' is not defined
def f(a, b):
    return 18 * a * b


print(f(1, 2))  # 36

## 2
# NameError: name 'summa' is not defined
summa = 0
for i in range(1, 11):
    summa += i
print("The sum is: ", summa)  # 55


## 3
# TypeError: not all arguments converted during string formatting
def is_even(n):
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")


is_even(int('4'))  # 4 is even


## 4
def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4))  # 24


## 5
def is_palindrome(s):
    s = s.lower()
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


print(is_palindrome('qweq'))  # False


## 6
def multiplylist(lst):
    if len(lst) == 0:
        return None
    else:
        result = 1
        for i in range(len(lst)):
            result = result * lst[i]
        return result


print(multiplylist([1, 2, 3, 4]))  # 24
