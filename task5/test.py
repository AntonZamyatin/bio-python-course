def permutations(n, pref=[]):
    """Function.
    It returns list of all permutations of n numbers in
    tupples.
    """
    def gen_n(n, pref=[]):
        if len(pref) == n:
            return [tuple(pref)]
        else:
            s = set(pref)
            answ = []
            for i in range(1, n + 1):
                if i not in s:
                    answ += gen_n(n, pref + [i])
            return answ
    return gen_n(n)


print(permutations(5))
