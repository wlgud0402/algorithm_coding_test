def solution(n, plans):
    x, y = 1, 1

    map_size = []
    for j in range(1, n+1):
        map_size.append([[j, i] for i in range(1, n + 1)])

    start = [1, 1]
    for plan in plans:
        if plan == "R" and start[1] < 5:
            start[1] += 1
        if plan == "L" and start[1] > 1:
            start[1] -= 1
        if plan == "U" and start[0] > 1:
            start[0] -= 1
        if plan == "D" and start[0] < 5:
            start[0] += 1
    return start


print(solution(5, "RRRUDD"))
