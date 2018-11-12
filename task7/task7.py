"""Task 7."""
import functools
import itertools

def valuesunion(*dicts):
    answ = set()
    for d in dicts:
        for el in d.values():
            answ.add(el)
    return answ

def popcount(n):
    s = bin(n)
    sum = 0
    for i in range(2, len(s)):
        if s[i] == '1':
            sum += 1
    return sum


def powers(n, m):
    answ = {}

    def power(n):
        a = 1
        for i in range(n):
            a *= n
        return a

    for i in range(1, n+1):
        answ[i] = power(i) % m
    return answ


def subpalindrome(s):
    max = 0
    answ = ''

    def is_palindrome(word):
        if len(word) == 1:
            return True
        return all(word[i] == word[-1*(i+1)] for i in range(len(word)//2))

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if is_palindrome(s[i:j]):
                if j - i > max:
                    answ = s[i:j]
                    max = j - i
                elif j - i == max:
                    if s[i:j] < answ:
                        answ = s[i:j]
    return answ


def isIPv4(s):
    for i in s:
        if i not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'):
            return False
    num = s.split('.')
    if len(num) != 4:
        return False
    for n in num:
        if int(n) < 0 or int(n) > 255:
            return False
        if n[0] == '0' and len(n) != 1:
            return False
    return True


def pascals():
    prev = (1,)

    for i in itertools.count(1):
        act = []
        act.append(1)
        for k in range(len(prev) - 1):
            act.append(prev[k] + prev[k + 1])
        act.append(1)
        yield tuple(prev)
        prev = act


def spiral(n):
    i = 1
    a = [[0 for i in range(n)] for j in range(n)]
    for l in range(n):
        a[0][l] = i
        i += 1
    h1 = 1
    h2 = n - 1
    v1 = 0
    v2 = n - 1
    while i <= (n*n):
        # down
        for l in range(h2 - h1 + 1):
            a[h1 + l][v2] = i
            i += 1
        v2 -= 1

        # left
        for l in range(v2 - v1 + 1):
            a[h2][v2 - l] = i
            i += 1
        h2 -= 1

        # up
        for l in range(h2 - h1 + 1):
            a[h2 - l][v1] = i
            i += 1
        v1 += 1

        # right
        for l in range(v2 - v1 + 1):
            a[h1][v1 + l] = i
            i += 1
        h1 += 1
    return a


def fibonacci(n):
    return functools.reduce(lambda x, n: [x[1], x[0] + x[1]],
                                      range(n), [0, 1])[0]


def brackets2(n, m, pref='', balance1=0, balance2=0):

    def count1(pref):
        return sum(map(lambda x: 1 if x in ('(', ')') else 0, pref))

    def count2(pref):
        return sum(map(lambda x: 1 if x in ('[', ']') else 0, pref))

    def stack_check(pref):
        stack = []
        for el in pref:
            n = len(stack)
            if n == 0:
                stack.append(el)
            elif stack[n - 1] == '(' and el == ')':
                stack.pop()
            elif stack[n - 1] == '['and el == ']':
                stack.pop()
            else:
                stack.append(el)
        if len(stack) == 0:
            return True
        else:
            return False

    if count1(pref) == 2 * n and count2(pref) == 2 * m\
       and balance1 == 0 and balance2 == 0 and stack_check(pref):
        yield pref
    else:
        for i in ('(', ')', '[', ']'):
            new_pref = pref + i
            if i == '(':
                new_balance1 = balance1 + 1
                new_balance2 = balance2
            elif i == ')':
                new_balance1 = balance1 - 1
                new_balance2 = balance2
            elif i == '[':
                new_balance2 = balance2 + 1
                new_balance1 = balance1
            elif i == ']':
                new_balance2 = balance2 - 1
                new_balance1 = balance1
            if count1(new_pref) <= 2 * n and count2(pref) <= 2 * m\
                        and new_balance1 >= 0 and new_balance2 >= 0:
                yield from brackets2(n, m, new_pref, new_balance1,
                                     new_balance2)


if __name__ == "__main__":
    assert valuesunion({1: 2, 4: 8}) == {2, 8}
    assert valuesunion({1: 2}, {4: 8}) == {2, 8}
    assert valuesunion({1: 2, 4: 8}, {'a': 'b'}, {}, {}) == {2, 8, 'b'}
    print("valuesunion - OK")

    assert popcount(0) == 0
    assert popcount(1) == 1
    assert popcount(10) == 2
    assert popcount(1023) == 10

    assert powers(3, 1000000000) == {1: 1, 2: 4, 3: 27}
    assert powers(4, 50) == {1: 1, 2: 4, 3: 27, 4: 6}
    assert powers(1, 1) == {1: 0}
    print("powers - OK")

    assert subpalindrome('abc') == 'a'
    assert subpalindrome('aaaa') == 'aaaa'
    assert subpalindrome('abaxfgf') == 'aba'
    assert subpalindrome('abacabad') == 'abacaba'
    print("subpalindrome - OK")

    assert isIPv4('192.168.0.15')
    assert isIPv4('255.255.255.255')
    assert not isIPv4('555.555.555.555')
    assert not isIPv4('190+2.168.0.0')
    assert not isIPv4('abacaba')
    assert not isIPv4('')
    print('isIPv4 - OK')

    it = pascals()
    for i in range(9):
        print(next(it))
    print("pascal - OK")

    assert spiral(1) == [[1]]
    assert spiral(2) == [[1, 2],
                         [4, 3]]
    assert spiral(4) == [[1, 2, 3, 4],
                         [12, 13, 14, 5],
                         [11, 16, 15, 6],
                         [10, 9, 8, 7]]
    print("spiral - OK")

    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    print("fibonacci - OK")

    assert list(brackets2(1, 0)) == ['()']
    assert list(brackets2(0, 1)) == ['[]']
    assert list(brackets2(1, 1)) == ['()[]', '([])', '[()]', '[]()']
    assert list(brackets2(3, 0)) == ['((()))', '(()())', '(())()', '()(())',
                                     '()()()']
    assert list(brackets2(2, 1)) == ['(())[]', '(()[])', '(([]))', '()()[]',
                                     '()([])', '()[()]', '()[]()', '([()])',
                                     '([]())', '([])()', '[(())]', '[()()]',
                                     '[()]()', '[](())', '[]()()']
    print("brackets - OK")
    print(subpalindrome("qfryinzykktqbvgdzaggxyjkw"))
