# 계수정렬 (Count Sort)
# 빠른 정렬 (N + K)를 보장한다
# but 정렬하려는 값의 크기만큼의 리스트를 선언하므로 메모리 낭비의 가능성이 있다. ex)[2, 9999]의 경우 1만크기의 리스트를 생성
# => 동일한 값을 가진 데이터가 여러개 등장할때 효율적이다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# array = [1, 6, 4, 5, 8, 9, 3]
count = [0] * (max(array)+1)  # 크기만큼의 빈 배열을 생성해서 0으로 채워준다.

for i in range(len(array)):
    count[array[i]] += 1  # 각 데이터에 해당하는 인덱스의 값 증가
    print(count)

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
