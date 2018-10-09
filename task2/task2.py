def listToString(a):
    assert type(a) == list, "listToString argument is not a list"
    return str(a)


def addBorder(a):
    assert type(a) == list, "addBorder argument is not a list"
    assert len(a) > 0, "addBorder: empty list"
    length = len(a[0])
    equal_strings = True
    for string in a:
        if len(string) != length:
            equal_strings = False
    assert equal_strings, "addBorder: strings with not equal length"
    h_border = "+"
    for i in range(length):
        h_border += "-"
    h_border += "+"
    for i in range(len(a)):
        a[i] = "|" + a[i] + "|"
    return [h_border] + a + [h_border]


def shorting(e):
    assert type(e) == list, "shorting: not a list"
    for i in range(len(e)):
        if len(e[i]) > 10:
            e[i] = e[i][0] + str(len(e[i]) - 2) + e[i][len(e[i]) - 1]
    return e


def competition(e, k):
        advanced = 0
        for i in range(len(e)):
            if e[i] >= e[k] and e[i] > 0:
                advanced += 1
        return advanced


def goodPairs(a, b):
    answ = []
    answ_set = set()
    for i in a:
        for j in b:
            if (i * j) % (i + j) == 0:
                s = (i ** 2 + j ** 2)
                if s not in answ_set:
                    answ.append(s)
                    answ_set.add(s)
    answ.sort()
    return answ


def makeShell(n):
    answ = []
    for i in range(n):
        answ += [[0] * (i + 1)]
    for i in range(n-1, 0, -1):
        answ += [[0] * i]
    return answ


if __name__ == "__main__":

    assert listToString([]) == "[]", "listToString error"
    assert listToString([1, 2, 3]) == "[1, 2, 3]", "listToString error"
    assert listToString([-5]) == "[-5]", "listToString error"
    print("listToString - OK")

    ################

    assert addBorder(['abc',
                      'def']) == ['+---+',
                                  '|abc|',
                                  '|def|',
                                  '+---+'], \
        "addBorder error"
    print("addBorder - OK")

    ################

    assert shorting(['word', 'localization', 'internationalization',
                    'pneumonoultramicroscopicsilicovolcanoconiosis']) == \
        ['word', 'l10n', 'i18n', 'p43s'], "shorting error"
    print("shorting - OK")

    ################

    assert competition([5, 4, 3, 2, 1], 2) == 3, \
        "competition error"
    assert competition([1, 0, 0, 0], 3) == 1, \
        "competition error"
    assert competition([10, 9, 8, 7, 7, 7, 5, 5], 4) == 6, \
        "competition error"
    print("competition - OK")

    ################

    assert goodPairs([4, 5, 6, 7, 8], [8, 9, 10, 11, 12]) == [128, 160, 180], \
        "goodPairs error"
    assert goodPairs([2], [2]) == [8], \
        "goodPairs error"
    assert goodPairs([7, 8, 9], [5, 3, 2]) == [], \
        "goodPairs error"
    print("goodPairs - OK")

    #################

    assert makeShell(1) == [[0]], "makeShell error"
    assert makeShell(2) == [[0], [0, 0], [0]], "makeShell error"
    assert makeShell(3) == [[0], [0, 0], [0, 0, 0], [0, 0], [0]], \
        "makeShell error"
    print("makeShell - OK")
