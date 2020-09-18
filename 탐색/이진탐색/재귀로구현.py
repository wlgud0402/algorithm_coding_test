def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end)//2

    if array[mid] == target:
        return mid + 1  # 인덱스를 0번째부터가아니라 1번째로 도출하기위해 마지막 결과에 +1을 해준다.
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
        # 타겟이보다 mid 의 값이 크다면 타겟은 mid보다 앞쪽에 있는것 =>  end를 mid -1 로 바꾼다.
    else:
        return binary_search(array, target, mid + 1, end)
        # 타겟이 array[mid] 보다 크다면 타겟은 mid보다 뒤쪽의 범위에 있는것 => start를 mid +1 로 바꾼다.


print(binary_search([1, 3, 4, 5, 6, 8, 9, 10], 6, 0, 7))
# binary_search(array, target, 0, n-1) 마지막 항의 인덱스는 길이-1 이므로 end = n-1이된다.
