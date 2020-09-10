def ice(matrix):
    visited = set()  # 방문했던곳들 => 반복문을 돌면서 추가해줌 : 값이 0인 곳들만
    ice_count = 0

    def search(matrix, row, col, is_first_access=False):
        nonlocal ice_count  # global을 사용하지 않고 지역변수는 아닌 상위 부모에서 선언한 변수를 가져옴

        # row: 행의 범위가 첫번째 줄이나 마지막 줄에서 벗어났을 경우
        # col: 열의 범위가 첫번째 , 마지막 에서 벗어났을 경우
        if row < 0 or row > len(matrix) - 1 or \
            col < 0 or col > len(matrix[0]) - 1 or \
            matrix[row][col] == 1:
            # 방문한 곳이 1 즉 벽일 경우
            return
            # 실행하는 함수를 리턴시킨다

        if (row, col) in visited:
            return
            # visited에 현재의 값들이 있으면 함수 종료
        visited.add((row, col))
        # 방문하지 않은 곳이라면 추가해준다

        if is_first_access:
            ice_count += 1
        # 첫방문일 경우 ice_counte 를 1 추가해줌

        # 이경우 is_first_access에 대해 따로 지정하지 않았으므로 default => False가 된다.
        search(matrix, row, col + 1)
        search(matrix, row, col - 1)
        search(matrix, row + 1, col)
        search(matrix, row - 1, col)

    # 반복문을 돌면서 모든 점들의 경우를 확인 => search 를 실행한다.
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            search(matrix, row, col, is_first_access=True)

    print(visited)
    print(ice_count)


print(ice([
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]))