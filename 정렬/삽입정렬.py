# 기본적으로 N제곱의 효율성 but 거의 정렬되있는 상태의 경우 최선은 N의 효율성을 가진다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):  # 현재위치부터 첫번째 위치까지 돌면서 넣을 위치 찾아서 정렬
        if array[j] < array[j-1]:
            # 만약 다음항이 전항보다 크다면
            print(array[j], "<", array[j-1])
            print("스왑!", array[j], array[j-1], array[j-1], array[j])
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
    print("array for문 끝", array)
print(array)
