# pivot (기준 설정)=> 기준데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다.
# 평균 NlogN의 효율성
# 삽입정렬과 달게 이미 데이터가 정렬되어있는경우 매우 느리게 작동한다. 최대 N제곱

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return

    pivot = start  # 피벗은 첫번째 원소
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # 피벗보다 작은 데이터 찾을때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:  # 엇갈렸다면 작은 right -= 1 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은데이터와 큰 데이터를 교체
            array[left], array[pivot] = array[left], array[pivot]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각ㄲ 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


quick_sort(array, 0, len(array)-1)
print(array)
