n, m = list(map(int, input().split(' ')))  # 띄어쓰기를 기준으로 나누기

array = list(map(int, input().split()))
array.sort()
start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1

    else:
        result = mid
        start = mid + 1

print(result)

# 이진탐색 없이


def search(array, target):
    answers = []
    array.sort()

    for i in range(len(array)):
        count = 0
        be_target = array[i]
        for i in array:
            if i > be_target:
                count += i - be_target
        if count >= target:
            answers.append(be_target)

    return max(answers)


# print(search([19, 15, 10, 17], 6))
