def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end)//2

    if array[mid] == target:
        return mid + 1  # 인덱스를 0번째부터가아니라 1번째로 도출하기위해 마지막 결과에 +1을 해준다.
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


print(binary_search([1, 3, 4, 5, 6, 8, 9, 10], 6, 0, 7))
# binary_search(array, target, 0, n-1) 마지막 항의 인덱스는 길이-1 이므로 end = n-1이된다.
