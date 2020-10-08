inpurt_data = input()
row = int(inpurt_data[1])
column = int(ord(inpurt_data[0])) - int(ord('a')) + 1
# 아스키코드로 변환해서 서로의 차이값으로 구하기

# 이동방향
moves = [(-2, -1), (-1, -2), (1, -2), (2, - 1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향 확인
result = 0
for move in moves:
    next_row = row + move[0]
    next_column = column + move[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
