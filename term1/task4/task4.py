"""Task 4."""


def factorial(n):
    """Factorial function."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def fibonacci(n):
    """Function. It returns n-th fibonacci number."""
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)


def recurrent(n):
    """Function. It returns number."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 0:
        return recurrent(n // 2)
    else:
        return recurrent((n - 1) // 2 + 1) + recurrent((n - 1) // 2)


def digitsum(n):
    """Function. It returns digit sum of n."""
    if n // 10 == 0:
        return n
    else:
        return n % 10 + digitsum(n // 10)


def reversestring(s):
    """Function. It return reversed string."""
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reversestring(s[0:-1])


def ackermann(m, n):
    """Function.  It return Ackermann number."""
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m - 1, 1)
    return ackermann(m-1, ackermann(m, n - 1))


def drawborders(n):
    """Fucnction draws boarders."""
    if n == 1:
        return ['+']
    elif n == 2:
        return ['++',
                '++']
    else:
        prev = drawborders(n - 2)
        answ = [0 for x in range(n)]
        answ[0] = '+'
        for i in range(n - 2):
            answ[0] += '-'
        answ[0] += '+'
        for i in range(1, n - 1):
            answ[i] = '|' + prev[i - 1] + '|'
        answ[n - 1] = '+'
        for i in range(n - 2):
            answ[n - 1] += '-'
        answ[n - 1] += '+'
        return answ


def genbinarystrings(n):
    """Function. It returns all binary strings with length n."""
    answ = []
    if n == 0:
        return ['']
    else:
        next = genbinarystrings(n-1)
        answ += list(map(lambda x: '0' + x, next)) + \
                list(map(lambda x: '1' + x, next))
    return answ


def istwopower(n):
    """Function. returns True if n = 2^x."""
    if n == 1:
        return True
    elif n <= 0:
        return False
    elif n % 2 == 0:
        return istwopower(n // 2)
    return False


def concatnumbers(a, b):
    """Function.

    Very strange recursive function for
    string concatination
    """
    if b // 10 == 0:
        return a*10 + b
    else:
        return concatnumbers(a, b // 10) * 10 + b % 10


def abacaba(n):
    """Freaking polyndrom function."""
    if n == 1:
        return [1]
    else:
        small = abacaba(n - 1)
        return small + [n] + small


def parentheses(s):
    """Text formating function."""
    if len(s) in {0, 1, 2}:
        return "(" + s + ")"
    else:
        return "(" + s[0] + parentheses(s[1: -1]) + s[-1] + ")"


def gcd(a, b):
    """Euclidean algorithm function."""
    return (b and gcd(b, a % b)) or a


def mergesort(a):
    """Merge sort recursive function."""
    if len(a) > 1:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]
        left = mergesort(left)
        right = mergesort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
    return a


if __name__ == "__main__":
    assert factorial(4) == 24
    assert factorial(0) == 1
    assert factorial(2) == 2
    print('factorial - OK')

    assert fibonacci(1) == 1
    assert fibonacci(4) == 3
    assert fibonacci(10) == 55
    print('fibonacci - OK')

    assert recurrent(2) == 1
    assert recurrent(3) == 2
    assert recurrent(5) == 3
    assert recurrent(7) == 3
    print('recurrent - OK')

    assert digitsum(0) == 0
    assert digitsum(123) == 6
    assert digitsum(192837465) == 45
    print('digitsum - OK')

    assert reversestring('') == ''
    assert reversestring('1') == '1'
    assert reversestring('asdf') == 'fdsa'
    assert reversestring('abacaba') == 'abacaba'
    print('reversestring - OK')

    assert ackermann(0, 10) == 11
    assert ackermann(1, 1) == 3
    assert ackermann(2, 2) == 7
    assert ackermann(2, 5) == 13
    assert ackermann(3, 3) == 61
    print('ackermann - OK')

    assert drawborders(1) == ['+']

    assert drawborders(2) == ['++',
                              '++']

    assert drawborders(3) == ['+-+',
                              '|+|',
                              '+-+']

    assert drawborders(4) == ['+--+',
                              '|++|',
                              '|++|',
                              '+--+']

    assert drawborders(5) == ['+---+',
                              '|+-+|',
                              '||+||',
                              '|+-+|',
                              '+---+']
    print('drawborders - OK')

    assert genbinarystrings(0) == ['']
    assert genbinarystrings(1) == ['0', '1']
    assert genbinarystrings(2) == ['00', '01', '10', '11']
    assert genbinarystrings(3) == ['000', '001', '010', '011', '100', '101',
                                   '110', '111']
    print('genbinarystrings - OK')

    assert istwopower(-5) is False
    assert istwopower(0) is False
    assert istwopower(1) is True
    assert istwopower(2) is True
    assert istwopower(4) is True
    assert istwopower(67) is False
    assert istwopower(1024) is True
    print('istwopower - OK')

    assert concatnumbers(1, 2) == 12
    assert concatnumbers(55, 88) == 5588
    assert concatnumbers(123, 789) == 123789
    assert concatnumbers(1000, 2) == 10002
    print('concatnumbers - OK')

    assert abacaba(1) == [1]
    assert abacaba(2) == [1, 2, 1]
    assert abacaba(3) == [1, 2, 1, 3, 1, 2, 1]
    assert abacaba(4) == [1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1]
    print('abacaba - OK')

    assert parentheses('example') == '(e(x(a(m)p)l)e)'
    assert parentheses('odd') == '(o(d)d)'
    assert parentheses('even') == '(e(ve)n)'
    print('parentheses - OK')

    assert gcd(1, 5) == 1
    assert gcd(4, 6) == 2
    assert gcd(18, 12) == 6
    assert gcd(283918822, 595730520) == 22
    print('gcd - OK')

    assert mergesort([]) == []
    assert mergesort([100]) == [100]
    assert mergesort([1, 3, 2]) == [1, 2, 3]
    assert mergesort([1, 3, 5, 4, 2]) == [1, 2, 3, 4, 5]
    print('mergesort - OK')
