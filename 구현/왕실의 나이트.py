def solution(position):
    position = list(position)
    widths = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8
    }

    width = widths[position[0]]
    height = int(position[1])

    start_position = [width, height]

    left_up = [-2, -1]
    left_down = [-2, 1]
    right_up = [2, -1]
    right_dowun = [2, 1]
    up_left = [-2, -1]
    up_right = [-2, 1]
    down_left = [2, -1]
    down_right = [2, 1]

    move_types = [left_up, left_down, right_up, right_dowun,
                  up_left, up_right, down_left, down_right]

    count = 0
    for move in move_types:
        if 0 < start_position[0] + move[0] < 9 and 0 < start_position[1] + move[1] < 9:
            count += 1
    print(count)


print(solution("c2"))
# 최대 출력 가지수 => 8개
