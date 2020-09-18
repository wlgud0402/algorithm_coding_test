from collections import deque
from pprint import pprint

run_count = 1
queue = deque()

matrix = [[1, 0, 1, 0, 1, 0],
          [1, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 1],
          [1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1]]

visited = [[False] * 6 for i in range(5)]
pprint(visited)


def maze(matrix, x, y, visited):
    global run_count
    if x < 0 or x > len(matrix) - 1 or \
            y < 0 or y > len(matrix[0]) - 1 or \
            matrix[x][y] == 0:
        print(x, y, " 이건 리턴할거야 끝! 조건에 맞지 않는 범위 이탈들")
        pprint(visited)
        return False

    if not visited[x][y]:
        queue.append((x, y))
        visited[x][y] = True

    while queue:
        queue.popleft()

        if x == 4 and y == 5:
            print("도착함", run_count)
            return run_count
        else:
            run_count += 1
            print("else문이 실행되고 run_count +=1")
            print(run_count)
            pprint(visited)
            print(x, y)

            if maze(matrix, x, y+1, visited) != False:
                return run_count

            if maze(matrix, x+1, y, visited) != False:
                return run_count

            if maze(matrix, x, y-1, visited) != False:
                return run_count

            if maze(matrix, x-1, y, visited) != False:
                return run_count

    return run_count


maze(matrix, 0, 0, visited)
