"""Task 7."""
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
        return all(word[i] == word[-1*(i+1)] for i in range(len(word)//2))

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if i == j and max <= 1:
                if 1 > max:
                    answ = s[i]
                    max = 1
                elif max == 1:
                    if s[i] < answ:
                        answ = s[i]
            elif is_palindrome(s[i:j]):
                if j - i + 1 > max:
                    answ = s[i:j]
                    max = j - i + 1
                elif j - i + 1 == max:
                    if s[i:j] < answ:
                        answ = s[i:j + 1]
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
