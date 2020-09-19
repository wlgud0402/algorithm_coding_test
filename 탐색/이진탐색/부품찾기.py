def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end)//2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


# 판매자
n = int(input())  # input()은 기본적으로 str 이므로 int로 변환시켜야한다.
array = list(map(int, input().split()))
array.sort()

# 구매자
m = int(input())
x = list(map(int, input().split()))

# 구매자가 원하는 값들이 각각 target으로써 binary_search를 통해 판매자 array와 함께 탐색을 실행한다.
for i in x:
    result = binary_search(array, i, 0, n-1)

    if result != None:
        print('yse', end=' ')
    else:
        print('no', end=' ')
