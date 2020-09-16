# N제곱의 효율성

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i  # 가장작은 원소의 인덱스
    print("min_index", min_index)

    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            print(array[min_index], ">", array[j])
            # 앞쪽에 있는것이 뒷쪽보다 크다면 min_index를 뒤쪽의 인덱스로 바꾼다. => 끝날때까지 반복
            min_index = j
    # 가장 작은 인덱스를 찾았고 그를 앞쪽 비교했던 요소와 위치를 바꾼다
    print("스왑", array[i], array[min_index], array[min_index], array[i])
    array[i], array[min_index] = array[min_index], array[i]  # 스왑
    print("스왑후: ", array)

print(array),
