def incertion_sort(a):
    n = len(a)
    pairs = 0
    for i in range(n):
        p = i
        while p > 0 and a[p - 1] > a[p]:
            a[p - 1], a[p] = a[p], a[p - 1]
            pairs += 1
            p -= 1
    return(a, pairs)


if __name__ == "__main__":
    s = input()
    print(incertion_sort(list(map(int, s.split()))))
