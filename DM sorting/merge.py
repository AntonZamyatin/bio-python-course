def merge_sort(A, inversion_count=0):

    def merge(M: list, left, middle, right, inv_c1, inv_c2):
        """
        merge algorithm
        """
        inversion_count = inv_c1 + inv_c2
        A = M[left:middle]
        B = M[middle:right]
        C = [0]*(len(A)+len(B))
        i = j = n = 0
        while i < len(A) and j < len(B):
            if A[i] <= B[j]: # <= гарантирует устойчивость
                C[n] = A[i]
                i += 1
                n += 1
                inversion_count += j
            else:
                C[n] = B[j]
                j += 1
                n += 1
        while i < len(A):
            C[n] = A[i]
            i += 1
            n += 1
            inversion_count += j
        while j < len(B):
            C[n] = B[j]
            j += 1
            n += 1
        return (C, inversion_count)

    if len(A) <= 1:
        return (A, inversion_count)
    middle = len(A) // 2
    left = 0
    right = len(A)
    A[left:middle], inv_c1 = merge_sort(A[left:middle], inversion_count)
    A[middle:right], inv_c2 = merge_sort(A[middle:right], inversion_count)
    A, inversion_count = merge(A, left, middle, right, inv_c1, inv_c2)
    return (A, inversion_count)


if __name__ == "__main__":
    s = input()
    out = merge_sort(list(map(int, s.split())))
    print(out[1])
