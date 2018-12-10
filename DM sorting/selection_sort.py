def selection_sort(a):
    n = len(a)
    swap_count = 0
    for i in range(n):
        min_pos = i
        for j in range(i, n):
            if a[j] < a[min_pos]:
                min_pos = j
        if min_pos != i:
            a[i], a[min_pos] = a[min_pos], a[i]
            swap_count += 1
        print(a, swap_count)
    return (a, swap_count)


if __name__ == "__main__":
    s = input()
    print(selection_sort(list(map(int, s.split()))))
