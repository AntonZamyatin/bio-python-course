"""Task 5."""


def permutations(n):
    """Function.

    It returns list of all permutations of n numbers in
    tupples.
    """
    def gen_n(n, pref=[]):
        if len(pref) == n:
            yield tuple(pref)
        else:
            s = set(pref)
            for i in range(1, n + 1):
                if i not in s:
                    yield from gen_n(n, pref + [i])
    return list(gen_n(n))


def correctbracketsequences(n):
    """Function.

    I returns correct bracket sequence with length n.
    """
    def gen_n(n, pref='', balance=0):
        if len(pref) == 2 * n and balance == 0:
            yield pref
        else:
            for i in ('(', ')'):
                new_pref = pref + i
                new_balance = balance + (1 if i == '(' else -1)
                if len(new_pref) <= 2 * n and new_balance >= 0:
                    yield from gen_n(n, new_pref, new_balance)
    return list(gen_n(n))


def combinationswithrepeats(n, k):
    """Function.

    It returns list of all combinations with repeats from n by k.
    """
    def gen_n(n, k, pref=[]):
        if len(pref) == k:
            yield tuple(pref)
        else:
            m = max(pref) if len(pref) > 0 else 1
            for i in range(m, n + 1):
                yield from gen_n(n, k, pref + [i])
    return list(gen_n(n, k))


def unorderedpartitions(n):
    """Function.

    It returns list of all unpaired partitions of n.
    """
    def gen_n(n, pref=[]):
        if sum(pref) == n:
            yield tuple(pref)
        else:
            m = pref[-1] if len(pref) > 0 else 1
            for i in range(m, n - m + 2):
                new_pref = pref + [i]
                if sum(new_pref) <= n:
                    yield from gen_n(n, pref + [i])
    return list(gen_n(n))


if __name__ == "__main__":
    assert permutations(1) == [(1,)]
    assert permutations(2) == [(1, 2), (2, 1)]
    assert permutations(3) == [(1, 2, 3), (1, 3, 2), (2, 1, 3),
                               (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    print("permutations - OK")

    assert correctbracketsequences(1) == ['()']
    assert correctbracketsequences(2) == ['(())', '()()']
    assert correctbracketsequences(3) == ['((()))', '(()())', '(())()',
                                          '()(())', '()()()']
    print("correctbracketsequences - OK")

    assert combinationswithrepeats(1, 1) == [(1,)]
    assert combinationswithrepeats(2, 2) == [(1, 1), (1, 2), (2, 2)]
    assert combinationswithrepeats(3, 2) == [(1, 1), (1, 2), (1, 3), (2, 2),
                                             (2, 3), (3, 3)]
    print("combinationswithrepeats - OK")

    assert unorderedpartitions(1) == [(1,)]
    assert unorderedpartitions(3) == [(1, 1, 1), (1, 2), (3,)]
    assert unorderedpartitions(5) == [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 1, 3),
                                      (1, 2, 2), (1, 4), (2, 3), (5,)]
    print("unorderedpartitions - OK")
