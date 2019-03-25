def bubble_sort(a):
    n = len(a)
    phase = 0
    for i in range(n - 1):
        changed = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                changed = changed = True
        if not changed:
            break
        phase += 1
        print(a)
    return (a, phase)


if __name__ == "__main__":
    s = input()
    print(bubble_sort(list(map(int, s.split()))))
