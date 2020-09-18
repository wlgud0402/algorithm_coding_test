def change(k, A, B):
    A.sort()
    B.sort(reverse=True)

    for i in range(3):
        if A[i] < B[i]:
            A[i], B[i] = B[i], A[i]
    return sum(A)


print(change(5, [1, 2, 5, 4, 3], [5, 5, 6, 6, 5]))
