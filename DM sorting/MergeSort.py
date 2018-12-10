def merge(M:list, left, right, middle):
    """
    merge algorithm
    """
    A = M[left:middle:]
    B = M[middle:right:]
    print(A)
    print(B)
    C = [0]*(len(A)+len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]: # <= гарантирует устойчивость
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C


def merge_sort(A):
    if len(A) <= 1:
        return A
    middle = len(A) // 2
    left = 0
    right = len(A)
    merge_sort(A[left:middle:])
    merge_sort(A[middle:right:])
    C = merge(A,left,middle,right)
    for i in range(len(A)):
        A[i] = C[i]
    return A

print(merge_sort([1,5,2]))
