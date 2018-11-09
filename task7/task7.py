"""Task 7."""

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


if __name__ == "__main__":
    assert valuesunion({1: 2, 4: 8}) == {2, 8}
    assert valuesunion({1: 2}, {4: 8}) == {2, 8}
    assert valuesunion({1: 2, 4: 8}, {'a': 'b'}, {}, {}) == {2, 8, 'b'}
    print("valuesunion - OK")

    assert popcount(0) == 0
    assert popcount(1) == 1
    assert popcount(10) == 2
    assert popcount(1023) == 10
    print("popcount - OK")

    print(powers(3, 1000000000))
    assert powers(3, 1000000000) == {1: 1, 2: 4, 3: 27}
    assert powers(4, 50) == {1: 1, 2: 4, 3: 27, 4: 6}
    assert powers(1, 1) == {1: 0}
    print("powers - OK")
